"""
Service module to interact with the Kindergarten API.
"""
from typing import Any
import requests, json, os
from datetime import date
from lib.utils.EnvironmentVariables import EnvironmentVariables

env = EnvironmentVariables()

def get_current_menu() -> Any | None:
    """
    Redirects to the correct menu based on current month:
    - November (11) to April (4) -> winter menu
    - May (5) to October (10) -> summer menu
    """
    month = date.today().month
    if month >= 11 or month <= 4:
        return get_winter_menu()
    return get_summer_menu()

def get_winter_menu() -> Any | None:
    """
    Makes a GET request to the Kindergarten API to retrieve winter menu.
    :return:
    """
    menu = _get()
    if menu is None:
        with open('static/kindergarten-winter-menu.json') as json_file:
            return json.load(json_file)
    return None


def get_summer_menu() -> Any | None:
    """
    Makes a GET request to the Kindergarten API to retrieve summer menu.
    :return:
    """
    menu = _get()
    if menu is None:
        with open('static/kindergarten-summer-menu.json') as json_file:
            return json.load(json_file)
    return None


def _get(base_url: str = env.get_kindergarten_api_host(), endpoint: str =env.get_kindergarten_api_path()) -> Any | None:
    """
    Makes a GET request to the Kindergarten API.

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
