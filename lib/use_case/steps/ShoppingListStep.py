"""
ShoppingListStep Module

This module defines the ShoppingListStep class, which generates a shopping list
from a full menu using the LLM. It is part of the TotChef workflow.
"""

import uuid
from lib.use_case.steps.AbstractStep import AbstractStep
from lib.use_case.steps.StepResult import StepResult
from lib.adapters.outbound.LLMExecutor import LLMExecutor
from lib.use_case.prompts.ShoppingListPrompt import ShoppingListPrompt

llm_executor = LLMExecutor.get_instance()
shopping_list_prompt = ShoppingListPrompt()


class ShoppingListStep(AbstractStep):
    """
    Step to generate a shopping list from a full menu.

    This class uses the LLM to create a shopping list based on the provided menu.
    """

    def __init__(self):
        """
        Initialize the ShoppingListStep instance.

        Generates a unique step ID for this step.
        """
        self.step_id = uuid.uuid4()

    def execute(self, full_menu: str) -> StepResult:
        """
        Execute the shopping list generation.

        Generates a shopping list from the full menu using the LLM with system and user prompts.

        Args:
            full_menu (str): The full menu to generate the shopping list from.

        Returns:
            StepResult: The result containing the generated shopping list.
        """
        print("Generating Shopping List...")
        shopping_list = llm_executor.ask(
            prompt=shopping_list_prompt.get_user_prompt(full_menu),
            system_prompt=shopping_list_prompt.get_system_prompt(),
            chatbot_mode=False,
            disable_think=True
        ).message.content

        return StepResult(step_id=self.step_id,
                          result=shopping_list)
