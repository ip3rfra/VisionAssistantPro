# -*- coding: utf-8 -*-
from .base import ProviderCapabilities
from .openai_api import build_chat_completions_payload


PROVIDER_ID = "groq"
DISPLAY_NAME = "Groq"
ORDER = 50
API_STYLE = "openai"
BASE_URL = "https://api.groq.com/openai"

CAPABILITIES = ProviderCapabilities(
    chat=True,
    vision=True,
    file_upload=False,
    audio_transcription=True,
    tts=False,
    model_listing=True,
    json_mode=True,
)


__all__ = ("CAPABILITIES", "build_chat_completions_payload")
