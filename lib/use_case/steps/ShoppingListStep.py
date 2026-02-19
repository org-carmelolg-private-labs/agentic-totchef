import uuid
from lib.use_case.steps.AbstractStep import AbstractStep
from lib.use_case.steps.StepResult import StepResult

from lib.adapters.outbound.LLMExecutor import ask
from lib.use_case.prompts.ShoppingListPrompt import ShoppingListPrompt

shopping_list_prompt = ShoppingListPrompt()


class ShoppingListStep(AbstractStep):

    def __init__(self):
        self.step_id = uuid.uuid4()

    def execute(self, full_menu: str) -> StepResult:
        print("Generating Shopping List...")
        shopping_list = ask(
            prompt=shopping_list_prompt.get_user_prompt(full_menu),
            system_prompt=shopping_list_prompt.get_system_prompt(),
            chatbot_mode=False,
            disable_think=True
        ).message.content

        return StepResult(step_id=self.step_id,
                          result=shopping_list)
