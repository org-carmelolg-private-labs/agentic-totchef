"""
TotChef runner using step classes for each phase.
"""
from concurrent.futures import ProcessPoolExecutor
from lib.use_case.steps.KindergartenMenuStep import KindergartenMenuStep
from lib.use_case.steps.HomeMenuStep import HomeMenuStep
from lib.use_case.steps.MergeMenuStep import MergeMenuStep
from lib.use_case.steps.ShoppingListStep import ShoppingListStep
from lib.use_case.steps.StepResult import StepResult
from lib.use_case.steps.CreateMarkdownStep import CreateMarkdownStep


class TotChef:
    """
    TotChef class that provides culinary and nutritional assistance
    using functions from KindergartenTools and HomeKitchenTools.
    """

    @staticmethod
    def run():
        """
        Run the TotChef workflow to generate menus and shopping lists.

        This method executes the following steps in sequence:
        1. Generate kindergarten menu (parallel with step 2).
        2. Generate home menu (parallel with step 1).
        3. Merge the two menus.
        4. Generate a shopping list from the merged menu.
        5. Create a Markdown file containing the merged menu and shopping list.

        The first two steps are executed in parallel using ProcessPoolExecutor.
        Results are logged after each step.
        """

        # Step 1: Kindergarten menu
        kg_step = KindergartenMenuStep()
        kg_step_output: StepResult = StepResult(step_id=kg_step.step_id, result="")
        # Step 2: Home menu
        home_step = HomeMenuStep()
        home_step_output = StepResult(step_id=home_step.step_id, result="")

        # Execute both steps in parallel
        with ProcessPoolExecutor() as executor:
            futures = [
                executor.submit(kg_step.execute),
                executor.submit(home_step.execute)
            ]

            for future in futures:
                single_result = future.result()
                if single_result is not None and single_result.is_success():
                    if single_result.step_id == kg_step.step_id:
                        kg_step_output: StepResult = single_result
                    elif single_result.step_id == home_step.step_id:
                        home_step_output: StepResult = single_result

        # Step 3: Merge menus
        merge_step = MergeMenuStep()
        merge_step_output: StepResult = merge_step.execute(kg_step_output.result, home_step_output.result)

        # Step 4: Shopping list
        shopping_list_step = ShoppingListStep()
        shopping_list_output: StepResult = shopping_list_step.execute(merge_step_output.result)

        # Add step that create a Markdown file with the merged menu and shopping list
        create_md_step = CreateMarkdownStep()
        create_md_output: StepResult = create_md_step.execute(merge_step_output.result, shopping_list_output.result)
        if create_md_output is not None and create_md_output.is_success():
            TotChef.log_element(f"Markdown created: {create_md_output.result}")
        else:
            TotChef.log_element("Failed to create markdown file")

    @staticmethod
    def log_element(string: str):
        """
        Log an element with separators.

        Prints the given string followed by a blank line and a separator line.

        Args:
            string (str): The string to log.
        """
        print(string)
        print()
        print('-----------------------------------')
        print()
