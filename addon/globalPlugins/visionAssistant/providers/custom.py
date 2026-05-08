# -*- coding: utf-8 -*-
from dataclasses import replace

from .base import ProviderCapabilities
from .gemini import CAPABILITIES as GEMINI_COMPAT_CAPABILITIES
from .openai_api import CAPABILITIES as OPENAI_COMPAT_CAPABILITIES


PROVIDER_ID = "custom"
DISPLAY_NAME = "Custom"
ORDER = 60
API_STYLE = "custom"
CAPABILITIES = OPENAI_COMPAT_CAPABILITIES


def capabilities_for(api_type="openai", file_upload=False):
    base_capabilities = GEMINI_COMPAT_CAPABILITIES if api_type == "gemini" else OPENAI_COMPAT_CAPABILITIES
    return replace(base_capabilities, file_upload=bool(file_upload))


__all__ = ("capabilities_for", "ProviderCapabilities")
