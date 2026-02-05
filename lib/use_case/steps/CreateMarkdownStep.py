import uuid
from datetime import datetime, timezone
from lib.use_case.steps.AbstractStep import AbstractStep
from lib.use_case.steps.StepResult import StepResult
import pathlib


class CreateMarkdownStep(AbstractStep):
    """Create a markdown file containing the full menu and shopping list.

    The file is written under the project's `static/` directory with a timestamped filename.
    """

    def __init__(self):
        self.step_id = uuid.uuid4()

    def execute(self, full_menu: str, shopping_list: str) -> StepResult:
        """Write markdown file and return StepResult with the filepath as result.

        Args:
            full_menu: The merged weekly menu as a string.
            shopping_list: The shopping list as a string.

        Returns:
            StepResult containing the created file path in `result` or errors in `errors`.
        """
        sr = StepResult(step_id=self.step_id, result=None)
        try:
            # Determine project root and static dir
            project_root = pathlib.Path(__file__).resolve().parents[3]
            static_dir = project_root / "static"
            static_dir.mkdir(parents=True, exist_ok=True)

            timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
            filename = f"menu_shopping_{timestamp}.md"
            file_path = static_dir / filename

            content_lines = [
                f"# Weekly Menu and Shopping List\n",
                "## Menu\n",
                full_menu or "(no menu provided)",
                "## Shopping List\n",
                "```",
                shopping_list or "(no shopping list provided)",
                "```\n",
            ]

            file_path.write_text("\n".join(content_lines), encoding="utf-8")

            sr.result = str(file_path)
            sr.message = f"Markdown file created at {file_path}"
        except Exception as e:
            sr.add_error(str(e))
        return sr
