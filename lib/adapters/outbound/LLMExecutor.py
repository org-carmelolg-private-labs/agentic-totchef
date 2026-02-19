"""
LLMExecutor Module

This module provides functions for interacting with Large Language Models (LLMs).
It abstracts the underlying LLM provider and configuration, allowing simple chat and tool-enabled interactions.

The executor uses environment variables and constants to configure the LLM provider, model, and behavior.
"""

from lib.commons.Constants import Constants
from lib.commons.EnvironmentVariables import get_embedding_model, get_language_model, get_thinking_mode
from lib.core.providers.LLMProviderFactory import LLMProviderFactory
from lib.core.providers.model.LLMProviderConfiguration import ProviderConfiguration

# Initialize environment and constants
const = Constants.get_instance()
current_provider = LLMProviderFactory.get_instance()

# Retrieve configuration from environment
think = get_thinking_mode()  # Whether the model should "think" before responding
llm = get_language_model()  # The primary language model to use
embedding_llm = get_embedding_model()  # The embedding model (not used in this class)


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
