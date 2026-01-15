from lib.commons.Constants import Constants
from lib.commons.EnvironmentVariables import EnvironmentVariables
from lib.core.providers.LLMProviderFactory import LLMProviderFactory
from lib.core.providers.model.LLMProviderConfiguration import ProviderConfiguration
from lib.core.tools import KindergartenTools, HomeKitchenTools

env = EnvironmentVariables()

const = Constants.get_instance()
current_provider = LLMProviderFactory.get_instance()
think = env.get_provider_think_mode()
llm = env.get_language_model()
embedding_llm = env.get_embedding_model()

def chat(prompt: str, system_prompt: str = None):
    """
    Facilitates a chat interaction with the specified language model, incorporating tool calls.
    :param prompt:
    :return: 
    """

    _functions = {}
    _functions.update(KindergartenTools.available_functions())
    _functions.update(HomeKitchenTools.available_functions())
    functions = _functions

    config: ProviderConfiguration = ProviderConfiguration(think=think, stream=False)
    return current_provider.chat(prompt=prompt, model=llm, tools=functions, config=config)
