"""
TotChefChatbot Module

This module provides the TotChefChatbot class, which implements an interactive chatbot
for culinary and nutritional assistance. It supports both command-line and GUI interfaces,
integrating tools from KindergartenTools and HomeKitchenTools.
"""

from lib.adapters.outbound.LLMExecutor import LLMExecutor
from lib.use_case.tools import KindergartenTools, HomeKitchenTools
from html_sanitizer import Sanitizer
from nicegui import ui

class TotChefChatbot:
    """
    TotChef Chatbot class that provides an interactive chat interface
    for culinary and nutritional assistance using functions from
    KindergartenTools and HomeKitchenTools.
    """
    def __init__(self):
        """
        Initialize the TotChefChatbot instance.

        Sets up the LLM executor and combines available functions from
        KindergartenTools and HomeKitchenTools.
        """
        self.llm_executor = LLMExecutor.get_instance()
        self.tools = {}
        self.tools.update(KindergartenTools.available_functions())
        self.tools.update(HomeKitchenTools.available_functions())

    def run(self):
        """
        Run an interactive chatbot session for TotChef in the command line.

        The chatbot utilizes functions from KindergartenTools and HomeKitchenTools
        to assist users with culinary and nutritional queries. Type 'exit' or 'quit'
        to end the session.
        """
        print("Welcome to TotChef Chat! Type 'exit' or 'quit' to end the chat.")

        # Start chat
        while True:
            user_prompt = input('\nUser > ')
            if user_prompt.lower() in ['exit', 'quit']:
                break
            else:
                print('Assistant >', end=' ')
                stream = self._chat(user_prompt)
                # print the response from the chatbot in real-time
                for chunk in stream:
                    print(chunk['message']['content'], end='', flush=True)

    def _chat(self, user_prompt: str):
        """
        Chat with the TotChef chatbot using the provided user prompt.

        This method integrates functions from KindergartenTools and HomeKitchenTools
        to enhance the chatbot's capabilities.

        Args:
            user_prompt (str): The prompt or question from the user.

        Returns:
            A stream of responses from the chatbot.
        """
        return self.llm_executor.chat(prompt=user_prompt, tools=self.tools)

    def _root(self):
        """
        Define the GUI layout and behavior for the TotChef chatbot.

        This method sets up the chat interface, including message display and input handling.
        It is used internally by the gui method.
        """
        async def send() -> None:
            question = text.value
            text.value = ''
            with message_container:
                ui.chat_message(text=question, name='You', sent=True)
                response_message = ui.chat_message(name='Nutritionist', sent=False)
                spinner = ui.spinner(type='dots', size='lg', color='primary')

            await ui.run_javascript('window.scrollTo(0, document.body.scrollHeight)')
            response = ''
            for chunk in self._chat(question):
                response += chunk['message']['content']
                with response_message.clear():
                    ui.html(response, sanitize=Sanitizer().sanitize)
                    await ui.run_javascript('window.scrollTo(0, document.body.scrollHeight)')
            message_container.remove(spinner)

        message_container = ui.column().classes('w-full max-w-2xl mx-auto flex-grow items-stretch')

        with (ui.footer().classes('bg-white'), ui.column().classes('w-full max-w-3xl mx-auto my-6')):
            with ui.row().classes('w-full no-wrap items-center'):
                placeholder = 'Message'
                text = ui.input(placeholder=placeholder).props('rounded outlined input-class=mx-3').classes('w-full self-center').on('keydown.enter', send)
                button = ui.button(text="Send", color="primary", on_click=send).props('rounded outlined input-class=mx-3').classes('self-center')

            ui.markdown('Made with 🔥 by [carmelolg](https://carmelolg.github.io)') \
                .classes('text-xs self-center mr-12 m-[-1em] text-primary') \
                .classes('[&_a]:text-inherit [&_a]:no-underline [&_a]:font-medium')

    def gui(self):
        """
        Launch the GUI for the TotChef chatbot.

        This method initializes the user interface and starts the event loop.
        """
        ui.run(self._root, title='Agentic TotChef', favicon='', show_welcome_message=True, reconnect_timeout=60)
