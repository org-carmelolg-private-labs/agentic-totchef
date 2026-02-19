"""
HomeMenuStep Module

This module defines the HomeMenuStep class, which generates a home menu for the week
using the LLM and HomeKitchenTools. It is part of the TotChef workflow.
"""

import uuid
from lib.use_case.steps.AbstractStep import AbstractStep
from lib.use_case.steps.StepResult import StepResult

from lib.adapters.outbound.LLMExecutor import chat
from lib.use_case.prompts.HomeMenuPrompt import GenerateHomeMenuPrompt
from lib.use_case.tools import HomeKitchenTools

home_menu_prompt = GenerateHomeMenuPrompt()


class HomeMenuStep(AbstractStep):
    """
    Step to generate a home menu for the week.

    This class uses the LLM to create a menu tailored for home use, incorporating
    tools from HomeKitchenTools for enhanced functionality.
    """

    def __init__(self):
        """
        Initialize the HomeMenuStep instance.

        Generates a unique step ID for this step.
        """
        self.step_id = uuid.uuid4()

    def execute(self) -> StepResult:
        """
        Execute the home menu generation.

        Generates a home menu for Week 1 using the LLM with system and user prompts,
        and available tools from HomeKitchenTools.

        Returns:
            StepResult: The result containing the generated home menu.
        """
        print("Generating Home Menu for Week 1...")
        home_menu = chat(
            prompt=home_menu_prompt.get_user_prompt(),
            system_prompt=home_menu_prompt.get_system_prompt(),
            chatbot_mode=False,
            tools=HomeKitchenTools.available_functions()).message.content

        return StepResult(step_id=self.step_id,
                          result=home_menu)
