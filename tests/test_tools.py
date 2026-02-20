"""
Unit tests for lib.use_case.tools.HomeKitchenTools and lib.use_case.tools.KindergartenTools.
"""

from unittest.mock import patch, MagicMock
import lib.use_case.tools.HomeKitchenTools as hkt
import lib.use_case.tools.KindergartenTools as kgt


class TestHomeKitchenTools:
    def test_available_functions_returns_dict(self):
        funcs = hkt.available_functions()
        assert "get_home_kitchen_recipes" in funcs
        assert "get_home_kitchen_recipes_by_category" in funcs

    def test_get_home_kitchen_recipes_returns_data(self):
        recipes = {"carbohydrates": ["pasta"]}
        with patch("lib.use_case.tools.HomeKitchenTools.HomeKitchenHttpService") as mock_svc_cls:
            mock_svc = mock_svc_cls.return_value
            mock_svc.get_available_recipes.return_value = recipes
            result = hkt.get_home_kitchen_recipes()
        assert result == recipes

    def test_get_home_kitchen_recipes_returns_not_found_when_empty(self):
        with patch("lib.use_case.tools.HomeKitchenTools.HomeKitchenHttpService") as mock_svc_cls:
            mock_svc = mock_svc_cls.return_value
            mock_svc.get_available_recipes.return_value = None
            result = hkt.get_home_kitchen_recipes()
        assert result == {"result": "Not found"}

    def test_get_home_kitchen_recipes_by_category_returns_category(self):
        recipes = {"carbohydrates": ["pasta"], "proteins": ["chicken"]}
        best_match = {"match": "carbohydrates", "similarity": 0.95}
        with patch("lib.use_case.tools.HomeKitchenTools.HomeKitchenHttpService") as mock_svc_cls:
            mock_svc = mock_svc_cls.return_value
            mock_svc.get_available_recipes.return_value = recipes
            with patch("lib.use_case.tools.HomeKitchenTools.get_best_matching_chunk", return_value=best_match):
                result = hkt.get_home_kitchen_recipes_by_category("carb")
        assert result == ["pasta"]

    def test_get_home_kitchen_recipes_by_category_low_similarity(self):
        recipes = {"carbohydrates": ["pasta"]}
        low_match = {"match": "carbohydrates", "similarity": 0.5}
        with patch("lib.use_case.tools.HomeKitchenTools.HomeKitchenHttpService") as mock_svc_cls:
            mock_svc = mock_svc_cls.return_value
            mock_svc.get_available_recipes.return_value = recipes
            with patch("lib.use_case.tools.HomeKitchenTools.get_best_matching_chunk", return_value=low_match):
                result = hkt.get_home_kitchen_recipes_by_category("xyz")
        assert result == {"result": "Not found"}

    def test_get_home_kitchen_recipes_by_category_no_recipes(self):
        with patch("lib.use_case.tools.HomeKitchenTools.HomeKitchenHttpService") as mock_svc_cls:
            mock_svc = mock_svc_cls.return_value
            mock_svc.get_available_recipes.return_value = None
            result = hkt.get_home_kitchen_recipes_by_category("carb")
        assert result == {"result": "Not found"}

    def test_get_home_kitchen_recipes_by_category_no_best_match(self):
        recipes = {"carbohydrates": ["pasta"]}
        with patch("lib.use_case.tools.HomeKitchenTools.HomeKitchenHttpService") as mock_svc_cls:
            mock_svc = mock_svc_cls.return_value
            mock_svc.get_available_recipes.return_value = recipes
            with patch("lib.use_case.tools.HomeKitchenTools.get_best_matching_chunk", return_value=None):
                result = hkt.get_home_kitchen_recipes_by_category("xyz")
        assert result == {"result": "Not found"}


class TestKindergartenTools:
    def test_available_functions_returns_dict(self):
        funcs = kgt.available_functions()
        assert "get_kindergarten_menu" in funcs

    def test_get_kindergarten_menu_returns_week_data(self):
        menu = {"week": {"1": {"monday": "pasta"}}}
        with patch("lib.use_case.tools.KindergartenTools.KindergartenHttpService") as mock_svc_cls:
            mock_svc = mock_svc_cls.return_value
            mock_svc.get_current_menu.return_value = menu
            result = kgt.get_kindergarten_menu(week=1)
        assert result == {"monday": "pasta"}

    def test_get_kindergarten_menu_returns_not_found_when_empty(self):
        with patch("lib.use_case.tools.KindergartenTools.KindergartenHttpService") as mock_svc_cls:
            mock_svc = mock_svc_cls.return_value
            mock_svc.get_current_menu.return_value = None
            result = kgt.get_kindergarten_menu(week=1)
        assert result == {"result": "Not found"}
