# -*- coding: utf-8 -*-
import importlib
import logging
import pkgutil
from dataclasses import dataclass

from .base import ProviderCapabilities, choose_provider_for_features


log = logging.getLogger(__name__)
FALLBACK_PROVIDER_AUTO = "auto"
FALLBACK_PROVIDER_CONFIG_KEYS = {
    "vision": "fallback_vision_provider",
    "file_upload": "fallback_file_upload_provider",
    "audio_transcription": "fallback_audio_provider",
    "tts": "fallback_tts_provider",
    "video_analysis": "fallback_video_provider",
    "operator": "fallback_operator_provider",
}
FALLBACK_FEATURE_PRIORITY = ("tts", "video_analysis", "file_upload", "audio_transcription", "operator", "vision")
FALLBACK_FEATURE_ORDER = {
    "tts": ("gemini", "openai", "custom"),
    "video_analysis": ("gemini", "custom"),
    "file_upload": ("gemini", "custom"),
    "audio_transcription": ("openai", "gemini", "groq", "mistral", "custom"),
    "operator": ("gemini", "openai", "mistral", "groq", "custom"),
    "vision": ("gemini", "openai", "mistral", "groq", "custom"),
}
NON_ADAPTER_MODULES = {"base", "registry"}


@dataclass(frozen=True)
class ProviderAdapter:
    provider_id: str
    display_name: str
    module_name: str
    module: object
    capabilities: ProviderCapabilities
    order: int = 100


@dataclass(frozen=True)
class ProviderFeatureStatus:
    provider_id: str
    supports: bool
    configured: bool
    available: bool


def adapter_from_module(module_name, module):
    provider_id = getattr(module, "PROVIDER_ID", "")
    if not provider_id:
        return None

    capabilities = getattr(module, "CAPABILITIES", None)
    if capabilities is None and hasattr(module, "capabilities_for"):
        capabilities = module.capabilities_for()
    if not isinstance(capabilities, ProviderCapabilities):
        return None

    return ProviderAdapter(
        provider_id=provider_id,
        display_name=getattr(module, "DISPLAY_NAME", provider_id),
        module_name=module_name,
        module=module,
        capabilities=capabilities,
        order=int(getattr(module, "ORDER", 100)),
    )


def discover_provider_adapters(package_name=__package__, search_paths=None):
    package = importlib.import_module(package_name)
    paths = search_paths or getattr(package, "__path__", ())
    adapters = {}
    for module_info in pkgutil.iter_modules(paths):
        name = module_info.name
        if name.startswith("_") or name in NON_ADAPTER_MODULES:
            continue
        module_name = f"{package_name}.{name}"
        try:
            module = importlib.import_module(module_name)
            adapter = adapter_from_module(module_name, module)
        except Exception:
            log.exception("Skipping provider adapter module %s", module_name)
            continue
        if adapter:
            adapters[adapter.provider_id] = adapter
    return dict(sorted(adapters.items(), key=lambda item: (item[1].order, item[0])))


PROVIDER_ADAPTERS = discover_provider_adapters()
PROVIDER_FALLBACK_ORDER = tuple(PROVIDER_ADAPTERS.keys())


def _adapters(adapters=None):
    return PROVIDER_ADAPTERS if adapters is None else adapters


def _ordered_provider_ids(adapters=None):
    return tuple(_adapters(adapters).keys())


def adapter_for(provider, adapters=None):
    return _adapters(adapters).get(provider)


def provider_choices(label_overrides=None, adapters=None):
    label_overrides = label_overrides or {}
    return tuple(
        (label_overrides.get(adapter.provider_id, adapter.display_name), adapter.provider_id)
        for adapter in _adapters(adapters).values()
    )


def capabilities_for(provider, custom_api_type="openai", custom_upload_support=False, adapters=None):
    adapter = adapter_for(provider, adapters=adapters)
    if not adapter:
        return ProviderCapabilities()
    if provider == "custom":
        return adapter.module.capabilities_for(custom_api_type, file_upload=custom_upload_support)
    capabilities = getattr(adapter.module, "CAPABILITIES", None)
    if isinstance(capabilities, ProviderCapabilities):
        return capabilities
    return adapter.capabilities


def capabilities_by_provider(custom_api_type="openai", custom_upload_support=False, adapters=None):
    return {
        provider: capabilities_for(
            provider,
            custom_api_type=custom_api_type,
            custom_upload_support=custom_upload_support,
            adapters=adapters,
        )
        for provider in _ordered_provider_ids(adapters)
    }


def fallback_provider_for_features(features, fallback_config=None, adapters=None):
    feature_set = set(features or ())
    fallback_config = fallback_config or {}
    provider_ids = set(_ordered_provider_ids(adapters))
    for feature in FALLBACK_FEATURE_PRIORITY:
        if feature not in feature_set:
            continue
        conf_key = FALLBACK_PROVIDER_CONFIG_KEYS[feature]
        provider = fallback_config.get(conf_key, FALLBACK_PROVIDER_AUTO)
        if provider in provider_ids:
            return provider
        return FALLBACK_PROVIDER_AUTO
    return FALLBACK_PROVIDER_AUTO


def _append_discovered_providers(order, adapters=None):
    providers = []
    seen = set()
    for provider in order:
        if provider in _adapters(adapters) and provider not in seen:
            providers.append(provider)
            seen.add(provider)
    for provider in _ordered_provider_ids(adapters):
        if provider not in seen:
            providers.append(provider)
            seen.add(provider)
    return tuple(providers)


def fallback_order_for_features(features, fallback_config=None, adapters=None):
    features = tuple(features or ())
    configured_fallback = fallback_provider_for_features(
        features,
        fallback_config=fallback_config,
        adapters=adapters,
    )
    if configured_fallback != FALLBACK_PROVIDER_AUTO:
        return (configured_fallback,)
    for feature in FALLBACK_FEATURE_PRIORITY:
        if feature in features:
            return _append_discovered_providers(FALLBACK_FEATURE_ORDER.get(feature, ()), adapters=adapters)
    return _ordered_provider_ids(adapters)


def resolve_provider_for_features(
    preferred_provider,
    features,
    configured_provider_ids,
    fallback_config=None,
    custom_api_type="openai",
    custom_upload_support=False,
    adapters=None,
):
    configured_fallback = fallback_provider_for_features(
        features,
        fallback_config=fallback_config,
        adapters=adapters,
    )
    if configured_fallback != FALLBACK_PROVIDER_AUTO:
        preferred_provider = None
    return choose_provider_for_features(
        preferred_provider=preferred_provider,
        features=tuple(features),
        capabilities_by_provider=capabilities_by_provider(
            custom_api_type=custom_api_type,
            custom_upload_support=custom_upload_support,
            adapters=adapters,
        ),
        configured_provider_ids=configured_provider_ids,
        fallback_order=fallback_order_for_features(features, fallback_config=fallback_config, adapters=adapters),
    )


def provider_feature_statuses(
    feature,
    configured_provider_ids,
    custom_api_type="openai",
    custom_upload_support=False,
    adapters=None,
):
    configured_provider_ids = set(configured_provider_ids or ())
    statuses = []
    for provider in _ordered_provider_ids(adapters):
        capabilities = capabilities_for(
            provider,
            custom_api_type=custom_api_type,
            custom_upload_support=custom_upload_support,
            adapters=adapters,
        )
        supports = bool(getattr(capabilities, feature, False))
        configured = provider in configured_provider_ids
        statuses.append(
            ProviderFeatureStatus(
                provider_id=provider,
                supports=supports,
                configured=configured,
                available=supports and configured,
            )
        )
    return tuple(statuses)
