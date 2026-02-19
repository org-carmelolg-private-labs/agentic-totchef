"""
Agentic TotChef Entry Point

This script serves as the main entry point for the Agentic TotChef application.
It runs the TotChef workflow to generate menus and shopping lists using LLM and tools.
"""

from lib.use_case.runner.TotChef import run

# RUN
if __name__ == "__main__":
    run()
