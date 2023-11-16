

class Zone:

    def __init__(self, Code, Name):
        self.__code = Code
        self.__name = Name

    @property
    def code(self):
        return self.__code
    
    @property
    def name(self):
        return self.__name