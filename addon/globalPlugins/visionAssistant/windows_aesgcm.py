# -*- coding: utf-8 -*-
import base64
import ctypes


class _BCRYPT_AUTH_TAG_LENGTHS_STRUCT(ctypes.Structure):
    _fields_ = [
        ("dwMinLength", ctypes.c_ulong),
        ("dwMaxLength", ctypes.c_ulong),
        ("dwIncrement", ctypes.c_ulong),
    ]


class _BCRYPT_AUTHENTICATED_CIPHER_MODE_INFO(ctypes.Structure):
    _fields_ = [
        ("cbSize", ctypes.c_ulong),
        ("dwInfoVersion", ctypes.c_ulong),
        ("pbNonce", ctypes.c_void_p),
        ("cbNonce", ctypes.c_ulong),
        ("pbAuthData", ctypes.c_void_p),
        ("cbAuthData", ctypes.c_ulong),
        ("pbTag", ctypes.c_void_p),
        ("cbTag", ctypes.c_ulong),
        ("pbMacContext", ctypes.c_void_p),
        ("cbMacContext", ctypes.c_ulong),
        ("cbAAD", ctypes.c_ulong),
        ("cbData", ctypes.c_ulonglong),
        ("dwFlags", ctypes.c_ulong),
    ]


class WindowsAesGcm:
    _provider = None
    _initialized = False
    _tag_length = 16

    @staticmethod
    def _ensure_provider():
        if WindowsAesGcm._initialized:
            return WindowsAesGcm._provider
        provider = ctypes.WinDLL("bcrypt.dll", use_last_error=True)
        provider.BCryptOpenAlgorithmProvider.argtypes = [
            ctypes.POINTER(ctypes.c_void_p),
            ctypes.c_wchar_p,
            ctypes.c_wchar_p,
            ctypes.c_ulong,
        ]
        provider.BCryptOpenAlgorithmProvider.restype = ctypes.c_long
        provider.BCryptCloseAlgorithmProvider.argtypes = [ctypes.c_void_p, ctypes.c_ulong]
        provider.BCryptCloseAlgorithmProvider.restype = ctypes.c_long
        provider.BCryptSetProperty.argtypes = [
            ctypes.c_void_p,
            ctypes.c_wchar_p,
            ctypes.c_void_p,
            ctypes.c_ulong,
            ctypes.c_ulong,
        ]
        provider.BCryptSetProperty.restype = ctypes.c_long
        provider.BCryptGetProperty.argtypes = [
            ctypes.c_void_p,
            ctypes.c_wchar_p,
            ctypes.c_void_p,
            ctypes.c_ulong,
            ctypes.POINTER(ctypes.c_ulong),
            ctypes.c_ulong,
        ]
        provider.BCryptGetProperty.restype = ctypes.c_long
        provider.BCryptGenerateSymmetricKey.argtypes = [
            ctypes.c_void_p,
            ctypes.POINTER(ctypes.c_void_p),
            ctypes.c_void_p,
            ctypes.c_ulong,
            ctypes.c_void_p,
            ctypes.c_ulong,
            ctypes.c_ulong,
        ]
        provider.BCryptGenerateSymmetricKey.restype = ctypes.c_long
        provider.BCryptDestroyKey.argtypes = [ctypes.c_void_p]
        provider.BCryptDestroyKey.restype = ctypes.c_long
        provider.BCryptEncrypt.argtypes = [
            ctypes.c_void_p,
            ctypes.c_void_p,
            ctypes.c_ulong,
            ctypes.c_void_p,
            ctypes.c_void_p,
            ctypes.c_ulong,
            ctypes.c_void_p,
            ctypes.c_ulong,
            ctypes.POINTER(ctypes.c_ulong),
            ctypes.c_ulong,
        ]
        provider.BCryptEncrypt.restype = ctypes.c_long
        provider.BCryptDecrypt.argtypes = [
            ctypes.c_void_p,
            ctypes.c_void_p,
            ctypes.c_ulong,
            ctypes.c_void_p,
            ctypes.c_void_p,
            ctypes.c_ulong,
            ctypes.c_void_p,
            ctypes.c_ulong,
            ctypes.POINTER(ctypes.c_ulong),
            ctypes.c_ulong,
        ]
        provider.BCryptDecrypt.restype = ctypes.c_long
        WindowsAesGcm._provider = provider
        WindowsAesGcm._initialized = True
        return provider

    @staticmethod
    def _check(status, action):
        if int(status) != 0:
            code = int(status) & 0xFFFFFFFF
            raise RuntimeError(f"{action} failed (NTSTATUS=0x{code:08X}).")

    @staticmethod
    def _open_aes_algorithm(provider):
        alg_handle = ctypes.c_void_p()
        status = provider.BCryptOpenAlgorithmProvider(
            ctypes.byref(alg_handle),
            "AES",
            None,
            0,
        )
        WindowsAesGcm._check(status, "BCryptOpenAlgorithmProvider")
        try:
            mode = ctypes.create_unicode_buffer("ChainingModeGCM")
            status = provider.BCryptSetProperty(
                alg_handle,
                "ChainingMode",
                ctypes.cast(mode, ctypes.c_void_p),
                ctypes.sizeof(mode),
                0,
            )
            WindowsAesGcm._check(status, "BCryptSetProperty(ChainingModeGCM)")
            return alg_handle
        except Exception:
            provider.BCryptCloseAlgorithmProvider(alg_handle, 0)
            raise

    @staticmethod
    def _get_algorithm_properties(provider, alg_handle):
        object_length = ctypes.c_ulong()
        result_len = ctypes.c_ulong()
        status = provider.BCryptGetProperty(
            alg_handle,
            "ObjectLength",
            ctypes.byref(object_length),
            ctypes.sizeof(object_length),
            ctypes.byref(result_len),
            0,
        )
        WindowsAesGcm._check(status, "BCryptGetProperty(ObjectLength)")

        tag_lengths = _BCRYPT_AUTH_TAG_LENGTHS_STRUCT()
        status = provider.BCryptGetProperty(
            alg_handle,
            "AuthTagLength",
            ctypes.byref(tag_lengths),
            ctypes.sizeof(tag_lengths),
            ctypes.byref(result_len),
            0,
        )
        WindowsAesGcm._check(status, "BCryptGetProperty(AuthTagLength)")
        tag_len = WindowsAesGcm._tag_length
        if tag_len < int(tag_lengths.dwMinLength) or tag_len > int(tag_lengths.dwMaxLength):
            tag_len = int(tag_lengths.dwMaxLength)
        return int(object_length.value), tag_len

    @staticmethod
    def _create_key(provider, alg_handle, key, key_object_length=None):
        if key_object_length is None:
            key_object_length, _ = WindowsAesGcm._get_algorithm_properties(provider, alg_handle)
        key_object = ctypes.create_string_buffer(key_object_length)
        key_material = ctypes.create_string_buffer(key, len(key))
        key_handle = ctypes.c_void_p()
        status = provider.BCryptGenerateSymmetricKey(
            alg_handle,
            ctypes.byref(key_handle),
            key_object,
            len(key_object),
            ctypes.cast(key_material, ctypes.c_void_p),
            len(key),
            0,
        )
        WindowsAesGcm._check(status, "BCryptGenerateSymmetricKey")
        return key_handle, key_object

    @staticmethod
    def _build_auth_info(nonce_buf, nonce_len, tag_buf, tag_len):
        auth_info = _BCRYPT_AUTHENTICATED_CIPHER_MODE_INFO()
        auth_info.cbSize = ctypes.sizeof(_BCRYPT_AUTHENTICATED_CIPHER_MODE_INFO)
        auth_info.dwInfoVersion = 1
        auth_info.pbNonce = ctypes.cast(nonce_buf, ctypes.c_void_p)
        auth_info.cbNonce = nonce_len
        auth_info.pbTag = ctypes.cast(tag_buf, ctypes.c_void_p)
        auth_info.cbTag = tag_len
        return auth_info

    @staticmethod
    def encrypt(key, nonce, plaintext):
        if len(key) != 32:
            raise ValueError("Invalid AES key length.")
        if len(nonce) != 12:
            raise ValueError("Invalid AES-GCM nonce length.")
        if not plaintext:
            raise ValueError("Plaintext cannot be empty.")

        provider = WindowsAesGcm._ensure_provider()
        alg_handle = WindowsAesGcm._open_aes_algorithm(provider)
        key_handle = ctypes.c_void_p()
        try:
            key_object_length, tag_len = WindowsAesGcm._get_algorithm_properties(provider, alg_handle)
            key_handle, _ = WindowsAesGcm._create_key(provider, alg_handle, key, key_object_length)
            nonce_buf = ctypes.create_string_buffer(nonce, len(nonce))
            tag_buf = ctypes.create_string_buffer(tag_len)
            plain_buf = ctypes.create_string_buffer(plaintext, len(plaintext))
            out_buf = ctypes.create_string_buffer(len(plaintext))
            auth_info = WindowsAesGcm._build_auth_info(nonce_buf, len(nonce), tag_buf, tag_len)
            out_len = ctypes.c_ulong()
            status = provider.BCryptEncrypt(
                key_handle,
                ctypes.cast(plain_buf, ctypes.c_void_p),
                len(plaintext),
                ctypes.byref(auth_info),
                None,
                0,
                ctypes.cast(out_buf, ctypes.c_void_p),
                len(plaintext),
                ctypes.byref(out_len),
                0,
            )
            WindowsAesGcm._check(status, "BCryptEncrypt")
            return out_buf.raw[: out_len.value], tag_buf.raw[:tag_len]
        finally:
            if key_handle.value:
                provider.BCryptDestroyKey(key_handle)
            if alg_handle.value:
                provider.BCryptCloseAlgorithmProvider(alg_handle, 0)

    @staticmethod
    def decrypt(key, nonce, ciphertext, tag):
        if len(key) != 32:
            raise ValueError("Invalid AES key length.")
        if len(nonce) != 12:
            raise ValueError("Invalid AES-GCM nonce length.")
        if not ciphertext:
            raise ValueError("Ciphertext cannot be empty.")
        if not tag:
            raise ValueError("Missing AES-GCM tag.")

        provider = WindowsAesGcm._ensure_provider()
        alg_handle = WindowsAesGcm._open_aes_algorithm(provider)
        key_handle = ctypes.c_void_p()
        try:
            key_handle, _ = WindowsAesGcm._create_key(provider, alg_handle, key)
            nonce_buf = ctypes.create_string_buffer(nonce, len(nonce))
            tag_buf = ctypes.create_string_buffer(tag, len(tag))
            cipher_buf = ctypes.create_string_buffer(ciphertext, len(ciphertext))
            out_buf = ctypes.create_string_buffer(len(ciphertext))
            auth_info = WindowsAesGcm._build_auth_info(nonce_buf, len(nonce), tag_buf, len(tag))
            out_len = ctypes.c_ulong()
            status = provider.BCryptDecrypt(
                key_handle,
                ctypes.cast(cipher_buf, ctypes.c_void_p),
                len(ciphertext),
                ctypes.byref(auth_info),
                None,
                0,
                ctypes.cast(out_buf, ctypes.c_void_p),
                len(ciphertext),
                ctypes.byref(out_len),
                0,
            )
            WindowsAesGcm._check(status, "BCryptDecrypt")
            return out_buf.raw[: out_len.value]
        finally:
            if key_handle.value:
                provider.BCryptDestroyKey(key_handle)
            if alg_handle.value:
                provider.BCryptCloseAlgorithmProvider(alg_handle, 0)


def b64encode_bytes(data):
    return base64.urlsafe_b64encode(data).decode("ascii")


def b64decode_text(text):
    return base64.urlsafe_b64decode(text.encode("ascii"))
