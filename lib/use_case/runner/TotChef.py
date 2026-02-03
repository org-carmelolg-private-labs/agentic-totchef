from lib.adapters.outbound.LLMExecutor import LLMExecutor
from lib.use_case.prompts.CheckerMenuPrompt import CheckerMenuPrompt
from lib.use_case.prompts.HomeMenuPrompt import GenerateHomeMenuPrompt
from lib.use_case.prompts.KindergartenMenuPrompt import GetKindergartenMenuPrompt
from lib.use_case.prompts.MergeMenuPrompt import MergeMenuPrompt
from lib.use_case.prompts.ShoppingListPrompt import ShoppingListPrompt
from lib.use_case.tools import KindergartenTools, HomeKitchenTools
from lib.use_case.runner.MenuChecker import MenuChecker

llm_executor = LLMExecutor.get_instance()

kindergarten_menu_prompt = GetKindergartenMenuPrompt()
home_menu_prompt = GenerateHomeMenuPrompt()
merge_menu_prompt = MergeMenuPrompt()
shopping_list_prompt = ShoppingListPrompt()
checker_menu_prompt = CheckerMenuPrompt()


class TotChef:
    """
    TotChef class that provides culinary and nutritional assistance
    using functions from KindergartenTools and HomeKitchenTools.
    """

    @staticmethod
    def run():
        # print("Generating Kindergarten Menu for Week 1...")
        # kindergarten_menu = llm_executor.chat(
        #     prompt=kindergarten_menu_prompt.get_user_prompt(1),
        #     chatbot_mode=False,
        #     tools=KindergartenTools.available_functions(),
        #     system_prompt=kindergarten_menu_prompt.get_system_prompt()).message.content
        # TotChef.log_element(kindergarten_menu)
        #
        # print("Generating Home Menu for Week 1...")
        # home_menu = llm_executor.chat(
        #     prompt=home_menu_prompt.get_user_prompt(),
        #     system_prompt=home_menu_prompt.get_system_prompt(),
        #     chatbot_mode=False,
        #     tools=HomeKitchenTools.available_functions()).message.content
        #
        # TotChef.log_element(home_menu)
        #
        # print("Merging all menus...")
        # full_menu = llm_executor.ask(
        #     prompt=merge_menu_prompt.get_user_prompt(kindergarten_menu, home_menu),
        #     chatbot_mode=False).message.content
        #
        # TotChef.log_element(full_menu)

        full_menu = """
        | Giorno      | Mattino                                                                 | Sera                                                                 |
        |-------------|------------------------------------------------------------------------|----------------------------------------------------------------------|
        | Lunedì      |                                                                      | Primo: Pasta al pomodoro<br>Secondo: Fettina di carne<br>Contorno: Broccoli |
        | Martedì     |                                                                      | Primo: Riso sugo e piselli<br>Secondo: Straccetti di pollo<br>Contorno: Carote |
        | Mercoledì   |                                                                      | Primo: Pasta al cavolo nero<br>Secondmente: Polpette di carne<br>Contorno: Zucchine |
        | Giovedì     |                                                                      | Primo: Pasta al ragù<br>Secondo: Orata in friggitrice ad aria<br>Contorno: Spinaci |
        | Venerdì     |                                                                      | Primo: Pasta e lenticchie<br>Secondo: Nasello con carote in padella<br>Contorno: Fagiolini |
        | Sabato      | Primo: Pasta al pesto<br>Secondo: Polpette di ceci<br>Contorno: Cavolfiore | Primo: Pasta alla zucca<br>Secondo: Philadelphia<br>Contorno: Costine |
        | Domenica    | Primo: Pasta alla crema di ceci<br>Secondo: Polpette di fagioli<br>Contorno: Pak Choi | Primo: Pasta alla crema di fagioli<br>Secondo: Formaggio fresco<br>Contorno: Verza |
        """

        checked_menu = llm_executor.chat(
            prompt=checker_menu_prompt.get_user_prompt(full_menu),
            system_prompt=checker_menu_prompt.get_system_prompt(),
            chatbot_mode=False,
            tools=HomeKitchenTools.available_functions()
        ).message.content

        TotChef.log_element(checked_menu)


    @staticmethod
    def log_element(string: str):
        print(string)
        print()
        print('-----------------------------------')
        print()
