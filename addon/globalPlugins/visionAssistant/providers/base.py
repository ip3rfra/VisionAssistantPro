# -*- coding: utf-8 -*-
from dataclasses import dataclass, replace


@dataclass(frozen=True)
class ProviderCapabilities:
    chat: bool = True
    vision: bool = False
    file_upload: bool = False
    audio_transcription: bool = False
    tts: bool = False
    model_listing: bool = False
    json_mode: bool = False
    video_analysis: bool = False
    operator: bool = False


@dataclass(frozen=True)
class AiPart:
    kind: str
    text: str = ""
    mime_type: str = ""
    data: str = ""
    file_uri: str = ""
    file_id: str = ""
    file_url: str = ""
    download_url: str = ""
    file_name: str = ""
    file_size_bytes: int = 0


@dataclass(frozen=True)
class AiMessage:
    role: str
    parts: tuple


@dataclass(frozen=True)
class AiRequest:
    messages: tuple
    json_mode: bool = False


def normalize_ai_request(prompt, attachments=None, json_mode=False):
    if isinstance(prompt, str):
        parts = []
        if prompt:
            parts.append(AiPart(kind="text", text=prompt))
        parts.extend(attachment_to_part(att) for att in attachments or [])
        return AiRequest(messages=(AiMessage(role="user", parts=tuple(parts)),), json_mode=bool(json_mode))

    messages = []
    for message in prompt or []:
        if not isinstance(message, dict):
            continue
        normalized = normalize_message(message)
        if normalized.parts:
            messages.append(normalized)
    return AiRequest(messages=tuple(messages), json_mode=bool(json_mode))


def normalize_message(message):
    role = normalize_role(message.get("role", "user"))
    if "parts" in message:
        parts = tuple(
            part
            for part in (gemini_part_to_ai_part(item) for item in message.get("parts", []))
            if part is not None
        )
        return AiMessage(role=role, parts=parts)

    content = message.get("content", "")
    if isinstance(content, str):
        parts = (AiPart(kind="text", text=content),) if content else ()
    elif isinstance(content, list):
        parts = tuple(
            part
            for part in (openai_content_block_to_ai_part(item) for item in content)
            if part is not None
        )
    else:
        parts = ()
    return AiMessage(role=role, parts=parts)


def normalize_role(role):
    role = str(role or "user").strip().lower()
    if role == "model":
        return "assistant"
    if role in {"assistant", "system", "developer"}:
        return role
    return "user"


def attachment_to_part(attachment):
    mime_type = str(attachment.get("mime_type") or "").strip()
    data = attachment.get("data")
    file_url = str(attachment.get("file_url") or "").strip()
    download_url = str(attachment.get("download_url") or "").strip()
    file_uri = str(attachment.get("file_uri") or attachment.get("uri") or "").strip()
    file_id = str(attachment.get("file_id") or "").strip()
    file_name = str(attachment.get("file_name") or attachment.get("filename") or "").strip()
    file_size = attachment.get("file_size_bytes") or 0
    try:
        file_size = int(file_size)
    except (TypeError, ValueError):
        file_size = 0

    if mime_type.startswith("image/") and data:
        return AiPart(kind="image", mime_type=mime_type, data=str(data), file_name=file_name)
    if mime_type.startswith("audio/") and data:
        return AiPart(kind="audio", mime_type=mime_type, data=str(data), file_name=file_name)
    return AiPart(
        kind="file",
        mime_type=mime_type,
        data=str(data or ""),
        file_uri=file_uri,
        file_id=file_id,
        file_url=file_url,
        download_url=download_url,
        file_name=file_name,
        file_size_bytes=file_size,
    )


def gemini_part_to_ai_part(part):
    if not isinstance(part, dict):
        return None
    if "text" in part:
        return AiPart(kind="text", text=str(part.get("text") or ""))

    inline_data = part.get("inline_data") or part.get("inlineData")
    if isinstance(inline_data, dict):
        return attachment_to_part(
            {
                "mime_type": inline_data.get("mime_type") or inline_data.get("mimeType") or "",
                "data": inline_data.get("data") or "",
            }
        )

    file_data = part.get("file_data") or part.get("fileData")
    if isinstance(file_data, dict):
        return AiPart(
            kind="file",
            mime_type=str(file_data.get("mime_type") or file_data.get("mimeType") or ""),
            file_uri=str(file_data.get("file_uri") or file_data.get("fileUri") or ""),
        )
    return attachment_to_part(part)


def openai_content_block_to_ai_part(block):
    if not isinstance(block, dict):
        return None
    block_type = block.get("type")
    if block_type in {"text", "input_text", "output_text"}:
        return AiPart(kind="text", text=str(block.get("text") or ""))
    if block_type in {"image_url", "input_image"}:
        image_url = block.get("image_url", "")
        if isinstance(image_url, dict):
            image_url = image_url.get("url", "")
        return image_url_to_part(str(image_url or ""))
    if block_type in {"input_file", "file"}:
        return AiPart(
            kind="file",
            file_id=str(block.get("file_id") or ""),
            file_url=str(block.get("file_url") or ""),
            file_name=str(block.get("filename") or block.get("file_name") or ""),
        )
    return None


def image_url_to_part(image_url):
    prefix = "data:"
    marker = ";base64,"
    if image_url.startswith(prefix) and marker in image_url:
        mime_type, data = image_url[len(prefix):].split(marker, 1)
        return AiPart(kind="image", mime_type=mime_type, data=data)
    return AiPart(kind="image", file_url=image_url)


def request_has_mime_prefix(ai_request, mime_prefix):
    return first_part_with_mime_prefix(ai_request, mime_prefix) is not None


def request_has_part_kind(ai_request, kind):
    return first_part_with_kind(ai_request, kind) is not None


def first_part_with_mime_prefix(ai_request, mime_prefix):
    for message in ai_request.messages:
        for part in message.parts:
            if part.mime_type.startswith(mime_prefix):
                return part
    return None


def first_part_with_kind(ai_request, kind):
    for message in ai_request.messages:
        for part in message.parts:
            if part.kind == kind:
                return part
    return None


def ai_part_to_attachment(part):
    return {
        "mime_type": part.mime_type,
        "data": part.data,
        "file_name": part.file_name,
        "filename": part.file_name,
        "file_id": part.file_id,
        "file_url": part.file_url,
        "download_url": part.download_url,
        "file_uri": part.file_uri,
        "uri": part.file_uri,
        "file_size_bytes": part.file_size_bytes,
    }


def request_required_features(ai_request, task="chat"):
    features = ["chat"]
    if task == "operator":
        features.append("operator")
        return tuple(features)
    if request_has_mime_prefix(ai_request, "audio/"):
        features.append("audio_transcription")
    if request_has_mime_prefix(ai_request, "image/"):
        features.append("vision")
    if request_has_part_kind(ai_request, "file"):
        features.append("file_upload")
    return tuple(features)


def provider_supports_features(capabilities, features):
    return all(getattr(capabilities, feature, False) for feature in features)


def choose_provider_for_features(
    preferred_provider,
    features,
    capabilities_by_provider,
    configured_provider_ids,
    fallback_order,
):
    preferred_capabilities = capabilities_by_provider.get(preferred_provider)
    if preferred_capabilities and provider_supports_features(preferred_capabilities, features):
        return preferred_provider

    configured_provider_ids = set(configured_provider_ids or ())
    for provider in fallback_order:
        if provider == preferred_provider or provider not in configured_provider_ids:
            continue
        capabilities = capabilities_by_provider.get(provider)
        if capabilities and provider_supports_features(capabilities, features):
            return provider
    return None


def replace_part(ai_request, old_part, new_part):
    messages = []
    replaced = False
    for message in ai_request.messages:
        parts = []
        for part in message.parts:
            if not replaced and part == old_part:
                parts.append(new_part)
                replaced = True
            else:
                parts.append(part)
        messages.append(replace(message, parts=tuple(parts)))
    return replace(ai_request, messages=tuple(messages))
