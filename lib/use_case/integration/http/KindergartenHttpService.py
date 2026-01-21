"""
Service module to interact with the Kindergarten API.
"""
from typing import Any
from datetime import date
from lib.commons.EnvironmentVariables import EnvironmentVariables
from lib.use_case.integration.http import GenericHttpService

env = EnvironmentVariables()

def get_current_menu() -> Any | None:
    """
    Redirects to the correct menu based on the current month:
    - November (11) to April (4) -> winter menu
    - May (5) to October (10) -> summer menu
    """
    month = date.today().month
    if month >= 11 or month <= 4:
        return get_winter_menu()
    return get_summer_menu()

def get_winter_menu() -> Any | None:
    """
    Makes a GET request to the Kindergarten API to retrieve the winter menu.
    """
    return GenericHttpService.get(
        api_host=env.get_kindergarten_api_host(),
        api_path=env.get_kindergarten_api_path(),
        fallback_path='static/kindergarten-winter-menu.json'
    )

def get_summer_menu() -> Any | None:
    """
    Makes a GET request to the Kindergarten API to retrieve the summer menu.
    """
    return GenericHttpService.get(
        api_host=env.get_kindergarten_api_host(),
        api_path=env.get_kindergarten_api_path(),
        fallback_path='static/kindergarten-summer-menu.json'
    )
