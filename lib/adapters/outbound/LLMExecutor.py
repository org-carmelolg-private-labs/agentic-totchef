"""
LLMExecutor Module

This module provides a singleton LLMExecutor class for interacting with Large Language Models (LLMs).
It abstracts the underlying LLM provider and configuration, allowing simple chat and tool-enabled interactions.

The executor uses environment variables and constants to configure the LLM provider, model, and behavior.
"""

from lib.commons.Constants import Constants
from lib.commons.EnvironmentVariables import EnvironmentVariables
from lib.core.providers.LLMProviderFactory import LLMProviderFactory
from lib.core.providers.model.LLMProviderConfiguration import ProviderConfiguration

# Initialize environment and constants
env = EnvironmentVariables()
const = Constants.get_instance()
current_provider = LLMProviderFactory.get_instance()

# Retrieve configuration from environment
think = env.get_thinking_mode()  # Whether the model should "think" before responding
llm = env.get_language_model()  # The primary language model to use
embedding_llm = env.get_embedding_model()  # The embedding model (not used in this class)


class LLMExecutor(object):
    """
    Singleton class for executing interactions with Large Language Models.

    This class provides static methods to perform simple chat interactions or tool-enabled chats
    with the configured LLM. It ensures only one instance exists and handles configuration
    such as thinking mode, streaming, and tool functions.

    Attributes:
        __instance: The singleton instance of the class.
    """

    __instance = None

    @staticmethod
    def get_instance():
        """
        Get the singleton instance of LLMExecutor.

        Returns:
            LLMExecutor: The singleton instance.
        """
        if LLMExecutor.__instance is None:
            LLMExecutor()
        return LLMExecutor.__instance

    def __init__(self):
        """
        Initialize the singleton instance.

        Raises:
            Exception: If an instance already exists (singleton violation).
        """
        if LLMExecutor.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            LLMExecutor.__instance = self

    @staticmethod
    def ask(prompt: str, system_prompt: str = None, chatbot_mode: bool = False, disable_think: bool = False):
        """
        Perform a simple chat interaction with the LLM.

        This method sends a prompt to the LLM and returns the response without tool calls.

        Args:
            prompt (str): The user prompt for the chat.
            system_prompt (str, optional): The system prompt to guide the model's behavior. Defaults to None.
            chatbot_mode (bool, optional): Enables streaming mode if True. Defaults to False.
            disable_think (bool, optional): Disables the model's thinking mode. Defaults to False.

        Returns:
            The response from the language model.
        """
        enable_think = False if disable_think else think

        config: ProviderConfiguration = ProviderConfiguration(think=bool(enable_think), stream=chatbot_mode)
        return current_provider.chat(prompt=prompt, system_prompt=system_prompt, model=llm, config=config)

    @staticmethod
    def chat(prompt: str, chatbot_mode: bool = True, tools: dict = None, system_prompt: str = None, disable_think: bool = False):
        """
        Perform a chat interaction with the LLM, optionally incorporating tool calls.

        This method allows for more advanced interactions, including the use of tools (functions)
        that the LLM can call during the conversation.

        Args:
            prompt (str): The user prompt for the chat.
            chatbot_mode (bool, optional): Enables streaming mode if True. Defaults to True.
            tools (dict, optional): A dictionary of available tool functions. Defaults to None.
            system_prompt (str, optional): The system prompt to guide the model's behavior. Defaults to None.
            disable_think (bool, optional): Disables the model's thinking mode. Defaults to False.

        Returns:
            The response from the language model.
        """
        functions = {}
        if tools:
            functions.update(tools)

        enable_think = False if disable_think else think

        config: ProviderConfiguration = ProviderConfiguration(think=bool(enable_think), stream=chatbot_mode)
        return current_provider.chat(prompt=prompt, model=llm, system_prompt=system_prompt, tools=functions, config=config)
