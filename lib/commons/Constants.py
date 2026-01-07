
class Constants(object):
    llm_provider_ollama = "ollama"

    __instance = None
    @staticmethod
    def get_instance():
        if Constants.__instance is None:
            Constants()
        return Constants.__instance
    def __init__(self):
        if Constants.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Constants.__instance = self