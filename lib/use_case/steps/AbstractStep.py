"""
AbstractStep Module

This module defines the AbstractStep class, which serves as a base class for all steps
in the TotChef workflow. It provides a common interface and ensures each step has a unique ID.
"""

import uuid
from abc import ABC
from lib.use_case.steps.StepResult import StepResult

class AbstractStep(ABC):
    """
    Abstract base class for workflow steps.

    This class defines the interface for all steps in the TotChef system. Each step
    must have a unique step_id and implement the execute method to perform its logic.

    Attributes:
        step_id (uuid.UUID): A unique identifier for the step instance.
    """

    step_id: uuid.UUID

    def execute(self, *args) -> StepResult:
        """
        Execute the step logic.

        This method must be implemented by subclasses to perform the specific task
        of the step. It accepts variable arguments and returns a StepResult.

        Args:
            *args: Variable arguments passed to the step execution.

        Returns:
            StepResult: The result of the step execution.
        """
        pass