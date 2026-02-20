"""
Unit tests for lib.use_case.steps.HomeMenuStep, KindergartenMenuStep,
MergeMenuStep, and ShoppingListStep.
"""

import uuid
from unittest.mock import patch, MagicMock

from lib.use_case.steps.StepResult import StepResult


class TestHomeMenuStep:
    def test_execute_returns_step_result(self):
        from lib.use_case.steps.HomeMenuStep import HomeMenuStep
        import lib.use_case.steps.HomeMenuStep as hms

        mock_response = MagicMock()
        mock_response.message.content = "generated home menu"

        with patch.object(hms, "chat", return_value=mock_response):
            step = HomeMenuStep()
            result = step.execute()

        assert isinstance(result, StepResult)
        assert result.result == "generated home menu"
        assert result.step_id == step.step_id

    def test_step_id_is_set(self):
        from lib.use_case.steps.HomeMenuStep import HomeMenuStep
        step = HomeMenuStep()
        assert isinstance(step.step_id, uuid.UUID)


class TestKindergartenMenuStep:
    def test_execute_returns_step_result(self):
        from lib.use_case.steps.KindergartenMenuStep import KindergartenMenuStep
        import lib.use_case.steps.KindergartenMenuStep as kms

        mock_response = MagicMock()
        mock_response.message.content = "generated kg menu"

        with patch.object(kms, "chat", return_value=mock_response):
            step = KindergartenMenuStep()
            result = step.execute()

        assert isinstance(result, StepResult)
        assert result.result == "generated kg menu"
        assert result.step_id == step.step_id

    def test_step_id_is_set(self):
        from lib.use_case.steps.KindergartenMenuStep import KindergartenMenuStep
        step = KindergartenMenuStep()
        assert isinstance(step.step_id, uuid.UUID)


class TestMergeMenuStep:
    def test_execute_returns_step_result(self):
        from lib.use_case.steps.MergeMenuStep import MergeMenuStep
        import lib.use_case.steps.MergeMenuStep as mms

        mock_response = MagicMock()
        mock_response.message.content = "merged menu"

        with patch.object(mms, "ask", return_value=mock_response):
            step = MergeMenuStep()
            result = step.execute("menu1", "menu2")

        assert isinstance(result, StepResult)
        assert result.result == "merged menu"

    def test_step_id_is_set(self):
        from lib.use_case.steps.MergeMenuStep import MergeMenuStep
        step = MergeMenuStep()
        assert isinstance(step.step_id, uuid.UUID)


class TestShoppingListStep:
    def test_execute_returns_step_result(self):
        from lib.use_case.steps.ShoppingListStep import ShoppingListStep
        import lib.use_case.steps.ShoppingListStep as sls

        mock_response = MagicMock()
        mock_response.message.content = "shopping list"

        with patch.object(sls, "ask", return_value=mock_response):
            step = ShoppingListStep()
            result = step.execute("full menu")

        assert isinstance(result, StepResult)
        assert result.result == "shopping list"

    def test_step_id_is_set(self):
        from lib.use_case.steps.ShoppingListStep import ShoppingListStep
        step = ShoppingListStep()
        assert isinstance(step.step_id, uuid.UUID)
