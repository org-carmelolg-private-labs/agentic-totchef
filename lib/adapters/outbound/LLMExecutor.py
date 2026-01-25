from lib.commons.Constants import Constants
from lib.commons.EnvironmentVariables import EnvironmentVariables
from lib.core.providers.LLMProviderFactory import LLMProviderFactory
from lib.core.providers.model.LLMProviderConfiguration import ProviderConfiguration

env = EnvironmentVariables()

const = Constants.get_instance()
current_provider = LLMProviderFactory.get_instance()
think = env.get_thinking_mode()
llm = env.get_language_model()
embedding_llm = env.get_embedding_model()

class LLMExecutor(object):

    __instance = None

    @staticmethod
    def get_instance():
        if LLMExecutor.__instance is None:
            LLMExecutor()
        return LLMExecutor.__instance
    def __init__(self):
        if LLMExecutor.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            LLMExecutor.__instance = self

    @staticmethod
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

    @staticmethod
    def chat(prompt: str, chatbot_mode: bool = True, tools: dict = None, system_prompt: str = None):
        """
        Facilitates a chat interaction with the specified language model, incorporating tool calls.
        :param prompt:
        :param chatbot_mode:
        :param tools:
        :param system_prompt:
        :return:
        """

        functions = {}
        if tools:
            functions.update(tools)

        config: ProviderConfiguration = ProviderConfiguration(think=bool(think), stream=chatbot_mode)
        return current_provider.chat(prompt=prompt, model=llm, system_prompt=system_prompt, tools=functions, config=config)
