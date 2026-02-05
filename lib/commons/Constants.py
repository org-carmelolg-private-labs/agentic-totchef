"""
Constants Module

This module defines a singleton Constants class that holds application-wide constant values.
It ensures that only one instance of the class exists, providing a centralized place for constants.

Currently, it defines the LLM provider name for Ollama.
"""

class Constants(object):
    """
    Singleton class for storing application constants.

    This class provides a centralized location for constant values used throughout the application.
    It follows the singleton pattern to ensure consistency and prevent multiple instances.

    Attributes:
        llm_provider_ollama (str): The string identifier for the Ollama LLM provider.
    """

    llm_provider_ollama = "ollama"

    __instance = None

    @staticmethod
    def get_instance():
        """
        Get the singleton instance of Constants.

        Returns:
            Constants: The singleton instance of the Constants class.
        """
        if Constants.__instance is None:
            Constants()
        return Constants.__instance

    def __init__(self):
        """
        Initialize the singleton instance of Constants.

        Raises:
            Exception: If an instance of Constants already exists (singleton violation).
        """
        if Constants.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Constants.__instance = self