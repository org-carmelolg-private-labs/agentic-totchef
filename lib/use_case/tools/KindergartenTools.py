"""
Kindergarten Tools module for retrieving kindergarten menu information.
"""
from lib.use_case.integration.http import KindergartenHttpService

def available_functions() -> dict:
    """
    Returns a dictionary of available functions for kindergarten menu retrieval
    :return: dictionary of functions
    """
    return {
        "get_kindergarten_menu": get_kindergarten_menu
    }

def get_kindergarten_menu(week: int = 1) -> dict:
    """
    Get the kindergarten menu for a specified week
    Args:
      week: The week number (default 1)
    Returns:
        The menu of the kindergarten for the specified week
    """
    menu = KindergartenHttpService.get_current_menu()

    if not menu:
        return {'result': "Not found"}

    return menu["week"].get(str(week), {})
