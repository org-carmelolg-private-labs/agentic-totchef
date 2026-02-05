"""
MergeMenuStep Module

This module defines the MergeMenuStep class, which merges two weekly menus
using the LLM. It is part of the TotChef workflow.
"""

import uuid
from lib.use_case.steps.AbstractStep import AbstractStep
from lib.use_case.steps.StepResult import StepResult

from lib.adapters.outbound.LLMExecutor import LLMExecutor
from lib.use_case.prompts.MergeMenuPrompt import MergeMenuPrompt

llm_executor = LLMExecutor.get_instance()
merge_menu_prompt = MergeMenuPrompt()


class MergeMenuStep(AbstractStep):
    """
    Step to merge two weekly menus.

    This class uses the LLM to combine two menus into a single merged menu.
    """

    def __init__(self):
        """
        Initialize the MergeMenuStep instance.

        Generates a unique step ID for this step.
        """
        self.step_id = uuid.uuid4()

    def execute(self, first_menu: str, second_menu: str) -> StepResult:
        """
        Execute the menu merging.

        Merges the first and second menus using the LLM with the merge prompt.

        Args:
            first_menu (str): The first menu to merge.
            second_menu (str): The second menu to merge.

        Returns:
            StepResult: The result containing the merged menu.
        """
        print("Merging menus...")
        merged_menu = llm_executor.ask(
            prompt=merge_menu_prompt.get_user_prompt(first_menu, second_menu),
            chatbot_mode=False,
            disable_think=True
        ).message.content

        return StepResult(step_id=self.step_id,
                          result=merged_menu)
