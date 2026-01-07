"""
Module to load environment variables from a .env file.
"""
import os
from dotenv import load_dotenv

class EnvironmentVariables:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            load_dotenv()  # Load .env once at initialization
        return cls._instance

    @staticmethod
    def get_embedding_model(default: str = None) -> str:
        return os.getenv("EMBEDDING_MODEL", default)

    @staticmethod
    def get_language_model(default: str = None) -> str:
        return os.getenv("LANGUAGE_MODEL", default)

    @staticmethod
    def get_thinking_mode(default: str = None) -> str:
        return os.getenv("THINKING_MODE", default)

    @staticmethod
    def get_kindergarten_api_host(default: str = None) -> str:
        return os.getenv("KINDERGARTEN_API_HOST", default)

    @staticmethod
    def get_home_kitchen_api_host(default: str = None) -> str:
        return os.getenv("HOME_KITCHEN_API_HOST", default)

    @staticmethod
    def get_kindergarten_api_path(default: str = None) -> str:
        return os.getenv("KINDERGARTEN_API_PATH", default)

    @staticmethod
    def get_home_kitchen_api_path(default: str = None) -> str:
        return os.getenv("HOME_KITCHEN_API_PATH", default)

    @staticmethod
    def get_llm_provider(default: str = None) -> str:
        return os.getenv("LLM_PROVIDER", default)
