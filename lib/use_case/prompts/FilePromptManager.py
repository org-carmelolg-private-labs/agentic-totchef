from lib.use_case.prompts.PromptManager import PromptManager

class FilePromptManager(PromptManager):
    def __init__(self, system_prompt_path: str, user_prompt_path: str):
        self.system_prompt_template = self._load_prompt(system_prompt_path)
        self.user_prompt_template = self._load_prompt(user_prompt_path)

    def _load_prompt(self, file_path: str) -> str:
        if file_path is None:
            return ""
        with open(file_path, 'r') as f:
            return f.read()

    def get_system_prompt(self, *args, **kwargs):
        return self.system_prompt_template.format(*args, **kwargs)

    def get_user_prompt(self, *args, **kwargs):
        return self.user_prompt_template.format(*args, **kwargs)
