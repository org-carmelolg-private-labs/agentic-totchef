"""
Module to load environment variables from a .env file.

This module provides a singleton EnvironmentVariables class that loads environment variables
from a .env file using the python-dotenv library. It ensures that the .env file is loaded only once
and provides static methods to retrieve various configuration values used throughout the application.
"""

import os
from dotenv import load_dotenv

class EnvironmentVariables:
    """
    Singleton class for managing environment variables.

    This class loads environment variables from a .env file once at instantiation and provides
    static methods to access them with optional default values. It follows the singleton pattern
    to ensure the .env file is loaded only once.

    Attributes:
        _instance: The singleton instance of the class.
    """

    _instance = None

    def __new__(cls):
        """
        Create or return the singleton instance of EnvironmentVariables.

        Loads the .env file if this is the first instantiation.

        Returns:
            EnvironmentVariables: The singleton instance.
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            load_dotenv()  # Load .env once at initialization
        return cls._instance

    @staticmethod
    def get_embedding_model(default: str = None) -> str:
        """
        Get the embedding model name from environment variables.

        Args:
            default (str, optional): Default value if EMBEDDING_MODEL is not set. Defaults to None.

        Returns:
            str: The embedding model name or the default value.
        """
        return os.getenv("EMBEDDING_MODEL", default)

    @staticmethod
    def get_language_model(default: str = None) -> str:
        """
        Get the language model name from environment variables.

        Args:
            default (str, optional): Default value if LANGUAGE_MODEL is not set. Defaults to None.

        Returns:
            str: The language model name or the default value.
        """
        return os.getenv("LANGUAGE_MODEL", default)

    @staticmethod
    def get_thinking_mode(default: str = None) -> str:
        """
        Get the thinking mode setting from environment variables.

        Args:
            default (str, optional): Default value if THINKING_MODE is not set. Defaults to None.

        Returns:
            str: The thinking mode setting or the default value.
        """
        return os.getenv("THINKING_MODE", default)

    @staticmethod
    def get_kindergarten_api_host(default: str = None) -> str:
        """
        Get the kindergarten API host from environment variables.

        Args:
            default (str, optional): Default value if KINDERGARTEN_API_HOST is not set. Defaults to None.

        Returns:
            str: The kindergarten API host or the default value.
        """
        return os.getenv("KINDERGARTEN_API_HOST", default)

    @staticmethod
    def get_home_kitchen_api_host(default: str = None) -> str:
        """
        Get the home kitchen API host from environment variables.

        Args:
            default (str, optional): Default value if HOME_KITCHEN_API_HOST is not set. Defaults to None.

        Returns:
            str: The home kitchen API host or the default value.
        """
        return os.getenv("HOME_KITCHEN_API_HOST", default)

    @staticmethod
    def get_kindergarten_api_path(default: str = None) -> str:
        """
        Get the kindergarten API path from environment variables.

        Args:
            default (str, optional): Default value if KINDERGARTEN_API_PATH is not set. Defaults to None.

        Returns:
            str: The kindergarten API path or the default value.
        """
        return os.getenv("KINDERGARTEN_API_PATH", default)

    @staticmethod
    def get_home_kitchen_api_path(default: str = None) -> str:
        """
        Get the home kitchen API path from environment variables.

        Args:
            default (str, optional): Default value if HOME_KITCHEN_API_PATH is not set. Defaults to None.

        Returns:
            str: The home kitchen API path or the default value.
        """
        return os.getenv("HOME_KITCHEN_API_PATH", default)

    @staticmethod
    def get_llm_provider(default: str = None) -> str:
        """
        Get the LLM provider name from environment variables.

        Args:
            default (str, optional): Default value if LLM_PROVIDER is not set. Defaults to None.

        Returns:
            str: The LLM provider name or the default value.
        """
        return os.getenv("LLM_PROVIDER", default)
