"""
OllamaProvider Module

This module provides the OllamaProvider class, which implements the Provider interface
for interacting with Ollama LLM models. It supports simple chats, agentic chats with tools,
and text embedding.
"""

from typing import Iterator, Union, List

import ollama as OllamaClient

from lib.commons.EnvironmentVariables import EnvironmentVariables
from lib.core.providers.LLMProvider import Provider
from lib.core.providers.model.LLMProviderConfiguration import ProviderConfiguration

env = EnvironmentVariables()


class OllamaProvider(Provider):
    """
    Singleton provider for Ollama LLM interactions.

    This class provides methods to perform chats with Ollama models, including simple chats,
    agentic chats with tool calls, and text embeddings. It follows the singleton pattern
    to ensure only one instance exists.

    Attributes:
        __instance: The singleton instance of the class.
    """

    __instance = None

    @staticmethod
    def get_instance():
        """
        Get the singleton instance of OllamaProvider.

        Returns:
            OllamaProvider: The singleton instance.
        """
        if OllamaProvider.__instance is None:
            OllamaProvider()
        return OllamaProvider.__instance

    def __init__(self):
        """
        Initialize the singleton instance of OllamaProvider.

        Raises:
            Exception: If an instance already exists (singleton violation).
        """
        if OllamaProvider.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            OllamaProvider.__instance = self

    def agentic_chat(self, prompt: str, model: str, system_prompt: str, assistant_prompt: str, tools: dict,
                     config: ProviderConfiguration = None) -> Union[
        OllamaClient.ChatResponse, Iterator[OllamaClient.ChatResponse]]:
        """
        Perform an agentic chat with tool calls.

        This method handles conversations where the LLM can call tools, process their results,
        and generate a final response.

        Args:
            prompt (str): The user prompt.
            model (str): The Ollama model to use.
            system_prompt (str): The system prompt.
            assistant_prompt (str): The assistant prompt.
            tools (dict): Dictionary of available tools.
            config (ProviderConfiguration, optional): Configuration for the chat.

        Returns:
            Union[OllamaClient.ChatResponse, Iterator[OllamaClient.ChatResponse]]: The chat response.
        """
        think = True if config is not None and config.get_think() is not None and config.get_think() else False
        stream = True if config is not None and config.get_stream() is not None and config.get_stream() else False

        _messages = []

        _messages = [{"role": "user", "content": prompt}]

        if assistant_prompt is not None:
            _messages.append({'role': 'assistant', 'content': assistant_prompt})

        response = OllamaClient.chat(model=model, messages=_messages, tools=tools.values(),
                                     think=think)
        _messages.append(response.message)

        if response.message.tool_calls:
            for tc in response.message.tool_calls:
                if tc.function.name in tools:
                    result = tools[tc.function.name](**tc.function.arguments)
                    # add the tool result to the messages
                    _messages.append({'role': 'tool', 'tool_name': tc.function.name, 'content': str(result)})
                else:
                    print(f"No tool available for {tc.function.name}")

        if system_prompt is not None:
            _messages.append({'role': 'system', 'content': system_prompt})

        # generate the final response
        return OllamaClient.chat(model=model, messages=_messages, stream=stream,
                                 think=False)

    def simple_chat(self, prompt: str, model: str, system_prompt: str = None, config: ProviderConfiguration = None) -> \
            Union[
                OllamaClient.ChatResponse, Iterator[OllamaClient.ChatResponse]]:
        """
        Perform a simple chat without tools.

        Args:
            prompt (str): The user prompt.
            model (str): The Ollama model to use.
            system_prompt (str, optional): The system prompt.
            config (ProviderConfiguration, optional): Configuration for the chat.

        Returns:
            Union[OllamaClient.ChatResponse, Iterator[OllamaClient.ChatResponse]]: The chat response.
        """
        _messages = [{'role': 'user', 'content': prompt}]
        if system_prompt is not None:
            _messages.append({'role': 'system', 'content': system_prompt})

        return OllamaClient.chat(
            model=model,
            messages=_messages,
            stream=config.get_stream(),
            think=config.get_think()
        )

    def embed(self, text: str, embedding_model: str = env.get_embedding_model()) -> List[float]:
        """
        Generate embeddings for the given text.

        Args:
            text (str): The text to embed.
            embedding_model (str, optional): The embedding model to use. Defaults to the configured model.

        Returns:
            List[float]: The embedding vector.
        """
        return OllamaClient.embed(model=embedding_model, input=text)['embeddings'][0]
