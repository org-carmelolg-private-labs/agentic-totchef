from concurrent.futures import ThreadPoolExecutor

from lib.adapters.outbound.LLMExecutor import LLMExecutor
from lib.use_case.prompts.HomeMenuPrompt import GenerateHomeMenuPrompt
from lib.use_case.prompts.KindergartenMenuPrompt import GetKindergartenMenuPrompt
from lib.use_case.prompts.MergeMenuPrompt import MergeMenuPrompt
from lib.use_case.prompts.ShoppingListPrompt import ShoppingListPrompt
from lib.use_case.tools import KindergartenTools, HomeKitchenTools

llm_executor = LLMExecutor.get_instance()

kindergarten_menu_prompt = GetKindergartenMenuPrompt()
home_menu_prompt = GenerateHomeMenuPrompt()
merge_menu_prompt = MergeMenuPrompt()
shopping_list_prompt = ShoppingListPrompt()


class TotChef:
    """
    TotChef class that provides culinary and nutritional assistance
    using functions from KindergartenTools and HomeKitchenTools.
    """

    @staticmethod
    def run():
        print("Generating Kindergarten Menu for Week 1...")
        kindergarten_menu = llm_executor.chat(
            prompt=kindergarten_menu_prompt.get_user_prompt(1),
            chatbot_mode=False,
            tools=KindergartenTools.available_functions(),
            system_prompt=kindergarten_menu_prompt.get_system_prompt()).message.content
        TotChef.log_element(kindergarten_menu)

        print("Generating Home Menu for Week 1...")
        home_menu = llm_executor.chat(
            prompt=home_menu_prompt.get_user_prompt(),
            system_prompt=home_menu_prompt.get_system_prompt(),
            chatbot_mode=False,
            tools=HomeKitchenTools.available_functions()).message.content

        TotChef.log_element(home_menu)

        print("Merging all menus...")
        full_menu = llm_executor.ask(
            prompt=merge_menu_prompt.get_user_prompt(kindergarten_menu, home_menu),
            chatbot_mode=False).message.content

        TotChef.log_element(full_menu)

        # print("Generating Shopping List...")
        # shopping_list = llm_executor.ask(
        #     prompt=shopping_list_prompt.get_user_prompt(full_menu),
        #     system_prompt=shopping_list_prompt.get_system_prompt(),
        #     chatbot_mode=False).message.content
        #
        # TotChef.log_element(shopping_list)

    @staticmethod
    def log_element(string: str):
        print(string)
        print()
        print('-----------------------------------')
        print()
