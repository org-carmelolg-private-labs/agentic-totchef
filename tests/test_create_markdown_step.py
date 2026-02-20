"""
Unit tests for lib.use_case.steps.CreateMarkdownStep.
"""

import pathlib
import uuid
from unittest.mock import patch, MagicMock

from lib.use_case.steps.CreateMarkdownStep import CreateMarkdownStep
from lib.use_case.steps.StepResult import StepResult


class TestCreateMarkdownStep:
    def test_execute_creates_file(self):
        step = CreateMarkdownStep()
        result = step.execute(full_menu="menu content", shopping_list="list content")
        assert isinstance(result, StepResult)
        assert result.is_success()
        assert result.result is not None
        file_path = pathlib.Path(result.result)
        assert file_path.exists()
        content = file_path.read_text(encoding="utf-8")
        assert "menu content" in content
        assert "list content" in content

    def test_execute_handles_empty_inputs(self):
        step = CreateMarkdownStep()
        result = step.execute(full_menu=None, shopping_list=None)
        assert result.is_success()
        content = pathlib.Path(result.result).read_text(encoding="utf-8")
        assert "(no menu provided)" in content
        assert "(no shopping list provided)" in content

    def test_execute_returns_error_on_failure(self):
        step = CreateMarkdownStep()
        import lib.use_case.steps.CreateMarkdownStep as csm
        # Patch write_text on a real Path instance by mocking the method at class level
        with patch.object(pathlib.Path, "write_text", side_effect=OSError("disk full")):
            result = step.execute(full_menu="menu", shopping_list="list")
        assert not result.is_success()
        assert len(result.errors) > 0
