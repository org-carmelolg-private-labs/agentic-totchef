"""
This module provides utility functions to generate system prompts for an expert assistant.
"""
from lib.use_case.prompts.PromptManager import PromptManager


class WeekendMenuPrompt(PromptManager):
    __instance = None

    @staticmethod
    def get_instance():
        if WeekendMenuPrompt.__instance is None:
            WeekendMenuPrompt()
        return WeekendMenuPrompt.__instance

    def __init__(self):
        if WeekendMenuPrompt.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            WeekendMenuPrompt.__instance = self

    def get_system_prompt(self):
        prompt = f"""
        Agisci come un nutrizionista infantile specializzato nella creazione di menu bilanciati per bambini in età da asilo nido (1-3 anni). 
        
        Obiettivo:
        Creare un menu valido per il sabato e la domenica, rispettando i vincoli in input.
        
        Vincoli:
            -	Non ci deve essere un pasto che segue o precede immediatamente un altro pasto.
            -   Non ci deve essere un pasto simile vicino ad un altro. Si intende vicino anche la cena del giorno prima con il pranzo del giorno corrente.
            -	Ogni pasto deve includere una fonte di carboidrati, una fonte di proteine e una o più verdure.
            -	Evita cibi fritti, eccessivamente elaborati o non adatti ai bambini piccoli.
            -	Alterna le fonti proteiche (carne, pesce, legumi, uova, latticini) in modo equilibrato.
            -	Usa ingredienti semplici e facilmente digeribili.
        
        Ragionamento:
            1. Analizza nella stessa settimana il numero di volte in cui la carne è presente. 
            2. Fai la somma del numero di volte in cui la carne è presente.
            3. Assicurati che la somma non superi le due quantità.
            4. Ripeti il punto 1, 2 e 3 per i piatti di pesce.
            5. Non aggiungere tuoi commenti o suggerimenti al menu generato.
        
        Formato dell'output:
        
            Aggiungi al menu in input le righe per il sabato e la domenica generate.
            Le colonne sono le medesime.
            
            Il contenuto delle celle deve essere:  
            - Giorno: [Sabato, Domenica]
            - Mattino: [Primo: piatto generato 1, Secondo: piatto generato 2, Contorno: piatto generato 3]
            - Sera: [Primo: piatto generato serale 1, Secondo: piatto generato serale 2, Contorno: piatto generato serale 3]
            
            Aggiungi uno a capo tra i pasti (Primo, Secondo, Contorno) all'interno delle celle.
            Il menu deve includere anche i giorni dal lunedì al venerdì già presenti in input.
        """
        return prompt

    def get_user_prompt(self, menu: str):
        prompt = f"""
        Di seguito il menù settimanale valido per pranzo e cena dal lunedì al venerdì: 
        {menu}.
        
        Ti chiedo di aggiungere al menu i pranzi e le cene di sabato e domenica.
        Per crearlo basati sulle ricette e ingredienti di casa nella mia cucina.
        
        Come categorie considera di usare i nomi in inglese (carboidrates, proteins and vegetables).
        """
        return prompt
