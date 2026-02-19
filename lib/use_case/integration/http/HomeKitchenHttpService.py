"""
Service module for interacting with the Home Kitchen API.

This module exposes `HomeKitchenHttpService` which inherits from
`lib.core.integration.http.GenericHttpService.GenericHttpService`.
Module-level helper functions were removed; callers should instantiate
`HomeKitchenHttpService` and call instance methods (e.g. `.get_available_recipes()`).
"""
from typing import Any
from lib.commons.EnvironmentVariables import get_home_kitchen_api_host, get_home_kitchen_api_path
from lib.core.integration.http.GenericHttpService import GenericHttpService

class HomeKitchenHttpService(GenericHttpService):
    """Service class to interact with the Home Kitchen API.

    Provides methods that wrap the GenericHttpService.get implementation.
    """

    def get_available_recipes(self) -> Any | None:
        """Retrieve available recipes from the Home Kitchen API or fallback file."""
        return self.get(
            api_host=get_home_kitchen_api_host(),
            api_path=get_home_kitchen_api_path(),
            fallback_path='static/home-kitchen-recipes.json'
        )