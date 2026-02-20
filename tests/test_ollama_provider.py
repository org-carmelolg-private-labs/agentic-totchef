"""
Unit tests for lib.core.providers.OllamaProvider.

Verifies that the singleton pattern still works correctly after converting
get_instance() from @staticmethod to @classmethod, and covers agentic_chat,
simple_chat, and embed.
"""

import pytest
from unittest.mock import patch, MagicMock
from lib.core.providers.OllamaProvider import OllamaProvider
from lib.core.providers.model.LLMProviderConfiguration import ProviderConfiguration


class TestOllamaProvider:
    def test_get_instance_returns_same_instance(self):
        instance1 = OllamaProvider.get_instance()
        instance2 = OllamaProvider.get_instance()
        assert instance1 is instance2
        assert isinstance(instance1, OllamaProvider)

    def test_singleton_raises_on_second_direct_instantiation(self):
        """Second direct call to __init__ must raise because the singleton already exists."""
        with pytest.raises(Exception, match="singleton"):
            OllamaProvider()



    def test_simple_chat_without_system_prompt(self):
        provider = OllamaProvider.get_instance()
        config = ProviderConfiguration(stream=False, think=False)
        mock_response = MagicMock()
        with patch("lib.core.providers.OllamaProvider.OllamaClient.chat", return_value=mock_response) as mock_chat:
            result = provider.simple_chat(prompt="hello", model="m", config=config)
        assert result is mock_response
        mock_chat.assert_called_once()
        call_kwargs = mock_chat.call_args[1]
        messages = call_kwargs["messages"]
        assert messages[0] == {"role": "user", "content": "hello"}

    def test_simple_chat_with_system_prompt(self):
        provider = OllamaProvider.get_instance()
        config = ProviderConfiguration(stream=False, think=False)
        mock_response = MagicMock()
        with patch("lib.core.providers.OllamaProvider.OllamaClient.chat", return_value=mock_response):
            result = provider.simple_chat(
                prompt="hello", model="m", system_prompt="sys", config=config
            )
        assert result is mock_response

    # ----- agentic_chat -----

    def _make_agentic_response(self, tool_name=None):
        response = MagicMock()
        if tool_name:
            tool_call = MagicMock()
            tool_call.function.name = tool_name
            tool_call.function.arguments = {}
            response.message.tool_calls = [tool_call]
        else:
            response.message.tool_calls = None
        return response

    def test_agentic_chat_no_tool_calls(self):
        provider = OllamaProvider.get_instance()
        config = ProviderConfiguration(stream=False, think=False)
        first_response = self._make_agentic_response()
        final_response = MagicMock()
        with patch(
            "lib.core.providers.OllamaProvider.OllamaClient.chat",
            side_effect=[first_response, final_response],
        ):
            result = provider.agentic_chat(
                prompt="hi",
                model="m",
                system_prompt="sys",
                assistant_prompt=None,
                tools={},
                config=config,
            )
        assert result is final_response

    def test_agentic_chat_with_tool_calls(self):
        provider = OllamaProvider.get_instance()
        config = ProviderConfiguration(stream=False, think=True)
        tool_fn = MagicMock(return_value="tool_result")
        first_response = self._make_agentic_response(tool_name="my_tool")
        final_response = MagicMock()
        with patch(
            "lib.core.providers.OllamaProvider.OllamaClient.chat",
            side_effect=[first_response, final_response],
        ):
            result = provider.agentic_chat(
                prompt="hi",
                model="m",
                system_prompt=None,
                assistant_prompt="asst",
                tools={"my_tool": tool_fn},
                config=config,
            )
        tool_fn.assert_called_once()
        assert result is final_response

    def test_agentic_chat_with_unknown_tool(self, capsys):
        provider = OllamaProvider.get_instance()
        config = ProviderConfiguration(stream=False, think=False)
        first_response = self._make_agentic_response(tool_name="unknown_tool")
        final_response = MagicMock()
        with patch(
            "lib.core.providers.OllamaProvider.OllamaClient.chat",
            side_effect=[first_response, final_response],
        ):
            result = provider.agentic_chat(
                prompt="hi",
                model="m",
                system_prompt=None,
                assistant_prompt=None,
                tools={},
                config=config,
            )
        captured = capsys.readouterr()
        assert "No tool available" in captured.out
        assert result is final_response

    # ----- embed -----

    def test_embed_returns_vector(self):
        provider = OllamaProvider.get_instance()
        mock_embeddings = {"embeddings": [[0.1, 0.2, 0.3]]}
        with patch(
            "lib.core.providers.OllamaProvider.OllamaClient.embed",
            return_value=mock_embeddings,
        ):
            result = provider.embed(text="hello", embedding_model="em")
        assert result == [0.1, 0.2, 0.3]
