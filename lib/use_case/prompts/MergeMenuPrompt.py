from lib.use_case.prompts.PromptManager import PromptManager


class MergeMenuPrompt(PromptManager):
    """
    This module provides utility functions to generate system prompts for merging two weekly menus.
    """
    __instance = None

    @staticmethod
    def get_instance():
        if MergeMenuPrompt.__instance is None:
            MergeMenuPrompt()
        return MergeMenuPrompt.__instance

    def __init__(self):
        if MergeMenuPrompt.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            MergeMenuPrompt.__instance = self

    def get_system_prompt(self):
        prompt = f"""
        """

        return prompt

    def get_user_prompt(self, morning_menu: str, evening_menu: str):
        prompt = f"""
        Unisci i seguenti due menu settimanali (mattina e sera) in un unico menu settimanale completo, 
        mantenendo la distinzione tra i pasti della mattina e quelli della sera.
        
        Menu della mattina:
        {morning_menu}
        Menu della sera:
        {evening_menu}
        
        Formatta il risultato in modo chiaro e strutturato, senza testo aggiuntivo
        
        Output richiesto:
        una tabella in formato markdown con le seguenti colonne:
        - Giorno
        - Mattino
        - Sera
        
        Il contenuto delle celle deve essere:  
        - Giorno: [Lunedì, Martedì, Mercoledì, Giovedì, Venerdì]
        - Mattino: [Primo: piatto menu nido 1, Secondo: piatto menu nido 2, Contorno: piatto menu nido 3]
        - Sera: [Primo: piatto menu casa 1, Secondo: piatto menu casa 2, Contorno: piatto menu casa 3]
        
        Aggiungi un a capo tra i pasti (Primo, Secondo, Contorno) all'interno delle celle.
        """
        return prompt