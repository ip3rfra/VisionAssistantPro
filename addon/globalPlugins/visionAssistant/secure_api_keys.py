# -*- coding: utf-8 -*-
import ctypes
from ctypes import wintypes
import hashlib
import json
import os
import random
import time
from uuid import uuid4

import config
import globalVars
from logHandler import log

from .windows_aesgcm import WindowsAesGcm, b64decode_text, b64encode_bytes

_rng = random.SystemRandom()

_ADVAPI32 = ctypes.windll.advapi32
_KERNEL32 = ctypes.windll.kernel32

_PSECURITY_DESCRIPTOR = ctypes.c_void_p
_PACL = ctypes.c_void_p

_SDDL_REVISION_1 = 1
_SE_FILE_OBJECT = 1
_DACL_SECURITY_INFORMATION = 0x00000004
_PROTECTED_DACL_SECURITY_INFORMATION = 0x80000000
_SECURITY_SDDL_FILE = "D:P(A;;FA;;;SY)(A;;FA;;;BA)(A;;FA;;;OW)"
_SECURITY_SDDL_DIR = "D:P(A;OICI;FA;;;SY)(A;OICI;FA;;;BA)(A;OICI;FA;;;OW)"

_ADVAPI32.ConvertStringSecurityDescriptorToSecurityDescriptorW.argtypes = [
    wintypes.LPCWSTR,
    wintypes.DWORD,
    ctypes.POINTER(_PSECURITY_DESCRIPTOR),
    ctypes.POINTER(wintypes.DWORD),
]
_ADVAPI32.ConvertStringSecurityDescriptorToSecurityDescriptorW.restype = wintypes.BOOL
_ADVAPI32.GetSecurityDescriptorDacl.argtypes = [
    _PSECURITY_DESCRIPTOR,
    ctypes.POINTER(wintypes.BOOL),
    ctypes.POINTER(_PACL),
    ctypes.POINTER(wintypes.BOOL),
]
_ADVAPI32.GetSecurityDescriptorDacl.restype = wintypes.BOOL
_ADVAPI32.SetNamedSecurityInfoW.argtypes = [
    wintypes.LPWSTR,
    wintypes.DWORD,
    wintypes.DWORD,
    ctypes.c_void_p,
    ctypes.c_void_p,
    _PACL,
    ctypes.c_void_p,
]
_ADVAPI32.SetNamedSecurityInfoW.restype = wintypes.DWORD
_KERNEL32.LocalFree.argtypes = [ctypes.c_void_p]
_KERNEL32.LocalFree.restype = ctypes.c_void_p
_KERNEL32.GetFileAttributesW.argtypes = [wintypes.LPCWSTR]
_KERNEL32.GetFileAttributesW.restype = wintypes.DWORD
_KERNEL32.SetFileAttributesW.argtypes = [wintypes.LPCWSTR, wintypes.DWORD]
_KERNEL32.SetFileAttributesW.restype = wintypes.BOOL


def _token_bytes(size):
    return os.urandom(size)


def _token_hex(size):
    return os.urandom(size).hex()


def _randbelow(limit):
    if limit <= 0:
        raise ValueError("limit must be greater than zero.")
    return _rng.randrange(limit)


def _apply_windows_acl(path, is_dir=False):
    sddl = _SECURITY_SDDL_DIR if is_dir else _SECURITY_SDDL_FILE
    security_descriptor = _PSECURITY_DESCRIPTOR()
    if not _ADVAPI32.ConvertStringSecurityDescriptorToSecurityDescriptorW(
        sddl,
        _SDDL_REVISION_1,
        ctypes.byref(security_descriptor),
        None,
    ):
        raise ctypes.WinError(ctypes.get_last_error())
    try:
        dacl_present = wintypes.BOOL()
        dacl_defaulted = wintypes.BOOL()
        dacl = _PACL()
        if not _ADVAPI32.GetSecurityDescriptorDacl(
            security_descriptor,
            ctypes.byref(dacl_present),
            ctypes.byref(dacl),
            ctypes.byref(dacl_defaulted),
        ):
            raise ctypes.WinError(ctypes.get_last_error())
        if not dacl_present.value:
            raise RuntimeError("Missing DACL in security descriptor.")
        result = _ADVAPI32.SetNamedSecurityInfoW(
            ctypes.c_wchar_p(path),
            _SE_FILE_OBJECT,
            _DACL_SECURITY_INFORMATION | _PROTECTED_DACL_SECURITY_INFORMATION,
            None,
            None,
            dacl,
            None,
        )
        if result != 0:
            raise ctypes.WinError(result)
    finally:
        if security_descriptor.value:
            _KERNEL32.LocalFree(security_descriptor)


class _ApiKeyVault:
    _VERSION = 1
    _PREFIX = "va1:"
    _KEY_BYTES = 32
    _NONCE_BYTES = 12
    _MIN_SHARDS = 6
    _MAX_SHARDS = 10
    _DECOY_SHARDS = 4
    _NAMESPACE = "visionassistantpro.api.vault.v1"

    def __init__(self):
        digest = hashlib.sha256(self._NAMESPACE.encode("ascii")).hexdigest()
        self._store_dir_name = f".{digest[:10]}"
        self._key_file_name = f".{digest[10:26]}.bin"
        self._vault_file_name = f".{digest[26:42]}.dat"
        self._last_error = ""

    @staticmethod
    def _get_config_dir():
        app_args = getattr(globalVars, "appArgs", None)
        config_path = getattr(app_args, "configPath", None)
        if isinstance(config_path, str) and config_path:
            return config_path
        raise RuntimeError("NVDA config path unavailable (globalVars.appArgs.configPath).")

    def _storage_dir(self):
        return os.path.join(self._get_config_dir(), self._store_dir_name)

    @staticmethod
    def _harden_path(path, is_dir=False):
        try:
            _apply_windows_acl(path, is_dir=is_dir)
        except Exception as e:
            log.warning(f"Failed to apply ACL hardening to {path}: {e}")
        try:
            attrs = _KERNEL32.GetFileAttributesW(path)
            if attrs != 0xFFFFFFFF and not (attrs & 0x2):
                _KERNEL32.SetFileAttributesW(path, attrs | 0x2)
        except Exception as e:
            log.warning(f"Failed to set hidden attribute for {path}: {e}")

    def _key_path(self):
        return os.path.join(self._storage_dir(), self._key_file_name)

    def _vault_path(self):
        return os.path.join(self._storage_dir(), self._vault_file_name)

    def _ensure_storage_dir(self):
        os.makedirs(self._storage_dir(), exist_ok=True)
        self._harden_path(self._storage_dir(), is_dir=True)

    @staticmethod
    def _write_bytes_atomic(path, data):
        tmp = f"{path}.{uuid4().hex}.tmp"
        with open(tmp, "wb") as f:
            f.write(data)
        os.replace(tmp, path)
        _ApiKeyVault._harden_path(path, is_dir=False)

    @staticmethod
    def _write_json_atomic(path, payload):
        encoded = json.dumps(payload, separators=(",", ":"), ensure_ascii=True).encode("utf-8")
        _ApiKeyVault._write_bytes_atomic(path, encoded)

    @staticmethod
    def _read_json(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def _load_key(self, create_if_missing=False):
        path = self._key_path()
        if os.path.exists(path):
            with open(path, "rb") as f:
                data = f.read()
            if len(data) == self._KEY_BYTES:
                return data
            log.warning("Secure API key vault key has invalid length; regenerating key.")
        if not create_if_missing:
            return None
        self._ensure_storage_dir()
        key = _token_bytes(self._KEY_BYTES)
        self._write_bytes_atomic(path, key)
        return key

    def _encrypt_bytes(self, key, plaintext):
        nonce = _token_bytes(self._NONCE_BYTES)
        ciphertext, tag = WindowsAesGcm.encrypt(key, nonce, plaintext)
        return {
            "n": b64encode_bytes(nonce),
            "c": b64encode_bytes(ciphertext),
            "t": b64encode_bytes(tag),
        }

    def _decrypt_bytes(self, key, encrypted):
        nonce = b64decode_text(encrypted["n"])
        ciphertext = b64decode_text(encrypted["c"])
        tag = b64decode_text(encrypted["t"])
        return WindowsAesGcm.decrypt(key, nonce, ciphertext, tag)

    @staticmethod
    def _normalize_keys(keys):
        return [k.strip() for k in keys if isinstance(k, str) and k.strip()]

    def _encode_api_blob(self, keys, key):
        payload = {
            "v": self._VERSION,
            "keys": self._normalize_keys(keys),
            "ts": int(time.time()),
            "noise": b64encode_bytes(_token_bytes(10)),
        }
        payload_bytes = json.dumps(payload, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
        encrypted = self._encrypt_bytes(key, payload_bytes)
        encoded = b64encode_bytes(json.dumps(encrypted, separators=(",", ":"), ensure_ascii=True).encode("utf-8"))
        return f"{self._PREFIX}{encoded}"

    def _decode_api_blob(self, blob, key):
        if not isinstance(blob, str) or not blob.startswith(self._PREFIX):
            raise ValueError("Unknown API blob format.")
        encoded = blob[len(self._PREFIX):]
        encrypted = json.loads(b64decode_text(encoded).decode("utf-8"))
        payload = json.loads(self._decrypt_bytes(key, encrypted).decode("utf-8"))
        keys = payload.get("keys", [])
        normalized = self._normalize_keys(keys)
        if not normalized:
            raise ValueError("Vault payload does not contain API keys.")
        return normalized

    @staticmethod
    def _random_shard_id(used):
        while True:
            candidate = _token_hex(3)
            if candidate not in used:
                return candidate

    def _split_blob(self, blob):
        if len(blob) <= 1:
            return [blob]
        target = max(self._MIN_SHARDS, min(self._MAX_SHARDS, len(blob) // 56 + 1))
        target = max(2, min(target, len(blob)))
        cut_count = min(target - 1, len(blob) - 1)
        cut_points = set()
        while len(cut_points) < cut_count:
            cut_points.add(_randbelow(len(blob) - 1) + 1)
        points = sorted(cut_points)
        parts = []
        start = 0
        for end in points:
            parts.append(blob[start:end])
            start = end
        parts.append(blob[start:])
        return parts

    def _build_fragmented_payload(self, blob, key):
        parts = self._split_blob(blob)
        used_ids = set()
        shards = {}
        order = []
        for part in parts:
            shard_id = self._random_shard_id(used_ids)
            used_ids.add(shard_id)
            shards[shard_id] = part
            order.append(shard_id)
        for _ in range(max(self._DECOY_SHARDS, len(order) // 2)):
            shard_id = self._random_shard_id(used_ids)
            used_ids.add(shard_id)
            decoy_size = 12 + _randbelow(40)
            shards[shard_id] = b64encode_bytes(_token_bytes(decoy_size))
        manifest = {
            "v": self._VERSION,
            "order": order,
            "sha256": hashlib.sha256(blob.encode("utf-8")).hexdigest(),
            "noise": b64encode_bytes(_token_bytes(7)),
        }
        return {
            "v": self._VERSION,
            "s": shards,
            "m": self._encrypt_bytes(
                key,
                json.dumps(manifest, separators=(",", ":"), ensure_ascii=True).encode("utf-8"),
            ),
            "x": b64encode_bytes(_token_bytes(6)),
        }

    def _rebuild_blob(self, payload, key):
        shards = payload.get("s")
        if not isinstance(shards, dict) or not shards:
            raise ValueError("Invalid vault shards.")
        manifest_raw = self._decrypt_bytes(key, payload["m"]).decode("utf-8")
        manifest = json.loads(manifest_raw)
        order = manifest.get("order")
        if not isinstance(order, list) or not order:
            raise ValueError("Invalid vault manifest order.")
        parts = []
        for shard_id in order:
            part = shards.get(shard_id)
            if not isinstance(part, str):
                raise ValueError("Vault shard is missing.")
            parts.append(part)
        blob = "".join(parts)
        expected = manifest.get("sha256")
        actual = hashlib.sha256(blob.encode("utf-8")).hexdigest()
        if expected != actual:
            raise ValueError("Vault shard integrity check failed.")
        return blob

    def save_keys(self, keys):
        normalized = self._normalize_keys(keys)
        if not normalized:
            self.clear()
            return True
        try:
            key = self._load_key(create_if_missing=True)
            blob = self._encode_api_blob(normalized, key)
            payload = self._build_fragmented_payload(blob, key)
            self._ensure_storage_dir()
            self._write_json_atomic(self._vault_path(), payload)
            self._last_error = ""
            return True
        except Exception as e:
            self._last_error = str(e)
            log.error(f"Failed to store API keys in secure vault: {e}", exc_info=True)
            return False

    def load_keys(self):
        try:
            self._last_error = ""
            key = self._load_key(create_if_missing=False)
            vault_path = self._vault_path()
            if not key or not os.path.exists(vault_path):
                return []
            payload = self._read_json(vault_path)
            blob = self._rebuild_blob(payload, key)
            return self._decode_api_blob(blob, key)
        except Exception as e:
            self._last_error = str(e)
            log.warning(f"Failed to read secure API key vault: {e}")
            return []

    def clear(self):
        self._last_error = ""
        for path in (self._vault_path(), self._key_path()):
            try:
                if os.path.exists(path):
                    os.remove(path)
            except Exception as e:
                log.warning(f"Failed to remove secure vault file {path}: {e}")

    def get_last_error(self):
        return self._last_error


_api_key_vault = _ApiKeyVault()


def _split_api_keys(raw):
    if not raw:
        return []
    clean_raw = raw.replace("\r\n", ",").replace("\n", ",")
    return [k.strip() for k in clean_raw.split(",") if k.strip()]


def _persist_config():
    try:
        config.conf.save()
    except Exception as e:
        log.warning(f"Unable to persist config after API key update: {e}")


def load_configured_api_keys():
    secure_keys = _api_key_vault.load_keys()
    if secure_keys:
        return secure_keys
    legacy_raw = config.conf["VisionAssistant"]["api_key"]
    legacy_keys = _split_api_keys(legacy_raw)
    if legacy_keys and _api_key_vault.save_keys(legacy_keys):
        config.conf["VisionAssistant"]["api_key"] = ""
        _persist_config()
    return legacy_keys


def save_configured_api_keys(raw):
    keys = _split_api_keys(raw)
    if not keys:
        _api_key_vault.clear()
    elif not _api_key_vault.save_keys(keys):
        return False
    config.conf["VisionAssistant"]["api_key"] = ""
    _persist_config()
    return True


def has_configured_api_keys():
    return bool(load_configured_api_keys())


def api_keys_for_settings():
    return "\n".join(load_configured_api_keys())


def get_api_key_vault_last_error():
    return _api_key_vault.get_last_error()


def migrate_api_key_storage_if_needed():
    legacy_raw = config.conf["VisionAssistant"]["api_key"]
    legacy_keys = _split_api_keys(legacy_raw)
    if not legacy_keys:
        return
    if _api_key_vault.save_keys(legacy_keys):
        config.conf["VisionAssistant"]["api_key"] = ""
        _persist_config()
    else:
        log.warning("Unable to migrate plaintext API keys to secure vault; leaving legacy value in place.")
