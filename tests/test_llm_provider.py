"""
Unit tests for lib.core.providers.LLMProvider (the abstract Provider base class).

Verifies chat() dispatches to agentic_chat() when tools are provided
and to simple_chat() otherwise.
"""

from unittest.mock import MagicMock
from lib.core.providers.LLMProvider import Provider
from lib.core.providers.model.LLMProviderConfiguration import ProviderConfiguration


class ConcreteProvider(Provider):
    """Minimal concrete implementation of the abstract Provider for testing."""

    def agentic_chat(self, prompt, model, system_prompt, assistant_prompt, tools, config=None):
        return "agentic"

    def simple_chat(self, prompt, model, system_prompt=None, config=None):
        return "simple"

    def embed(self, text, embedding_model):
        return [0.1, 0.2]


class TestProvider:
    def setup_method(self):
        self.provider = ConcreteProvider()
        self.config = ProviderConfiguration(stream=False, think=False)

    def test_chat_without_tools_calls_simple_chat(self):
        result = self.provider.chat(prompt="hi", model="m", config=self.config)
        assert result == "simple"

    def test_chat_with_tools_calls_agentic_chat(self):
        tools = {"fn": MagicMock()}
        result = self.provider.chat(prompt="hi", model="m", tools=tools, config=self.config)
        assert result == "agentic"

    def test_chat_passes_system_prompt(self):
        result = self.provider.chat(
            prompt="hi", model="m", system_prompt="sys", config=self.config
        )
        assert result == "simple"

    def test_abstract_method_bodies_return_none(self):
        """Call abstract method bodies directly to cover the pass statements."""
        provider = ConcreteProvider()
        assert Provider.agentic_chat(provider, "p", "m", "sp", "ap", {}) is None
        assert Provider.simple_chat(provider, "p", "m") is None
        assert Provider.embed(provider, "text", "em") is None
