"""
Unit tests for lib.use_case.steps.StepResult and lib.use_case.steps.AbstractStep.
"""

import uuid
import pytest
from lib.use_case.steps.StepResult import StepResult
from lib.use_case.steps.AbstractStep import AbstractStep


class ConcreteStep(AbstractStep):
    """Minimal concrete step for testing AbstractStep."""

    def __init__(self):
        self.step_id = uuid.uuid4()

    def execute(self, *args):
        return StepResult(step_id=self.step_id, result="done")


class TestStepResult:
    def test_init_defaults(self):
        sid = uuid.uuid4()
        sr = StepResult(step_id=sid)
        assert sr.step_id == sid
        assert sr.result is None
        assert sr.message is None

    def test_init_with_result_and_message(self):
        sid = uuid.uuid4()
        sr = StepResult(step_id=sid, result="data", message="ok")
        assert sr.result == "data"
        assert sr.message == "ok"

    def test_add_error(self):
        sr = StepResult(step_id=uuid.uuid4())
        sr.errors = []
        sr.add_error("something went wrong")
        assert "something went wrong" in sr.errors

    def test_is_success_no_errors(self):
        sr = StepResult(step_id=uuid.uuid4(), result="ok")
        sr.errors = []
        assert sr.is_success() is True

    def test_is_success_with_errors(self):
        sr = StepResult(step_id=uuid.uuid4(), result="ok")
        sr.errors = []
        sr.add_error("err")
        assert sr.is_success() is False

    def test_to_dict(self):
        sid = uuid.uuid4()
        sr = StepResult(step_id=sid, result="res", message="msg")
        sr.errors = []
        d = sr.to_dict()
        assert d["step_id"] == sid
        assert d["result"] == "res"
        assert d["message"] == "msg"
        assert d["errors"] == []
        assert d["success"] is True


class TestAbstractStep:
    def test_execute_returns_step_result(self):
        step = ConcreteStep()
        result = step.execute()
        assert isinstance(result, StepResult)
        assert result.result == "done"

    def test_step_id_is_uuid(self):
        step = ConcreteStep()
        assert isinstance(step.step_id, uuid.UUID)

    def test_abstract_execute_body_returns_none(self):
        """Call AbstractStep.execute body directly to cover the pass statement."""
        step = ConcreteStep()
        assert AbstractStep.execute(step) is None
