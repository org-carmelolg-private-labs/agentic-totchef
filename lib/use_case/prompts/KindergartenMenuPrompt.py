"""
This module provides utility functions to generate system prompts for an expert assistant.
"""
from lib.use_case.prompts.PromptManager import PromptManager


class GetKindergartenMenuPrompt(PromptManager):
    __instance = None

    @staticmethod
    def get_instance():
        if GetKindergartenMenuPrompt.__instance is None:
            GetKindergartenMenuPrompt()
        return GetKindergartenMenuPrompt.__instance

    def __init__(self):
        if GetKindergartenMenuPrompt.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            GetKindergartenMenuPrompt.__instance = self

    def get_system_prompt(self):
        prompt = f"""
        Agisci come una persona che sta creando un menu completo settimanale. 
        Il tuo compito è recuperare il menu dell’asilo nido, ossia l’elenco dei pasti pianificati (primo, secondo e contorno) per i giorni della settimana.

        Obiettivo:
        Restituire il menu in modo completo, fedele e conciso, senza interpretazioni personali, suggerimenti, commenti o testo aggiuntivo.
        Il risultato deve essere direttamente utilizzabile e privo di elementi superflui.

        Istruzioni operative
            1.	Ricevi dall'assistente e dai tool il menu settimanale diviso per carboidrati, proteine e verdure.
            2.  I carboidrati sono i primi piatti, le proteine i secondi piatti e le verdure i contorni.
            3.	Organizza il menu in base ai giorni della settimana (Lunedì, Martedì, Mercoledì, Giovedì, Venerdì).
            4.	Per ogni giorno, elenca i pasti previsti: Primo, Secondo e Contorno.
            5.	Restituisci il menu in un formato chiaro e strutturato, senza testo aggiuntivo.

        Formato dell'output:
    
            Lunedì
                Primo: [piatto 1]
                Secondo: [piatto 2]
                Contorno: [piatto 3]
            Martedì
                Primo: [piatto 1]
                Secondo: [piatto 2]
                Contorno: [piatto 3]
            ...
        """

        return prompt

    def get_user_prompt(self, week: int):
        prompt = f"""
        Per favore fornisci il menu dell’asilo nido per la settimana {week}.
        """
        return prompt
