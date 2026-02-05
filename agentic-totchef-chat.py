"""
Agentic TotChef Chat Entry Point

This script serves as the main entry point for the Agentic TotChef chatbot application.
It launches an interactive command-line chatbot for culinary and nutritional assistance.
"""

from lib.use_case.runner.TotChefChatbot import TotChefChatbot

if __name__ == "__main__":
    chatbot = TotChefChatbot()
    chatbot.run()