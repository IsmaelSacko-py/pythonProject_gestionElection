from entities.personne import *


# callDB()

class Electeur(Personne):

    def __init__(self, Name, Surname, Nci, Zone):
        super().__init__(Name, Surname)
        self.__nci = Nci
        self.__zone = Zone

    @property
    def nci(self):
        return self.__nci

    @property
    def zone(self):
        return self.__zone
    
    def __repr__(self):
        return "electeur"