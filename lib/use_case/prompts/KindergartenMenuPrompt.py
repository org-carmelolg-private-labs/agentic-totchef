"""
This module provides utility functions to generate system prompts for an expert assistant.
"""
from lib.use_case.prompts.FilePromptManager import FilePromptManager

class GetKindergartenMenuPrompt(FilePromptManager):
    def __init__(self):
        super().__init__(
            system_prompt_path='lib/use_case/prompts/templates/kindergarten_menu_system.prompt',
            user_prompt_path='lib/use_case/prompts/templates/kindergarten_menu_user.prompt'
        )

    def get_user_prompt(self, week: int):
        return self.user_prompt_template.format(week=week)
