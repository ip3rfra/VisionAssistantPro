import importlib
import json
import tempfile
import sys
import types
import unittest
from pathlib import Path
from types import SimpleNamespace


PACKAGE_DIR = Path(__file__).resolve().parents[1] / "addon" / "globalPlugins" / "visionAssistant"
if "visionAssistant" not in sys.modules:
    package = types.ModuleType("visionAssistant")
    package.__path__ = [str(PACKAGE_DIR)]
    sys.modules["visionAssistant"] = package


base = importlib.import_module("visionAssistant.providers.base")
custom = importlib.import_module("visionAssistant.providers.custom")
gemini = importlib.import_module("visionAssistant.providers.gemini")
groq = importlib.import_module("visionAssistant.providers.groq")
mistral = importlib.import_module("visionAssistant.providers.mistral")
openai_api = importlib.import_module("visionAssistant.providers.openai_api")


class FakeResponse:
    def __init__(self, body, headers=None):
        self._body = body.encode("utf-8") if isinstance(body, str) else body
        self.headers = headers or {}

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, traceback):
        return False

    def read(self):
        return self._body


class FakeOpener:
    def __init__(self, response):
        self.response = response
        self.request = None
        self.timeout = None

    def open(self, request, timeout=None):
        self.request = request
        self.timeout = timeout
        return self.response


class ProviderAdapterTests(unittest.TestCase):
    def test_normalizes_gemini_style_messages_to_internal_request(self):
        request = base.normalize_ai_request(
            [
                {"role": "model", "parts": [{"text": "Previous answer"}]},
                {
                    "role": "user",
                    "parts": [
                        {"text": "Follow up"},
                        {"inline_data": {"mime_type": "image/png", "data": "img-data"}},
                    ],
                },
            ]
        )

        self.assertEqual(request.messages[0].role, "assistant")
        self.assertEqual(request.messages[0].parts[0].kind, "text")
        self.assertEqual(request.messages[0].parts[0].text, "Previous answer")
        self.assertEqual(request.messages[1].parts[1].kind, "image")
        self.assertEqual(request.messages[1].parts[1].mime_type, "image/png")
        self.assertTrue(base.request_has_mime_prefix(request, "image/"))

    def test_openai_api_adapter_builds_chat_completions_messages(self):
        request = base.normalize_ai_request(
            "Describe this",
            attachments=[{"mime_type": "image/jpeg", "data": "abc123"}],
        )

        payload = openai_api.build_chat_completions_payload(
            model="gpt-4.1",
            ai_request=request,
            temperature=0.2,
            json_mode=True,
        )

        self.assertEqual(payload["model"], "gpt-4.1")
        self.assertEqual(payload["temperature"], 0.2)
        self.assertEqual(payload["response_format"], {"type": "json_object"})
        content = payload["messages"][0]["content"]
        self.assertEqual(content[0], {"type": "text", "text": "Describe this"})
        self.assertEqual(
            content[1],
            {"type": "image_url", "image_url": {"url": "data:image/jpeg;base64,abc123"}},
        )

    def test_openai_api_adapter_uses_string_content_for_text_only_messages(self):
        request = base.normalize_ai_request(
            [
                {"role": "user", "content": "Hello"},
                {"role": "assistant", "content": "Hi"},
            ]
        )

        payload = openai_api.build_chat_completions_payload(
            model="gpt-4.1",
            ai_request=request,
        )

        self.assertEqual(payload["messages"][0]["content"], "Hello")
        self.assertEqual(payload["messages"][1]["content"], "Hi")

    def test_provider_capabilities_advertise_task_support(self):
        self.assertTrue(gemini.CAPABILITIES.tts)
        self.assertTrue(gemini.CAPABILITIES.video_analysis)
        self.assertTrue(openai_api.CAPABILITIES.tts)
        self.assertTrue(openai_api.CAPABILITIES.audio_transcription)
        self.assertFalse(groq.CAPABILITIES.tts)
        self.assertFalse(mistral.CAPABILITIES.tts)
        self.assertTrue(custom.capabilities_for("gemini", file_upload=True).file_upload)
        self.assertFalse(custom.capabilities_for("openai", file_upload=False).file_upload)

    def test_gemini_adapter_builds_generate_content_payload(self):
        request = base.normalize_ai_request(
            [
                {"role": "model", "parts": [{"text": "Previous answer"}]},
                {
                    "role": "user",
                    "parts": [
                        {"text": "Analyze"},
                        {"inline_data": {"mime_type": "image/png", "data": "img-data"}},
                        {"file_data": {"mime_type": "application/pdf", "file_uri": "gemini://file/1"}},
                    ],
                },
            ],
            json_mode=True,
        )

        payload = gemini.build_generate_content_payload(request, temperature=0.3)

        self.assertEqual(payload["generationConfig"]["temperature"], 0.3)
        self.assertEqual(payload["generationConfig"]["response_mime_type"], "application/json")
        self.assertEqual(payload["contents"][0]["role"], "model")
        self.assertEqual(payload["contents"][0]["parts"], [{"text": "Previous answer"}])
        self.assertEqual(payload["contents"][1]["role"], "user")
        self.assertEqual(payload["contents"][1]["parts"][0], {"text": "Analyze"})
        self.assertEqual(
            payload["contents"][1]["parts"][1],
            {"inline_data": {"mime_type": "image/png", "data": "img-data"}},
        )
        self.assertEqual(
            payload["contents"][1]["parts"][2],
            {"file_data": {"mime_type": "application/pdf", "file_uri": "gemini://file/1"}},
        )

    def test_mistral_adapter_builds_native_ocr_payload(self):
        payload = mistral.build_ocr_payload("pdf-data", "application/pdf")

        self.assertEqual(payload["model"], "mistral-ocr-latest")
        self.assertEqual(payload["document"]["type"], "document_url")
        self.assertEqual(payload["document"]["document_url"], "data:application/pdf;base64,pdf-data")

    def test_openai_api_adapter_builds_audio_transcription_and_speech_payloads(self):
        body, content_type = openai_api.build_transcription_multipart(
            {"mime_type": "audio/wav", "data": "YWJj"},
            model_name="whisper-1",
            boundary="Boundary-test",
        )

        self.assertEqual(content_type, "multipart/form-data; boundary=Boundary-test")
        self.assertIn(b'name="file"; filename="audio.wav"', body)
        self.assertIn(b"Content-Type: audio/wav", body)
        self.assertIn(b"name=\"model\"", body)
        self.assertIn(b"whisper-1", body)

        payload = openai_api.build_speech_payload("tts-1", "Hello", "Nova")

        self.assertEqual(
            payload,
            {"model": "tts-1", "input": "Hello", "voice": "nova", "response_format": "mp3"},
        )

    def test_openai_api_send_chat_completions_request_posts_json(self):
        opener = FakeOpener(FakeResponse('{"choices": [{"message": {"content": "done"}}]}'))

        result = openai_api.send_chat_completions_request(
            opener,
            "https://api.test/v1/chat/completions",
            "key-123",
            {"model": "gpt-test", "messages": []},
        )

        self.assertEqual(result, "done")
        self.assertEqual(opener.request.full_url, "https://api.test/v1/chat/completions")
        self.assertEqual(opener.request.get_header("Authorization"), "Bearer key-123")
        self.assertEqual(json.loads(opener.request.data.decode("utf-8"))["model"], "gpt-test")

    def test_openai_api_send_transcription_request_posts_multipart(self):
        opener = FakeOpener(FakeResponse('{"text": "hello"}'))

        result = openai_api.send_transcription_request(
            opener,
            "https://api.test/v1/audio/transcriptions",
            "key-123",
            {"mime_type": "audio/wav", "data": "YWJj"},
            "whisper-1",
            "Boundary-test",
        )

        self.assertEqual(result, "hello")
        self.assertIn(b'name="file"; filename="audio.wav"', opener.request.data)
        self.assertIn(b"whisper-1", opener.request.data)
        self.assertIn("multipart/form-data", opener.request.get_header("Content-type"))

    def test_openai_api_send_speech_request_returns_base64_audio(self):
        opener = FakeOpener(FakeResponse(b"mp3-data"))

        result = openai_api.send_speech_request(
            opener,
            "https://api.test/v1/audio/speech",
            "key-123",
            {"model": "tts-1", "input": "Hello"},
        )

        self.assertEqual(result, "bXAzLWRhdGE=")
        self.assertEqual(json.loads(opener.request.data.decode("utf-8"))["model"], "tts-1")

    def test_gemini_send_generate_content_request_posts_key_header(self):
        opener = FakeOpener(FakeResponse('{"candidates": [{"content": {"parts": [{"text": "ok"}]}}]}'))

        result = gemini.send_generate_content_request(
            opener,
            "https://gemini.test/v1beta/models/model:generateContent",
            "gemini-key",
            {"contents": []},
        )

        self.assertEqual(result["candidates"][0]["content"]["parts"][0]["text"], "ok")
        self.assertEqual(opener.request.get_header("X-goog-api-key"), "gemini-key")
        self.assertEqual(json.loads(opener.request.data.decode("utf-8")), {"contents": []})

    def test_mistral_send_ocr_request_joins_page_markdown(self):
        opener = FakeOpener(FakeResponse('{"pages": [{"markdown": "one"}, {"markdown": "two"}]}'))

        result = mistral.send_ocr_request(
            opener,
            "https://mistral.test/v1/ocr",
            "key-123",
            {"model": "mistral-ocr-latest"},
        )

        self.assertEqual(result, "one\n\ntwo")
        self.assertEqual(opener.request.get_header("Authorization"), "Bearer key-123")

    def test_fallback_selection_chooses_configured_provider_with_required_features(self):
        capabilities = {
            "groq": groq.CAPABILITIES,
            "openai": openai_api.CAPABILITIES,
            "gemini": gemini.CAPABILITIES,
        }

        provider = base.choose_provider_for_features(
            preferred_provider="groq",
            features=("tts",),
            capabilities_by_provider=capabilities,
            configured_provider_ids={"gemini"},
            fallback_order=("openai", "gemini"),
        )

        self.assertEqual(provider, "gemini")

    def test_fallback_selection_returns_preferred_when_it_supports_features(self):
        provider = base.choose_provider_for_features(
            preferred_provider="gemini",
            features=("vision", "file_upload"),
            capabilities_by_provider={"gemini": gemini.CAPABILITIES},
            configured_provider_ids=set(),
            fallback_order=("gemini",),
        )

        self.assertEqual(provider, "gemini")

    def test_request_required_features_reports_file_upload_need(self):
        request = base.normalize_ai_request(
            "Read",
            attachments=[{"mime_type": "application/pdf", "data": "pdf-data"}],
        )

        self.assertEqual(base.request_required_features(request), ("chat", "file_upload"))

    def test_registry_auto_fallback_uses_task_order_and_configured_providers(self):
        registry = importlib.import_module("visionAssistant.providers.registry")

        provider = registry.resolve_provider_for_features(
            preferred_provider="groq",
            features=("tts",),
            configured_provider_ids={"gemini", "openai"},
            fallback_config={"fallback_tts_provider": registry.FALLBACK_PROVIDER_AUTO},
        )

        self.assertEqual(provider, "gemini")

    def test_registry_explicit_fallback_is_strict(self):
        registry = importlib.import_module("visionAssistant.providers.registry")

        provider = registry.resolve_provider_for_features(
            preferred_provider="groq",
            features=("tts",),
            configured_provider_ids={"gemini", "openai"},
            fallback_config={"fallback_tts_provider": "openai"},
        )

        self.assertEqual(provider, "openai")

    def test_registry_returns_none_for_explicit_unconfigured_fallback(self):
        registry = importlib.import_module("visionAssistant.providers.registry")

        provider = registry.resolve_provider_for_features(
            preferred_provider="groq",
            features=("tts",),
            configured_provider_ids={"gemini"},
            fallback_config={"fallback_tts_provider": "openai"},
        )

        self.assertIsNone(provider)

    def test_registry_returns_none_for_explicit_unsupported_fallback(self):
        registry = importlib.import_module("visionAssistant.providers.registry")

        provider = registry.resolve_provider_for_features(
            preferred_provider="groq",
            features=("tts",),
            configured_provider_ids={"groq"},
            fallback_config={"fallback_tts_provider": "groq"},
        )

        self.assertIsNone(provider)

    def test_registry_reports_provider_feature_statuses_for_ui(self):
        registry = importlib.import_module("visionAssistant.providers.registry")

        statuses = registry.provider_feature_statuses(
            "tts",
            configured_provider_ids={"openai"},
            custom_api_type="openai",
            custom_upload_support=False,
        )
        by_provider = {status.provider_id: status for status in statuses}

        self.assertTrue(by_provider["openai"].supports)
        self.assertTrue(by_provider["openai"].configured)
        self.assertTrue(by_provider["openai"].available)
        self.assertFalse(by_provider["gemini"].configured)

    def test_registry_builds_adapter_from_module_metadata(self):
        registry = importlib.import_module("visionAssistant.providers.registry")
        module = SimpleNamespace(
            PROVIDER_ID="example",
            DISPLAY_NAME="Example AI",
            ORDER=55,
            CAPABILITIES=base.ProviderCapabilities(chat=True, tts=True),
        )

        adapter = registry.adapter_from_module("visionAssistant.providers.example", module)

        self.assertEqual(adapter.provider_id, "example")
        self.assertEqual(adapter.display_name, "Example AI")
        self.assertEqual(adapter.module_name, "visionAssistant.providers.example")
        self.assertEqual(adapter.order, 55)
        self.assertTrue(adapter.capabilities.tts)

    def test_registry_discovers_provider_modules_from_metadata(self):
        registry = importlib.import_module("visionAssistant.providers.registry")

        adapters = registry.discover_provider_adapters()

        self.assertIn("gemini", adapters)
        self.assertIn("custom", adapters)
        self.assertNotIn("base", adapters)
        self.assertEqual(adapters["gemini"].module_name.rsplit(".", 1)[-1], "gemini")

    def test_registry_provider_choices_use_discovered_stable_order(self):
        registry = importlib.import_module("visionAssistant.providers.registry")

        choices = registry.provider_choices()

        self.assertEqual([provider_id for _, provider_id in choices], [
            "gemini",
            "openai",
            "mistral",
            "groq",
            "custom",
        ])

    def test_registry_respects_explicit_empty_adapter_map(self):
        registry = importlib.import_module("visionAssistant.providers.registry")

        self.assertEqual(registry.provider_choices(adapters={}), ())
        self.assertEqual(registry.fallback_order_for_features(("tts",), adapters={}), ())
        self.assertEqual(registry.provider_feature_statuses("tts", configured_provider_ids=set(), adapters={}), ())

    def test_registry_skips_broken_adapter_modules_during_discovery(self):
        registry = importlib.import_module("visionAssistant.providers.registry")
        package_name = "fakeproviders_registry_test"
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            package_dir = tmp_path / package_name
            package_dir.mkdir()
            (package_dir / "__init__.py").write_text("", encoding="utf-8")
            (package_dir / "broken.py").write_text("raise RuntimeError('boom')\n", encoding="utf-8")
            (package_dir / "good.py").write_text(
                "\n".join(
                    [
                        "from visionAssistant.providers.base import ProviderCapabilities",
                        "PROVIDER_ID = 'good'",
                        "DISPLAY_NAME = 'Good'",
                        "ORDER = 1",
                        "CAPABILITIES = ProviderCapabilities(chat=True, tts=True)",
                    ]
                ),
                encoding="utf-8",
            )

            sys.path.insert(0, str(tmp_path))
            importlib.invalidate_caches()
            try:
                with self.assertLogs(registry.log, level="ERROR") as captured:
                    adapters = registry.discover_provider_adapters(
                        package_name=package_name,
                        search_paths=[str(package_dir)],
                    )
            finally:
                sys.path.remove(str(tmp_path))
                for name in list(sys.modules):
                    if name == package_name or name.startswith(f"{package_name}."):
                        del sys.modules[name]

        self.assertEqual(tuple(adapters.keys()), ("good",))
        self.assertIn("Skipping provider adapter module", captured.output[0])

    def test_registry_feature_fallback_appends_discovered_providers(self):
        registry = importlib.import_module("visionAssistant.providers.registry")
        adapters = {
            "groq": registry.PROVIDER_ADAPTERS["groq"],
            "localai": registry.ProviderAdapter(
                provider_id="localai",
                display_name="LocalAI",
                module_name="visionAssistant.providers.localai",
                module=SimpleNamespace(CAPABILITIES=base.ProviderCapabilities(chat=True, tts=True)),
                capabilities=base.ProviderCapabilities(chat=True, tts=True),
                order=99,
            ),
        }

        provider = registry.resolve_provider_for_features(
            preferred_provider="groq",
            features=("tts",),
            configured_provider_ids={"localai"},
            fallback_config={"fallback_tts_provider": registry.FALLBACK_PROVIDER_AUTO},
            adapters=adapters,
        )

        self.assertEqual(provider, "localai")

    def test_runtime_uses_provider_adapters_instead_of_local_openai_conversion(self):
        source = (PACKAGE_DIR / "__init__.py").read_text(encoding="utf-8")

        self.assertIn("build_chat_completions_payload(", source)
        self.assertIn("build_gemini_generate_content_payload(", source)
        self.assertIn("build_mistral_ocr_payload(", source)

    def test_runtime_delegates_provider_http_calls_to_adapters(self):
        source = (PACKAGE_DIR / "__init__.py").read_text(encoding="utf-8")

        self.assertIn("send_chat_completions_request(", source)
        self.assertIn("send_transcription_request(", source)
        self.assertIn("send_speech_request(", source)
        self.assertIn("send_generate_content_request(", source)
        self.assertIn("parse_models_response(", source)
        self.assertNotIn("with get_proxy_opener().open(req, timeout=180) as r:", source)
        self.assertNotIn("with get_proxy_opener().open(req, timeout=60) as r:", source)

    def test_runtime_exposes_capabilities_for_feature_routing(self):
        source = (PACKAGE_DIR / "__init__.py").read_text(encoding="utf-8")

        self.assertIn("provider_choices(", source)
        self.assertNotIn("PROVIDER_CHOICES = (", source)
        self.assertIn("def capabilities_for", source)
        self.assertIn("def resolve_provider_for_features", source)
        self.assertIn("def _call_with_active_provider", source)
        self.assertIn("registry_resolve_provider_for_features(", source)
        self.assertIn('AIHandler.resolve_provider_for_features(("tts",), preferred_provider=provider)', source)

    def test_runtime_exposes_configurable_fallback_provider_settings(self):
        source = (PACKAGE_DIR / "__init__.py").read_text(encoding="utf-8")

        for key in (
            "fallback_vision_provider",
            "fallback_file_upload_provider",
            "fallback_audio_provider",
            "fallback_tts_provider",
            "fallback_video_provider",
        ):
            self.assertIn(f'"{key}": "string(default=\'auto\')"', source)
            self.assertIn(f'config.conf["VisionAssistant"]["{key}"]', source)

        self.assertIn('groupLabel = _("Fallback Providers")', source)
        self.assertIn('label=_("Image analysis:")', source)
        self.assertIn('label=_("Files and documents:")', source)
        self.assertIn('label=_("Audio transcription:")', source)
        self.assertIn('label=_("Text-to-speech:")', source)
        self.assertIn('label=_("Video analysis:")', source)
        self.assertIn("provider_feature_statuses(", source)
        self.assertIn("def validateFallbackProviderChoices", source)
        self.assertIn("Fallback provider unavailable", source)
        self.assertIn("self.validateFallbackProviderChoices()", source)

    def test_runtime_announces_provider_fallback(self):
        source = (PACKAGE_DIR / "__init__.py").read_text(encoding="utf-8")

        self.assertIn("def fallback_provider_for_features", source)
        self.assertIn("def _announce_provider_fallback", source)
        self.assertIn('message = _("Using {provider} for {features}.")', source)
        self.assertIn("AIHandler._announce_provider_fallback(", source)


if __name__ == "__main__":
    unittest.main()
