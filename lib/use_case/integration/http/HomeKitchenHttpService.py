"""
Service module for interacting with the Home Kitchen API.
"""
from typing import Any
from lib.commons.EnvironmentVariables import EnvironmentVariables
from lib.use_case.integration.http import GenericHttpService

env = EnvironmentVariables()

def get_available_recipes() -> Any | None:
    """
    Makes a GET request to the Home Kitchen API to retrieve available recipes.

    Returns:
        dict: The JSON response from the API or local file with the same data.
    """
    return GenericHttpService.get(
        api_host=env.get_home_kitchen_api_host(),
        api_path=env.get_home_kitchen_api_path(),
        fallback_path='static/home-kitchen-recipes.json'
    )
