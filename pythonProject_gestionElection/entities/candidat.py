
from entities.personne import *

callDB()
from DB.DB import *

class Candidat(Personne):

    def __init__(self, Name, Surname, Parti):
        super().__init__(Name, Surname)
        self.__parti = Parti

    
    @property
    def name(self):
        return self._name
    
    @property
    def surname(self):
        return self._surname
    
    @property
    def parti(self):
        return self.__parti

    def __repr__(self):
        return "candidat"
    
c = Candidat("Sacko", "Ismael", 9)

test = c

print(test)
print(f"type : {type(c.__repr__())}")
    

