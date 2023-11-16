
from entities.appConfig import *
from entities.appMenu import AppMenu
def callPage():
    import sys, os

    # Obtenez le chemin absolu du répertoire parent du dossier actuel (candidat)
    repertoire_parent = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    # Ajoutez le répertoire parent à sys.path
    sys.path.append(repertoire_parent)

    # Vous pouvez maintenant importer DB.py comme un module
    
# callPage()
var = 30

class pageAccueil(appConfiguration):

    def __init__(self, app:tkinter.Tk, list_entites:list , title:str = "ELECTION PROJECT BY SACKO ISMAEL"):
        super().__init__(app, list_entites, title)
        super().objectCrees.append(self)

    def test(self):
        print("hello")

    def createPageElement(self):
        super().destruction(self.objectCrees)
        
        super().appCreation()
        # super().main_div.config(background='green')
        
        # print('hello page electeur')
        # self.destroy_main_div()
        
        
        appMenu = AppMenu(self._app, self._listEntities)
        
        appMenu.createMenu()

        label_bienvenue = tkinter.Label(self._main_div, bg = self._bg, text = "Bienvenue", font = ("Arial", 40, "bold"), foreground = "white").pack(expand = 1)
    