"""
KindergartenMenuStep Module

This module defines the KindergartenMenuStep class, which generates a kindergarten menu for the week
using the LLM and KindergartenTools. It is part of the TotChef workflow.
"""

import uuid
from lib.adapters.outbound.LLMExecutor import LLMExecutor
from lib.use_case.prompts.KindergartenMenuPrompt import GetKindergartenMenuPrompt
from lib.use_case.steps.AbstractStep import AbstractStep
from lib.use_case.steps.StepResult import StepResult
from lib.use_case.tools import KindergartenTools

llm_executor = LLMExecutor.get_instance()
kindergarten_menu_prompt = GetKindergartenMenuPrompt()


class KindergartenMenuStep(AbstractStep):
    """
    Step to generate a kindergarten menu for the week.

    This class uses the LLM to create a menu tailored for kindergarten use, incorporating
    tools from KindergartenTools for enhanced functionality.
    """

    def __init__(self):
        """
        Initialize the KindergartenMenuStep instance.

        Generates a unique step ID for this step.
        """
        self.step_id = uuid.uuid4()

    def execute(self) -> StepResult:
        """
        Execute the kindergarten menu generation.

        Generates a kindergarten menu for Week 1 using the LLM with system and user prompts,
        and available tools from KindergartenTools.

        Returns:
            StepResult: The result containing the generated kindergarten menu.
        """
        print("Generating Kindergarten Menu for Week 1...")
        kindergarten_menu = llm_executor.chat(
            prompt=kindergarten_menu_prompt.get_user_prompt(1),
            chatbot_mode=False,
            tools=KindergartenTools.available_functions(),
            system_prompt=kindergarten_menu_prompt.get_system_prompt()).message.content

        return StepResult(step_id=self.step_id,
                          result=kindergarten_menu)
