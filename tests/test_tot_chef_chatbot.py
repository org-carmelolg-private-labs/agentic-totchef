"""
Unit tests for lib.use_case.runner.TotChefChatbot.
"""

import asyncio
from unittest.mock import patch, MagicMock, AsyncMock

from lib.use_case.runner.TotChefChatbot import TotChefChatbot


class TestTotChefChatbot:
    def test_init_sets_tools(self):
        chatbot = TotChefChatbot()
        assert "get_kindergarten_menu" in chatbot.tools
        assert "get_home_kitchen_recipes" in chatbot.tools
        assert "get_home_kitchen_recipes_by_category" in chatbot.tools

    def test_chat_calls_chat_func(self):
        chatbot = TotChefChatbot()
        mock_response = MagicMock()
        chatbot.chat_func = MagicMock(return_value=mock_response)
        result = chatbot._chat("hello there")
        chatbot.chat_func.assert_called_once_with(prompt="hello there", tools=chatbot.tools)
        assert result is mock_response

    def test_run_exits_on_quit(self):
        chatbot = TotChefChatbot()
        chatbot.chat_func = MagicMock()
        with patch("builtins.input", side_effect=["quit"]), \
             patch("builtins.print"):
            chatbot.run()  # should not block

    def test_run_exits_on_exit(self):
        chatbot = TotChefChatbot()
        chatbot.chat_func = MagicMock()
        with patch("builtins.input", side_effect=["exit"]), \
             patch("builtins.print"):
            chatbot.run()

    def test_run_handles_user_message(self):
        chatbot = TotChefChatbot()
        stream = [{"message": {"content": "hi"}}, {"message": {"content": "!"}}]
        chatbot.chat_func = MagicMock(return_value=stream)
        with patch("builtins.input", side_effect=["hello", "exit"]), \
             patch("builtins.print"):
            chatbot.run()
        chatbot.chat_func.assert_called_once()

    def test_gui_calls_ui_run(self):
        chatbot = TotChefChatbot()
        with patch("lib.use_case.runner.TotChefChatbot.ui") as mock_ui:
            chatbot.gui()
            mock_ui.run.assert_called_once()

    def test_root_executes_without_error(self):
        """
        Calls _root() with NiceGUI ui fully mocked so no server is started.
        Also retrieves and invokes the `send` coroutine to cover async lines.
        """
        chatbot = TotChefChatbot()

        # --- Build a mock ecosystem for NiceGUI ---
        # Most UI builders need to support chaining (.classes(), .props(), .style(), .on())
        # and context manager protocol.

        def chainable_mock():
            m = MagicMock()
            m.__enter__ = MagicMock(return_value=m)
            m.__exit__ = MagicMock(return_value=False)
            m.classes.return_value = m
            m.props.return_value = m
            m.style.return_value = m
            m.on.return_value = m
            m.clear.return_value = m
            return m

        text_mock = chainable_mock()
        text_mock.value = "my question"

        send_holder = {}

        def capture_on(event, callback):
            if event == "keydown.enter":
                send_holder["send"] = callback
            return text_mock

        text_mock.on = capture_on

        column_mock = chainable_mock()
        footer_mock = chainable_mock()
        row_mock = chainable_mock()
        element_mock = chainable_mock()
        button_mock = chainable_mock()
        chat_msg_mock = chainable_mock()
        spinner_mock = chainable_mock()
        html_mock = chainable_mock()
        markdown_mock = chainable_mock()

        stream_chunk = {"message": {"content": "response text"}}
        chatbot.chat_func = MagicMock(return_value=iter([stream_chunk]))

        with patch("lib.use_case.runner.TotChefChatbot.ui") as mock_ui:
            mock_ui.add_head_html = MagicMock()
            mock_ui.element.return_value = element_mock
            mock_ui.html.return_value = html_mock
            mock_ui.column.return_value = column_mock
            mock_ui.footer.return_value = footer_mock
            mock_ui.row.return_value = row_mock
            mock_ui.input.return_value = text_mock
            mock_ui.button.return_value = button_mock
            mock_ui.chat_message.return_value = chat_msg_mock
            mock_ui.spinner.return_value = spinner_mock
            mock_ui.markdown.return_value = markdown_mock
            mock_ui.run_javascript = AsyncMock()

            chatbot._root()

            # Now exercise the captured async `send` callback
            assert "send" in send_holder, "send callback was not captured"
            send_fn = send_holder["send"]

            # Provide fresh chunk iterator for the send call
            chatbot.chat_func = MagicMock(return_value=iter([stream_chunk]))
            asyncio.run(send_fn())
