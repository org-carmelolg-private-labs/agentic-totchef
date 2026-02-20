"""
Unit tests for lib.core.providers.model.LLMProviderConfiguration.
"""

import pytest
from lib.core.providers.model.LLMProviderConfiguration import (
    ProviderConfiguration,
    ProviderConfigurationBuilder,
)


class TestProviderConfiguration:
    def test_init_and_getters(self):
        config = ProviderConfiguration(stream=True, think=False)
        assert config.get_stream() is True
        assert config.get_think() is False

    def test_stream_setter_returns_self(self):
        config = ProviderConfiguration(stream=False, think=False)
        result = config.stream(True)
        assert result is config
        assert config.get_stream() is True

    def test_think_setter_returns_self(self):
        config = ProviderConfiguration(stream=False, think=False)
        result = config.think(True)
        assert result is config
        assert config.get_think() is True

    def test_build_returns_self(self):
        config = ProviderConfiguration(stream=False, think=True)
        assert config.build() is config

    def test_chaining(self):
        config = ProviderConfiguration(stream=False, think=False).stream(True).think(True)
        assert config.get_stream() is True
        assert config.get_think() is True


class TestProviderConfigurationBuilder:
    def test_builder_returns_instance(self):
        config = ProviderConfigurationBuilder()
        assert isinstance(config, ProviderConfiguration)

    def test_builder_defaults(self):
        config = ProviderConfigurationBuilder()
        assert config.get_stream() is False
        assert config.get_think() is False
