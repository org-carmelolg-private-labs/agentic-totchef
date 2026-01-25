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
        :param prompt: the user prompt for the chat
        :param system_prompt: the system prompt to guide the model's behavior
        :param chatbot_mode: enables streaming mode if True
        :return: the response from the language model
        """

        config: ProviderConfiguration = ProviderConfiguration(think=bool(think), stream=chatbot_mode)
        return current_provider.chat(prompt=prompt, system_prompt=system_prompt, model=llm, config=config)

    @staticmethod
    def chat(prompt: str, chatbot_mode: bool = True, tools: dict = None, system_prompt: str = None, disable_think: bool = False):
        """
        Facilitates a chat interaction with the specified language model, incorporating tool calls.
        :param prompt: the user prompt for the chat
        :param chatbot_mode: enables streaming mode if True
        :param tools: a dictionary of available tool functions
        :param system_prompt: the system prompt to guide the model's behavior
        :param disable_think: disables the model to think before responding
        :return: the response from the language model
        """

        functions = {}
        if tools:
            functions.update(tools)

        enable_think = False if disable_think else think

        config: ProviderConfiguration = ProviderConfiguration(think=bool(enable_think), stream=chatbot_mode)
        return current_provider.chat(prompt=prompt, model=llm, system_prompt=system_prompt, tools=functions, config=config)
