"""
This module provides utility functions to generate prompts for shopping list generation.
"""
from lib.use_case.prompts.FilePromptManager import FilePromptManager

class ShoppingListPrompt(FilePromptManager):
    def __init__(self):
        super().__init__(
            system_prompt_path='lib/use_case/prompts/templates/shopping_list_system.prompt',
            user_prompt_path='lib/use_case/prompts/templates/shopping_list_user.prompt'
        )

    def get_user_prompt(self, menu: str):
        return self.user_prompt_template.format(menu=menu)
