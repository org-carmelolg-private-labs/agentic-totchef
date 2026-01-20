from typing import Iterator, Union, List

import ollama as OllamaClient

from lib.commons.EnvironmentVariables import EnvironmentVariables
from lib.core.providers.LLMProvider import Provider
from lib.core.providers.model.LLMProviderConfiguration import ProviderConfiguration

env = EnvironmentVariables()


class OllamaProvider(Provider):
    __instance = None

    @staticmethod
    def get_instance():
        if OllamaProvider.__instance is None:
            OllamaProvider()
        return OllamaProvider.__instance

    def __init__(self):
        if OllamaProvider.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            OllamaProvider.__instance = self

    def agentic_chat(self, prompt: str, model: str, system_prompt: str, assistant_prompt: str, tools: dict,
                     config: ProviderConfiguration = None) -> Union[
        OllamaClient.ChatResponse, Iterator[OllamaClient.ChatResponse]]:

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
        return OllamaClient.embed(model=embedding_model, input=text)['embeddings'][0]
