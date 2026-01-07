from lib.commons.Constants import Constants
from lib.commons.EnvironmentVariables import EnvironmentVariables
from lib.core.providers import OllamaProvider
from lib.core.tools import KindergartenTools, HomeKitchenTools

env = EnvironmentVariables()
LLM_PROVIDER = env.get_llm_provider('ollama')

const = Constants.get_instance()

def chat(prompt: str):

    _functions = {}
    _functions.update(KindergartenTools.available_functions())
    _functions.update(HomeKitchenTools.available_functions())
    functions = _functions

    if LLM_PROVIDER == const.llm_provider_ollama:
        return OllamaProvider.chat(user_prompt=prompt, tools=functions)

    return None