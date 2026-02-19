import uuid
from lib.adapters.outbound.LLMExecutor import chat
from lib.use_case.prompts.KindergartenMenuPrompt import GetKindergartenMenuPrompt
from lib.use_case.steps.AbstractStep import AbstractStep
from lib.use_case.steps.StepResult import StepResult
from lib.use_case.tools import KindergartenTools

kindergarten_menu_prompt = GetKindergartenMenuPrompt()


class KindergartenMenuStep(AbstractStep):

    def __init__(self):
        self.step_id = uuid.uuid4()

    def execute(self) -> StepResult:
        print("Generating Kindergarten Menu for Week 1...")
        kindergarten_menu = chat(
            prompt=kindergarten_menu_prompt.get_user_prompt(1),
            chatbot_mode=False,
            tools=KindergartenTools.available_functions(),
            system_prompt=kindergarten_menu_prompt.get_system_prompt()).message.content

        return StepResult(step_id=self.step_id,
                          result=kindergarten_menu)