"""
Service module for interacting with the Home Kitchen API.
"""
from typing import Any
import requests, json
from lib.utils.EnvironmentVariables import EnvironmentVariables

env = EnvironmentVariables()

def get_available_recipes() -> Any | None:
    """
    Makes a GET request to the Home Kitchen API to retrieve available recipes.

    Returns:
        dict: The JSON response from the API or local file with the same data.
    """
    recipes = _get()
    if recipes is None:
        with open('static/home-kitchen-recipes.json') as json_file:
            return json.load(json_file)
    return None


def _get(base_url: str = env.get_home_kitchen_api_host(), endpoint: str =env.get_home_kitchen_api_path()) -> Any | None:
    """
    Makes a GET request to the Home Kitchen API.

    Args:
        base_url (str): The base URL of the API.
        endpoint (str): The endpoint to make the request to.

    Returns:
        dict: The JSON response from the API.
    """

    if base_url and endpoint:
        try:
            # Make the GET request to the API
            response = requests.get(base_url + '/' + endpoint)

            # Check if the response was successful
            response.raise_for_status()

            # Return the JSON response
            return response.json()
        except requests.exceptions.RequestException as e:
            # Handle any exceptions that occur during the request
            # print(f"An error occurred: {e}")
            return None
    return None
