from lib.adapters.outbound.LLMExecutor import LLMExecutor
from lib.use_case.prompts.GenerateHomeMenuPrompt import GenerateHomeMenuPrompt
from lib.use_case.prompts.GetKindergartenMenuPrompt import GetKindergartenMenuPrompt
from lib.use_case.tools import KindergartenTools, HomeKitchenTools

llm_executor = LLMExecutor.get_instance()

class TotChef:
    """
    TotChef class that provides culinary and nutritional assistance
    using functions from KindergartenTools and HomeKitchenTools.
    """

    @staticmethod
    def run_chain():
        _functions = {}
        _functions.update(KindergartenTools.available_functions())
        _functions.update(HomeKitchenTools.available_functions())

        week_1_user_prompt_morning = GetKindergartenMenuPrompt.get_user_prompt(1)
        week_1_system_prompt_morning = GetKindergartenMenuPrompt.get_system_prompt()

        week_1_menu_morning = llm_executor.chat(prompt=week_1_user_prompt_morning, system_prompt=week_1_system_prompt_morning, chatbot_mode=False, tools=_functions).message.content

        week_1_user_prompt_evening = GenerateHomeMenuPrompt.get_user_prompt(week_1_menu_morning)
        week_1_system_prompt_evening = GenerateHomeMenuPrompt.get_system_prompt()

        week_1_menu_evening = llm_executor.chat(prompt=week_1_user_prompt_evening, system_prompt=week_1_system_prompt_evening,
                                        chatbot_mode=False, tools=_functions).message.content

        print(week_1_menu_morning)
        print("********************")
        print(week_1_menu_evening)


    @staticmethod
    def run():
        """
        Run a TotChef session that utilizes functions from
        KindergartenTools and HomeKitchenTools to assist users
        with culinary and nutritional queries.
        :return:
        """
        user_prompt = "Dammi le ricette casalinghe a base di verdure?"
        # user_prompt = "Dammi il menu di martedì della seconda settimana del nido"

        _functions = {}
        _functions.update(KindergartenTools.available_functions())
        _functions.update(HomeKitchenTools.available_functions())

        first_response = llm_executor.chat(prompt=user_prompt, chatbot_mode=False, tools=_functions).message.content

        print(first_response)
        print('************************')

        second_response = llm_executor.ask(prompt=first_response,
                                          system_prompt="Ti è stato consegnata una lista di verdure. Restituisci solo quelle con il nome che inizia per C",
                                          chatbot_mode=False).message.content

        print(second_response)

        # for chunk in stream:
        #    print(chunk['message']['content'], end='', flush=True)
