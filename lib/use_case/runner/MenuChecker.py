from typing import Dict, Any
import json

from lib.adapters.outbound.LLMExecutor import LLMExecutor
from lib.use_case.prompts.CheckerMenuPrompt import CheckerMenuPrompt
from lib.use_case.tools import HomeKitchenTools


class MenuChecker:
    """
    MenuChecker delegates validation and substitution to the LLM.

    The LLM is provided with the full menu (as JSON) and has access to
    HomeKitchenTools functions so it can look up replacement dishes. The
    LLM must return the final menu as a JSON object (string) so this class
    can parse it and return a Python dict.
    """

    def __init__(self, menu: Dict[str, Dict[str, str]]):
        # store original menu (keys are expected to be strings)
        self.menu = menu
        self.llm = LLMExecutor.get_instance()
        self.prompt_manager = CheckerMenuPrompt()

    def validate_and_fix(self) -> Dict[str, Dict[str, str]]:
        """
        Ask the LLM to validate the menu according to the business rules and
        return the possibly modified menu. If the LLM response cannot be
        parsed as JSON/dict, the original menu is returned unchanged.
        """
        try:
            menu_json = json.dumps(self.menu, ensure_ascii=False)
        except Exception:
            # fallback to string conversion
            menu_json = str(self.menu)

        user_prompt = self.prompt_manager.get_user_prompt(menu_json)
        system_prompt = self.prompt_manager.get_system_prompt()

        try:
            # Provide the LLM with the HomeKitchenTools so it can call functions
            tools = HomeKitchenTools.available_functions()

            response = self.llm.chat(
                prompt=user_prompt,
                chatbot_mode=False,
                tools=tools,
                system_prompt=system_prompt,
            )

            content = None
            # The provider typically returns an object with message.content
            if hasattr(response, 'message') and hasattr(response.message, 'content'):
                content = response.message.content
            elif isinstance(response, dict):
                # some providers may return a simple dict with 'content'
                content = response.get('content') or response.get('message')
            elif hasattr(response, 'content'):
                content = response.content

            if not content:
                return self.menu

            # Try to parse JSON first (recommended format from the LLM)
            try:
                parsed = json.loads(content)
                if isinstance(parsed, dict):
                    return parsed
            except Exception:
                pass

            # If content is not pure JSON, try eval as a last resort
            try:
                parsed = eval(content)
                if isinstance(parsed, dict):
                    return parsed
            except Exception:
                pass

            # Could not parse a structured menu -> return original
            return self.menu

        except Exception:
            # In case of any errors (network, provider, tools), return original
            return self.menu
