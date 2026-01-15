from lib.commons.Constants import Constants
from lib.commons.EnvironmentVariables import EnvironmentVariables
from lib.core.providers.OllamaProvider import OllamaProvider

env = EnvironmentVariables()
LLM_PROVIDER = env.get_llm_provider('ollama')

const = Constants.get_instance()
ollama_provider = OllamaProvider.get_instance()

class LLMProviderFactory:
    """
    Factory class to get the appropriate LLM provider instance based on configuration.
    """
    @staticmethod
    def get_instance():
        if LLM_PROVIDER == const.llm_provider_ollama:
            return ollama_provider
        else:
            return None