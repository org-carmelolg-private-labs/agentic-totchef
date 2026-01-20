from abc import ABC, abstractmethod


class PromptManager(ABC):
    """
    Abstract base class for managing prompts.
    Defines the interface for getting user and system prompts.
    """
    @abstractmethod
    def get_user_prompt(self, *args):
        """
        Get the user prompt based on provided arguments.
        :param args:
        :return:
        """
        pass

    @abstractmethod
    def get_system_prompt(self, *args):
        """
        Get the system prompt based on provided arguments.
        :param args:
        :return:
        """
        pass