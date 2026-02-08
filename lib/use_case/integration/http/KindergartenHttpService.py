"""
Service module to interact with the Kindergarten API.

This module exposes `KindergartenHttpService` which inherits from
`lib.core.integration.http.GenericHttpService.GenericHttpService`.
Module-level helper functions were removed; callers should instantiate
`KindergartenHttpService` and call instance methods (e.g. `.get_current_menu()`).
"""
from typing import Any
from datetime import date
from lib.commons.EnvironmentVariables import EnvironmentVariables
from lib.core.integration.http.GenericHttpService import GenericHttpService

env = EnvironmentVariables()


class KindergartenHttpService(GenericHttpService):
    """Service class to interact with the Kindergarten API."""

    def get_current_menu(self) -> Any | None:
        """Return the appropriate menu depending on the current month."""
        month = date.today().month
        if month >= 11 or month <= 4:
            return self.get_winter_menu()
        return self.get_summer_menu()

    def get_winter_menu(self) -> Any | None:
        """Retrieve the winter menu from the Kindergarten API or fallback file."""
        return self.get(
            api_host=env.get_kindergarten_api_host(),
            api_path=env.get_kindergarten_api_path(),
            fallback_path='static/kindergarten-winter-menu.json'
        )

    def get_summer_menu(self) -> Any | None:
        """Retrieve the summer menu from the Kindergarten API or fallback file."""
        return self.get(
            api_host=env.get_kindergarten_api_host(),
            api_path=env.get_kindergarten_api_path(),
            fallback_path='static/kindergarten-summer-menu.json'
        )
