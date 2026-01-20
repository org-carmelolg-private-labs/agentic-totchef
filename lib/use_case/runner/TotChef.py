from lib.adapters.outbound.LLMExecutor import LLMExecutor
from lib.use_case.prompts.HomeMenuPrompt import GenerateHomeMenuPrompt
from lib.use_case.prompts.KindergartenMenuPrompt import GetKindergartenMenuPrompt
from lib.use_case.prompts.MergeMenuPrompt import MergeMenuPrompt
from lib.use_case.prompts.WeekendMenuPrompt import WeekendMenuPrompt
from lib.use_case.tools import KindergartenTools, HomeKitchenTools

llm_executor = LLMExecutor.get_instance()

kindergarten_menu_prompt = GetKindergartenMenuPrompt.get_instance()
home_menu_prompt = GenerateHomeMenuPrompt.get_instance()
merge_menu_prompt = MergeMenuPrompt.get_instance()
weekend_menu_prompt = WeekendMenuPrompt.get_instance()


class TotChef:
    """
    TotChef class that provides culinary and nutritional assistance
    using functions from KindergartenTools and HomeKitchenTools.
    """

    @staticmethod
    def run():
        print("Generating Kindergarten Menu for Week 1 Morning...")
        first_workweek_menu_morning = llm_executor.chat(
            prompt=kindergarten_menu_prompt.get_user_prompt(1),
            system_prompt=kindergarten_menu_prompt.get_system_prompt(),
            chatbot_mode=False,
            tools=KindergartenTools.available_functions()).message.content
        # TotChef.log_element(first_workweek_menu_morning)

        print("Generating Home Menu for Week 1 Evening...")
        first_workweek_menu_evening = llm_executor.chat(
            prompt=home_menu_prompt.get_user_prompt(first_workweek_menu_morning),
            system_prompt=home_menu_prompt.get_system_prompt(),
            chatbot_mode=False,
            tools=HomeKitchenTools.available_functions()).message.content

        # TotChef.log_element(first_workweek_menu_evening)

        print("Union of Morning and Evening Menus for Week 1...")
        workday_full_menu = llm_executor.ask(
            prompt=merge_menu_prompt.get_user_prompt(first_workweek_menu_morning, first_workweek_menu_evening),
            chatbot_mode=False).message.content

        # TotChef.log_element(workday_full_menu)

        print("Generating Full Week Menu...")
        full_week_menu = llm_executor.chat(
            prompt=weekend_menu_prompt.get_user_prompt(workday_full_menu),
            system_prompt=weekend_menu_prompt.get_system_prompt(),
            chatbot_mode=False,
            tools=HomeKitchenTools.available_functions()).message.content

        TotChef.log_element(full_week_menu)

        # TODO generate an adeguate prompt for shopping list. This is for testing purpose only
        # shopping_list = llm_executor.ask(
        #     prompt=f"Generami una lista della spesa divisa per categoria di prodotto in base al menu in input: {full_week_menu}",
        #     chatbot_mode=False).message.content
        # TotChef.log_element(shopping_list)

    @staticmethod
    def log_element(string: str):
        print(string)
        print()
        print('-----------------------------------')
        print()
