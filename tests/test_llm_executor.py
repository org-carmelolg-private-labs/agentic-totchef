"""
Unit tests for lib.adapters.outbound.LLMExecutor.
"""

from unittest.mock import MagicMock, patch
import lib.adapters.outbound.LLMExecutor as executor


class TestLLMExecutor:
    def setup_method(self):
        self.mock_provider = MagicMock()

    def test_ask_calls_simple_chat(self):
        mock_response = MagicMock()
        self.mock_provider.chat.return_value = mock_response
        with patch.object(executor, "current_provider", self.mock_provider):
            result = executor.ask(prompt="hello")
        self.mock_provider.chat.assert_called_once()
        assert result is mock_response

    def test_ask_with_system_prompt(self):
        mock_response = MagicMock()
        self.mock_provider.chat.return_value = mock_response
        with patch.object(executor, "current_provider", self.mock_provider):
            result = executor.ask(prompt="hello", system_prompt="sys")
        assert result is mock_response

    def test_ask_disable_think(self):
        mock_response = MagicMock()
        self.mock_provider.chat.return_value = mock_response
        with patch.object(executor, "current_provider", self.mock_provider):
            with patch.object(executor, "think", True):
                result = executor.ask(prompt="hello", disable_think=True)
        # With disable_think=True the config should have think=False
        call_kwargs = self.mock_provider.chat.call_args[1]
        assert call_kwargs["config"].get_think() is False

    def test_ask_chatbot_mode(self):
        mock_response = MagicMock()
        self.mock_provider.chat.return_value = mock_response
        with patch.object(executor, "current_provider", self.mock_provider):
            result = executor.ask(prompt="hello", chatbot_mode=True)
        call_kwargs = self.mock_provider.chat.call_args[1]
        assert call_kwargs["config"].get_stream() is True

    def test_chat_no_tools(self):
        mock_response = MagicMock()
        self.mock_provider.chat.return_value = mock_response
        with patch.object(executor, "current_provider", self.mock_provider):
            result = executor.chat(prompt="hello")
        assert result is mock_response

    def test_chat_with_tools(self):
        mock_response = MagicMock()
        self.mock_provider.chat.return_value = mock_response
        tools = {"fn": MagicMock()}
        with patch.object(executor, "current_provider", self.mock_provider):
            result = executor.chat(prompt="hello", tools=tools)
        call_kwargs = self.mock_provider.chat.call_args[1]
        assert "fn" in call_kwargs["tools"]

    def test_chat_disable_think(self):
        mock_response = MagicMock()
        self.mock_provider.chat.return_value = mock_response
        with patch.object(executor, "current_provider", self.mock_provider):
            with patch.object(executor, "think", True):
                result = executor.chat(prompt="hello", disable_think=True)
        call_kwargs = self.mock_provider.chat.call_args[1]
        assert call_kwargs["config"].get_think() is False
