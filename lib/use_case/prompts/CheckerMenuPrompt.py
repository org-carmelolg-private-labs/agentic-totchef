"""
Prompt manager for validating and suggesting substitutions for a full menu.
"""
from lib.use_case.prompts.FilePromptManager import FilePromptManager

class CheckerMenuPrompt(FilePromptManager):
    def __init__(self):
        super().__init__(
            system_prompt_path='lib/use_case/prompts/templates/checker_menu_system.prompt',
            user_prompt_path='lib/use_case/prompts/templates/checker_menu_user.prompt'
        )

    def get_user_prompt(self, menu: str):
        return self.user_prompt_template.format(menu=menu)

    def get_system_prompt(self, *args):
        return self.system_prompt_template
