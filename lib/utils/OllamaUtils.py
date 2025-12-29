"""
Utility functions for interacting with Ollama models for embedding and chat functionalities.
"""
from typing import List
import ollama as _ollama_client
from lib.utils.EnvironmentVariables import EnvironmentVariables

env = EnvironmentVariables()

EMBEDDING_MODEL = env.get_embedding_model('nomic-embed-text:latest')
LANGUAGE_MODEL = env.get_language_model('qwen3:lates')
THINKING_MODE= env.get_thinking_mode('True')

def embed_text(text: str) -> List[float]:
    """
    Generates an embedding for the given text using the specified embedding model.
    :param text:
    :return:
    """
    return _ollama_client.embed(model=EMBEDDING_MODEL, input=text)['embeddings'][0]

def chat(
        user_prompt: str,
        tools: dict,
        system_prompt: str = None,
        assistant_prompt: str = None
):
    """
    Facilitates a chat interaction with the specified language model, incorporating tool calls.
    :param user_prompt:
    :param tools:
    :param system_prompt:
    :param assistant_prompt:
    :return:
    """
    _messages = [{"role": "user", "content": user_prompt}]
    response = _ollama_client.chat(model=LANGUAGE_MODEL, messages=_messages, tools=tools.values(), think=THINKING_MODE)
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
    if assistant_prompt is not None:
        _messages.append({'role': 'assistant', 'content': assistant_prompt})

    # generate the final response
    return _ollama_client.chat(model=LANGUAGE_MODEL, messages=_messages, tools=tools.values(), stream=True, think=False)
