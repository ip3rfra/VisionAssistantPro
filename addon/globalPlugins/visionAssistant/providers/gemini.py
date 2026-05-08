# -*- coding: utf-8 -*-
import json
from urllib import request

from .base import ProviderCapabilities


PROVIDER_ID = "gemini"
DISPLAY_NAME = "Google Gemini"
ORDER = 10
API_STYLE = "gemini"
BASE_URL = "https://generativelanguage.googleapis.com"

CAPABILITIES = ProviderCapabilities(
    chat=True,
    vision=True,
    file_upload=True,
    audio_transcription=True,
    tts=True,
    model_listing=True,
    json_mode=True,
    video_analysis=True,
)

SAFETY_SETTINGS = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
]


def build_generate_content_payload(ai_request, temperature=0.7, safety_settings=None):
    payload = {
        "contents": generate_content_contents(ai_request),
        "generationConfig": {"temperature": temperature},
        "safetySettings": list(safety_settings or SAFETY_SETTINGS),
    }
    if ai_request.json_mode:
        payload["generationConfig"]["response_mime_type"] = "application/json"
    return payload


def send_generate_content_request(opener, url, key, payload, timeout=180):
    req = request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json", "x-goog-api-key": key},
    )
    with opener.open(req, timeout=timeout) as response:
        return json.loads(response.read().decode())


def parse_generate_content_response(data):
    return data["candidates"][0]["content"]["parts"][0].get("text", "")


def parse_models_response(data):
    models_info = []
    for model in data.get("models", []):
        model_id = model.get("name", "").split("/")[-1]
        if model_id:
            models_info.append((model_id, model.get("displayName", model_id)))
    return models_info


def generate_content_contents(ai_request):
    return [
        {"role": gemini_role(message.role), "parts": generate_content_parts(message.parts)}
        for message in ai_request.messages
        if message.parts
    ]


def gemini_role(role):
    if role == "assistant":
        return "model"
    return "user"


def generate_content_parts(parts):
    content_parts = []
    for part in parts:
        if part.kind == "text":
            content_parts.append({"text": part.text})
        elif part.kind in {"image", "audio"} and part.data:
            content_parts.append({"inline_data": {"mime_type": part.mime_type, "data": part.data}})
        elif part.kind == "file":
            file_part = file_content_part(part)
            if file_part:
                content_parts.append(file_part)
    return content_parts


def file_content_part(part):
    if part.file_uri:
        return {"file_data": {"mime_type": part.mime_type, "file_uri": part.file_uri}}
    if part.data:
        return {"inline_data": {"mime_type": part.mime_type, "data": part.data}}
    return None


def should_force_zero_temperature(ai_request):
    keywords = ("extract", "translate", "ocr", "transcribe")
    for message in ai_request.messages:
        for part in message.parts:
            if part.kind == "text" and any(keyword in part.text.lower() for keyword in keywords):
                return True
    return False
