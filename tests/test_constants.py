"""
Unit tests for lib.commons.Constants.

Verifies that the singleton pattern still works correctly after converting
get_instance() from @staticmethod to @classmethod.
"""

import pytest
from lib.commons.Constants import Constants


class TestConstants:
    def test_get_instance_returns_instance(self):
        instance = Constants.get_instance()
        assert instance is not None
        assert isinstance(instance, Constants)

    def test_get_instance_is_singleton(self):
        instance1 = Constants.get_instance()
        instance2 = Constants.get_instance()
        assert instance1 is instance2

    def test_singleton_raises_on_direct_instantiation(self):
        # A second direct instantiation must raise because the singleton already exists
        with pytest.raises(Exception, match="singleton"):
            Constants()

    def test_llm_provider_ollama_constant(self):
        instance = Constants.get_instance()
        assert instance.llm_provider_ollama == "ollama"
