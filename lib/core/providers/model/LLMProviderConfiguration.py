"""
LLMProviderConfiguration Module

This module defines the ProviderConfiguration class, which encapsulates configuration settings
for LLM providers, such as streaming mode and thinking mode. It includes a builder function
for creating default configurations.
"""

def ProviderConfigurationBuilder():
    """
    Create a default ProviderConfiguration instance.

    Returns:
        ProviderConfiguration: A new ProviderConfiguration with stream=False and think=False.
    """
    return ProviderConfiguration(stream=False, think=False)

class ProviderConfiguration:
    """
    Configuration class for LLM provider settings.

    This class holds configuration options for interacting with LLM providers, including
    whether to enable streaming responses and thinking mode. It uses private attributes
    and provides fluent setter methods for building configurations.

    Attributes:
        __stream (bool): Indicates if streaming mode is enabled.
        __think (bool): Indicates if thinking mode is enabled.
    """

    __stream: bool
    __think: bool

    def __init__(self, stream: bool, think: bool):
        """
        Initialize a ProviderConfiguration instance.

        Args:
            stream (bool): Whether to enable streaming mode.
            think (bool): Whether to enable thinking mode.
        """
        self.__stream = stream
        self.__think = think

    def stream(self, stream: bool):
        """
        Set the streaming mode.

        Args:
            stream (bool): True to enable streaming, False otherwise.

        Returns:
            ProviderConfiguration: Self for method chaining.
        """
        self.__stream = stream
        return self

    def get_stream(self):
        """
        Get the current streaming mode setting.

        Returns:
            bool: True if streaming is enabled, False otherwise.
        """
        return self.__stream

    def think(self, think: bool):
        """
        Set the thinking mode.

        Args:
            think (bool): True to enable thinking mode, False otherwise.

        Returns:
            ProviderConfiguration: Self for method chaining.
        """
        self.__think = think
        return self

    def get_think(self):
        """
        Get the current thinking mode setting.

        Returns:
            bool: True if thinking mode is enabled, False otherwise.
        """
        return self.__think

    def build(self):
        """
        Build and return the configuration instance.

        Since this class is already the configuration object, this method simply returns self.
        It is provided for consistency with builder patterns.

        Returns:
            ProviderConfiguration: The current instance.
        """
        return self