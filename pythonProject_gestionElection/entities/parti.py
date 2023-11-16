
class Parti:

    def __init__(self, Id, Name):
        self.__id = Id
        self.__name = Name

    @property
    def id(self):
        return self.__id
    
    @property
    def name(self):
        return self.__name
        