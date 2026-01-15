from lib.commons.Constants import Constants
from lib.commons.EnvironmentVariables import EnvironmentVariables
from lib.core.providers.LLMProviderFactory import LLMProviderFactory
from lib.core.providers.model.LLMProviderConfiguration import ProviderConfiguration
from lib.core.tools import KindergartenTools, HomeKitchenTools

env = EnvironmentVariables()

const = Constants.get_instance()
current_provider = LLMProviderFactory.get_instance()
think = env.get_thinking_mode()
llm = env.get_language_model()
embedding_llm = env.get_embedding_model()


def ask(prompt: str, system_prompt: str = None, chatbot_mode: bool = False):
    """
    Simple chat interaction with the specified language model.
    :param prompt:
    :param system_prompt:
    :param chatbot_mode:
    :return:
    """

    config: ProviderConfiguration = ProviderConfiguration(think=bool(think), stream=chatbot_mode)
    return current_provider.chat(prompt=prompt, system_prompt=system_prompt, model=llm, config=config)

def chat(prompt: str, chatbot_mode: bool = True, system_prompt: str = None):
    """
    Facilitates a chat interaction with the specified language model, incorporating tool calls.
    :param prompt:
    :param chatbot_mode:
    :param system_prompt:
    :return:
    """

    _functions = {}
    _functions.update(KindergartenTools.available_functions())
    _functions.update(HomeKitchenTools.available_functions())
    functions = _functions

    config: ProviderConfiguration = ProviderConfiguration(think=bool(think), stream=chatbot_mode)
    return current_provider.chat(prompt=prompt, model=llm, system_prompt=system_prompt, tools=functions, config=config)
