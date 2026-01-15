def ProviderConfigurationBuilder():
    return ProviderConfiguration(stream=False, think=False)

class ProviderConfiguration:
    __stream: bool
    __think: bool

    def __init__(self, stream: bool, think: bool):
        self.__stream = stream
        self.__think = think

    def stream(self, stream: bool):
        self.__stream = stream
        return self

    def get_stream(self):
        return self.__stream

    def think(self, think: bool):
        self.__think = think
        return self

    def get_think(self):
        return self.__think

    def build(self):
        return self