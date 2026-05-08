# -*- coding: utf-8 -*-
import json
from urllib import request

from .base import ProviderCapabilities
from .openai_api import build_chat_completions_payload, build_json_headers


PROVIDER_ID = "mistral"
DISPLAY_NAME = "Mistral AI"
ORDER = 40
API_STYLE = "openai"
BASE_URL = "https://api.mistral.ai"

CAPABILITIES = ProviderCapabilities(
    chat=True,
    vision=True,
    file_upload=False,
    audio_transcription=True,
    tts=False,
    model_listing=True,
    json_mode=True,
)


def build_ocr_payload(document_data, mime_type, model="mistral-ocr-latest"):
    document_type = "document_url" if "pdf" in str(mime_type).lower() else "image_url"
    return {
        "model": model,
        "document": {
            "type": document_type,
            document_type: f"data:{mime_type};base64,{document_data}",
        },
    }


def send_ocr_request(opener, url, key, payload, timeout=120):
    req = request.Request(url, data=json.dumps(payload).encode(), headers=build_json_headers(key))
    with opener.open(req, timeout=timeout) as response:
        res = json.loads(response.read().decode())
    return "\n\n".join(page.get("markdown", "") for page in res.get("pages", []))


__all__ = (
    "CAPABILITIES",
    "PROVIDER_ID",
    "DISPLAY_NAME",
    "ORDER",
    "API_STYLE",
    "BASE_URL",
    "build_chat_completions_payload",
    "build_ocr_payload",
    "send_ocr_request",
)
