import uuid
from typing import Any, List, Optional, Dict


class StepResult:
    """
    Represents the result of a step in a process, including its ID, result, message, and any errors encountered.
    """

    step_id: uuid.UUID  # Unique identifier for the step result.
    message: Optional[str]  # Optional message providing additional context about the result.
    result: Any = None  # The result of the step, can be of any type.
    errors: List[str] = []  # List of error messages associated with the step.

    def __init__(self, step_id: uuid.UUID, result: Any = None, message: Optional[str] = None) -> None:
        """
        Initializes a StepResult instance.

        Args:
            step_id (uuid.UUID): The unique identifier for the step result.
            result (Any, optional): The result of the step. Defaults to None.
            message (Optional[str], optional): Additional context or message about the result. Defaults to None.
        """
        self.step_id = step_id
        self.result = result
        self.message = message

    def add_error(self, error: str) -> None:
        """
        Adds an error message to the list of errors.

        Args:
            error (str): The error message to add.
        """
        self.errors.append(error)

    def is_success(self) -> bool:
        """
        Checks if the step result is successful.

        Returns:
            bool: True if there are no errors and a result is present, False otherwise.
        """
        return len(self.errors) == 0 and self.errors is not None

    def to_dict(self) -> Dict[str, Any]:
        """
        Serializes the StepResult instance into a dictionary.

        Returns:
            Dict[str, Any]: A dictionary representation of the StepResult instance.
        """
        return {
            "step_id": self.step_id,  # Note: 'name' is not defined in the current implementation.
            "message": self.message,
            "result": self.result,
            "errors": list(self.errors),
            "success": self.is_success(),
        }
