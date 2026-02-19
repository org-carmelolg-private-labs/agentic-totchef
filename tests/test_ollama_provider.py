"""
Unit tests for lib.core.providers.OllamaProvider.

Verifies that the singleton pattern still works correctly after converting
get_instance() from @staticmethod to @classmethod.
"""

import pytest
from lib.core.providers.OllamaProvider import OllamaProvider


class TestOllamaProvider:
    def test_get_instance_returns_same_instance(self):
        instance1 = OllamaProvider.get_instance()
        instance2 = OllamaProvider.get_instance()
        assert instance1 is instance2
        assert isinstance(instance1, OllamaProvider)

    def test_get_instance_is_not_none(self):
        instance = OllamaProvider.get_instance()
        assert instance is not None
