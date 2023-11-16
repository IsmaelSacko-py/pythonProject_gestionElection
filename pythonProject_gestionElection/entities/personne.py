def callDB():
    import sys, os

    # Obtenez le chemin absolu du répertoire parent du dossier actuel (candidat)
    repertoire_parent = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))


    # Ajoutez le répertoire parent à sys.path
    sys.path.append(repertoire_parent)
    # Vous pouvez maintenant importer DB.py comme un module

    
callDB()
from DB.DB import *

class Personne:

    def __init__(self,Name, Surname):
        self._name = Name
        self._surname = Surname
        self.test = "Hello"

    @property
    def name(self):
        return self._name
    
    @property
    def surname(self):
        return self._surname

    def add(self):
        pass

    def update(self, id):
        pass

    def delete(self, id):
        pass

p = Personne("Ismael", "Sacko")
print(p.test)
