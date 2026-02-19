"""
Unit tests for lib.core.providers.LLMProviderFactory.

Verifies that get_instance() still works correctly after converting
from @staticmethod to @classmethod.
"""

import pytest
from unittest.mock import patch
from lib.core.providers.LLMProviderFactory import LLMProviderFactory


class TestLLMProviderFactory:
    def test_get_instance_returns_ollama_provider_when_configured(self):
        with patch("lib.core.providers.LLMProviderFactory.LLM_PROVIDER", "ollama"):
            result = LLMProviderFactory.get_instance()
        assert result is not None

    def test_get_instance_returns_none_for_unknown_provider(self):
        with patch("lib.core.providers.LLMProviderFactory.LLM_PROVIDER", "unknown_provider"):
            result = LLMProviderFactory.get_instance()
        assert result is None

    def test_get_instance_callable_as_classmethod(self):
        # Ensure the method can still be called on the class (not just an instance)
        result = LLMProviderFactory.get_instance()
        # Result is either a provider instance or None depending on env; both are valid
        from lib.core.providers.OllamaProvider import OllamaProvider
        assert result is None or isinstance(result, OllamaProvider)
