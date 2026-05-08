# -*- coding: utf-8 -*-
import base64
import json
from urllib import request

from .base import ProviderCapabilities


PROVIDER_ID = "openai"
DISPLAY_NAME = "OpenAI"
ORDER = 20
API_STYLE = "openai"
BASE_URL = "https://api.openai.com"

CAPABILITIES = ProviderCapabilities(
    chat=True,
    vision=True,
    file_upload=False,
    audio_transcription=True,
    tts=True,
    model_listing=True,
    json_mode=True,
)


def build_chat_completions_payload(model, ai_request, temperature=0.7, json_mode=False):
    payload = {
        "model": model,
        "messages": chat_completions_messages(ai_request),
        "temperature": temperature,
    }
    if json_mode or ai_request.json_mode:
        payload["response_format"] = {"type": "json_object"}
    return payload


def build_transcription_multipart(audio_attachment, model_name, boundary):
    body = [
        f"--{boundary}".encode(),
        b'Content-Disposition: form-data; name="file"; filename="audio.wav"',
        f"Content-Type: {audio_attachment['mime_type']}".encode(),
        b"",
        base64.b64decode(audio_attachment["data"]),
        f"--{boundary}".encode(),
        b'Content-Disposition: form-data; name="model"',
        b"",
        model_name.encode(),
        f"--{boundary}--".encode(),
        b"",
    ]
    return b"\r\n".join(body), f"multipart/form-data; boundary={boundary}"


def build_speech_payload(model, text, voice_name, response_format="mp3"):
    return {
        "model": model,
        "input": text,
        "voice": voice_name.lower(),
        "response_format": response_format,
    }


def build_json_headers(key=None):
    headers = {"Content-Type": "application/json", "User-Agent": "Mozilla/5.0"}
    if key and key.strip():
        headers["Authorization"] = f"Bearer {key}"
    return headers


def send_chat_completions_request(opener, url, key, payload, timeout=180):
    req = request.Request(url, data=json.dumps(payload).encode(), headers=build_json_headers(key))
    with opener.open(req, timeout=timeout) as response:
        res = json.loads(response.read().decode())
    return res["choices"][0]["message"]["content"]


def send_transcription_request(opener, url, key, audio_attachment, model_name, boundary, timeout=60):
    body, content_type = build_transcription_multipart(audio_attachment, model_name, boundary)
    headers = {"Content-Type": content_type, "User-Agent": "Mozilla/5.0"}
    if key and key.strip():
        headers["Authorization"] = f"Bearer {key}"
    req = request.Request(url, data=body, headers=headers)
    with opener.open(req, timeout=timeout) as response:
        return json.loads(response.read().decode())["text"]


def send_speech_request(opener, url, key, payload, timeout=120):
    req = request.Request(url, data=json.dumps(payload).encode(), headers=build_json_headers(key))
    with opener.open(req, timeout=timeout) as response:
        return base64.b64encode(response.read()).decode("utf-8")


def parse_models_response(data):
    return [
        (model_id, model_id)
        for model_id in (model.get("id") for model in data.get("data", []))
        if model_id
    ]


def chat_completions_messages(ai_request):
    return [
        {"role": message.role, "content": chat_completions_content(message)}
        for message in ai_request.messages
    ]


def chat_completions_content(message):
    blocks = []
    text_only = True
    for part in message.parts:
        if part.kind == "text":
            blocks.append({"type": "text", "text": part.text})
        elif part.kind == "image":
            image_url = part.file_url or f"data:{part.mime_type};base64,{part.data}"
            blocks.append({"type": "image_url", "image_url": {"url": image_url}})
            text_only = False

    if text_only:
        return "\n".join(block["text"] for block in blocks if block["type"] == "text")
    return blocks
