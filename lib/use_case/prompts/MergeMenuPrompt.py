from lib.use_case.prompts.FilePromptManager import FilePromptManager

class MergeMenuPrompt(FilePromptManager):
    """
    This module provides utility functions to generate system prompts for merging two weekly menus.
    """
    def __init__(self):
        super().__init__(
            system_prompt_path='',
            user_prompt_path='lib/use_case/prompts/templates/merge_menu_user.prompt'
        )

    def get_user_prompt(self, morning_menu: str, evening_menu: str):
        return self.user_prompt_template.format(morning_menu=morning_menu, evening_menu=evening_menu)
    
    def get_system_prompt(self, *args):
        return ""