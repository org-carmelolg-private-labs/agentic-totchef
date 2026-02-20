"""
Unit tests for lib.use_case.prompts (FilePromptManager, PromptManager,
HomeMenuPrompt, KindergartenMenuPrompt, MergeMenuPrompt, ShoppingListPrompt).
"""

import pytest
from unittest.mock import patch, mock_open

from lib.use_case.prompts.FilePromptManager import FilePromptManager
from lib.use_case.prompts.HomeMenuPrompt import GenerateHomeMenuPrompt
from lib.use_case.prompts.KindergartenMenuPrompt import GetKindergartenMenuPrompt
from lib.use_case.prompts.MergeMenuPrompt import MergeMenuPrompt
from lib.use_case.prompts.ShoppingListPrompt import ShoppingListPrompt


class ConcreteFilePromptManager(FilePromptManager):
    """Minimal concrete subclass to test FilePromptManager without a real file."""
    def get_system_prompt(self, *args, **kwargs):
        return super().get_system_prompt(*args, **kwargs)

    def get_user_prompt(self, *args, **kwargs):
        return super().get_user_prompt(*args, **kwargs)


class TestFilePromptManager:
    def test_load_prompt_with_valid_path(self):
        with patch("builtins.open", mock_open(read_data="system content")):
            with patch("builtins.open", mock_open(read_data="user content")):
                mgr = ConcreteFilePromptManager(
                    system_prompt_path="sys.prompt",
                    user_prompt_path="usr.prompt",
                )
        # The last mock wins; just verify the object was created
        assert mgr is not None

    def test_load_prompt_with_none_path(self):
        # None path should return empty string without file open
        with patch("builtins.open", mock_open(read_data="user {name}")) as m:
            mgr = ConcreteFilePromptManager(
                system_prompt_path=None,
                user_prompt_path="usr.prompt",
            )
        assert mgr.system_prompt_template == ""

    def test_load_prompt_with_empty_path(self):
        with patch("builtins.open", mock_open(read_data="user content")) as m:
            mgr = ConcreteFilePromptManager(
                system_prompt_path="",
                user_prompt_path="usr.prompt",
            )
        assert mgr.system_prompt_template == ""

    def test_get_system_prompt_formats(self):
        with patch("builtins.open", mock_open(read_data="Hello {name}!")):
            mgr = ConcreteFilePromptManager("sys.prompt", "usr.prompt")
        # Both templates will be "Hello {name}!" due to mock_open behaviour
        result = mgr.get_system_prompt(name="World")
        assert result == "Hello World!"

    def test_get_user_prompt_formats(self):
        with patch("builtins.open", mock_open(read_data="User: {q}")):
            mgr = ConcreteFilePromptManager("sys.prompt", "usr.prompt")
        result = mgr.get_user_prompt(q="test")
        assert result == "User: test"


class TestGenerateHomeMenuPrompt:
    """Tests that use the actual template files present in the repository."""

    def test_init_creates_instance(self):
        prompt = GenerateHomeMenuPrompt()
        assert prompt is not None

    def test_get_user_prompt_returns_string(self):
        prompt = GenerateHomeMenuPrompt()
        result = prompt.get_user_prompt()
        assert isinstance(result, str)
        assert len(result) > 0

    def test_get_system_prompt_returns_string(self):
        prompt = GenerateHomeMenuPrompt()
        result = prompt.get_system_prompt()
        assert isinstance(result, str)


class TestGetKindergartenMenuPrompt:
    def test_init_creates_instance(self):
        prompt = GetKindergartenMenuPrompt()
        assert prompt is not None

    def test_get_user_prompt_with_week(self):
        prompt = GetKindergartenMenuPrompt()
        result = prompt.get_user_prompt(week=1)
        assert isinstance(result, str)

    def test_get_system_prompt_returns_string(self):
        prompt = GetKindergartenMenuPrompt()
        result = prompt.get_system_prompt()
        assert isinstance(result, str)


class TestMergeMenuPrompt:
    def test_init_creates_instance(self):
        prompt = MergeMenuPrompt()
        assert prompt is not None

    def test_get_user_prompt_formats_menus(self):
        prompt = MergeMenuPrompt()
        result = prompt.get_user_prompt(first_menu="menu1", second_menu="menu2")
        assert "menu1" in result
        assert "menu2" in result

    def test_get_system_prompt_returns_empty(self):
        prompt = MergeMenuPrompt()
        result = prompt.get_system_prompt()
        assert result == ""


from lib.use_case.prompts.PromptManager import PromptManager


class TestPromptManagerAbstractBodies:
    def test_abstract_get_user_prompt_body_returns_none(self):
        """Call PromptManager.get_user_prompt body directly to cover the pass statement."""
        prompt = GenerateHomeMenuPrompt()
        assert PromptManager.get_user_prompt(prompt) is None

    def test_abstract_get_system_prompt_body_returns_none(self):
        """Call PromptManager.get_system_prompt body directly to cover the pass statement."""
        prompt = GenerateHomeMenuPrompt()
        assert PromptManager.get_system_prompt(prompt) is None


class TestShoppingListPrompt:
    def test_init_creates_instance(self):
        prompt = ShoppingListPrompt()
        assert prompt is not None

    def test_get_user_prompt_formats_menu(self):
        prompt = ShoppingListPrompt()
        result = prompt.get_user_prompt(menu="pasta, chicken")
        assert "pasta, chicken" in result

    def test_get_system_prompt_returns_string(self):
        prompt = ShoppingListPrompt()
        result = prompt.get_system_prompt()
        assert isinstance(result, str)
