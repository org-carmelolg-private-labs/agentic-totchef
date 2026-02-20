"""
Unit tests for lib.use_case.runner.TotChef (run and log_element functions).
"""

import uuid
from unittest.mock import patch, MagicMock

import lib.use_case.runner.TotChef as tot_chef
from lib.use_case.steps.StepResult import StepResult


def _make_step_result(step_id, content):
    sr = StepResult(step_id=step_id, result=content)
    sr.errors = []
    return sr


class TestTotChefRunner:
    def test_log_element_prints(self, capsys):
        tot_chef.log_element("Hello World")
        captured = capsys.readouterr()
        assert "Hello World" in captured.out
        assert "---" in captured.out

    def test_run_executes_all_steps(self):
        kg_id = uuid.uuid4()
        home_id = uuid.uuid4()

        kg_result = _make_step_result(kg_id, "kg menu")
        home_result = _make_step_result(home_id, "home menu")
        merge_result = _make_step_result(uuid.uuid4(), "merged menu")
        shopping_result = _make_step_result(uuid.uuid4(), "shopping list")
        markdown_result = _make_step_result(uuid.uuid4(), "/static/menu.md")

        mock_kg_step = MagicMock()
        mock_kg_step.step_id = kg_id
        mock_kg_step.execute.return_value = kg_result

        mock_home_step = MagicMock()
        mock_home_step.step_id = home_id
        mock_home_step.execute.return_value = home_result

        mock_merge_step = MagicMock()
        mock_merge_step.step_id = uuid.uuid4()
        mock_merge_step.execute.return_value = merge_result

        mock_shopping_step = MagicMock()
        mock_shopping_step.execute.return_value = shopping_result

        mock_md_step = MagicMock()
        mock_md_step.execute.return_value = markdown_result

        # Patch the executor futures to return step results directly
        class MockFuture:
            def __init__(self, result):
                self._result = result

            def result(self):
                return self._result

        class MockExecutor:
            def __enter__(self):
                return self

            def __exit__(self, *args):
                pass

            def submit(self, fn, *args, **kwargs):
                return MockFuture(fn(*args, **kwargs))

        with patch("lib.use_case.runner.TotChef.KindergartenMenuStep", return_value=mock_kg_step), \
             patch("lib.use_case.runner.TotChef.HomeMenuStep", return_value=mock_home_step), \
             patch("lib.use_case.runner.TotChef.MergeMenuStep", return_value=mock_merge_step), \
             patch("lib.use_case.runner.TotChef.ShoppingListStep", return_value=mock_shopping_step), \
             patch("lib.use_case.runner.TotChef.CreateMarkdownStep", return_value=mock_md_step), \
             patch("lib.use_case.runner.TotChef.ProcessPoolExecutor", return_value=MockExecutor()):
            tot_chef.run()

        mock_merge_step.execute.assert_called_once()
        mock_shopping_step.execute.assert_called_once()
        mock_md_step.execute.assert_called_once()

    def test_run_handles_failed_markdown(self):
        """Verify run still completes when markdown step fails."""
        kg_id = uuid.uuid4()
        home_id = uuid.uuid4()

        kg_result = _make_step_result(kg_id, "kg menu")
        home_result = _make_step_result(home_id, "home menu")
        merge_result = _make_step_result(uuid.uuid4(), "merged menu")
        shopping_result = _make_step_result(uuid.uuid4(), "shopping list")

        failed_md = StepResult(step_id=uuid.uuid4(), result=None)
        failed_md.errors = ["disk full"]

        mock_kg_step = MagicMock()
        mock_kg_step.step_id = kg_id
        mock_kg_step.execute.return_value = kg_result

        mock_home_step = MagicMock()
        mock_home_step.step_id = home_id
        mock_home_step.execute.return_value = home_result

        mock_merge_step = MagicMock()
        mock_merge_step.execute.return_value = merge_result

        mock_shopping_step = MagicMock()
        mock_shopping_step.execute.return_value = shopping_result

        mock_md_step = MagicMock()
        mock_md_step.execute.return_value = failed_md

        class MockFuture:
            def __init__(self, result):
                self._result = result

            def result(self):
                return self._result

        class MockExecutor:
            def __enter__(self):
                return self

            def __exit__(self, *args):
                pass

            def submit(self, fn, *args, **kwargs):
                return MockFuture(fn(*args, **kwargs))

        with patch("lib.use_case.runner.TotChef.KindergartenMenuStep", return_value=mock_kg_step), \
             patch("lib.use_case.runner.TotChef.HomeMenuStep", return_value=mock_home_step), \
             patch("lib.use_case.runner.TotChef.MergeMenuStep", return_value=mock_merge_step), \
             patch("lib.use_case.runner.TotChef.ShoppingListStep", return_value=mock_shopping_step), \
             patch("lib.use_case.runner.TotChef.CreateMarkdownStep", return_value=mock_md_step), \
             patch("lib.use_case.runner.TotChef.ProcessPoolExecutor", return_value=MockExecutor()), \
             patch("builtins.print"):
            tot_chef.run()  # Should not raise
