
import tkinter

# from pagesEntities.pageCandidat import pageCandidat
# from pagesEntities.pageElecteur import pageElecteur
# from pagesEntities.pageFaireVote import pageFaireVote
# from pagesEntities.pageResultat import pageResultat
# from pagesEntities.pageConnexion import pageConnexion


class AppMenu:
    # self.__pageConnexion = pageConnexion(self._app)
    def __init__(self, app:tkinter.Tk, listEntities:list):
        self._app = app

        
        # Creation du navBar
        self.__topBar = tkinter.Menu(self._app)
        self.__menu = tkinter.Menu(self.__topBar, tearoff=0, bg="light blue", font=(10))

        # Creation du menu et des sous-menus
        self.__allEntities = listEntities
        *self.__listEntities, self.__page_connexion = self.__allEntities

        self.__Functions = []
        self.__Labels = ["Ajout d'un candidat", "Ajout d'un électeur", "Faire le vote", "Résultat par ordre croissant", "Déconnexion", "Quitter"]
        # self.__Labels = ["Ajout d'un candidat", "Ajout d'un électeur", "Faire le vote", "Résultat par ordre croissant", "Déconnexion", "Quitter"]

    
    def createMenu(self):
        listFunctions = self.__listEntities[::-1]

        self.__Functions = [ lambda: self.__page_connexion(self._app, self.__allEntities).deconnexion(self.__topBar), quit]
        # self.__Functions = [ lambda: self.__page_connexion(self._app, self.__allEntities).deconnexion(self.__topBar), quit]

        for function in listFunctions:
            # if function not in self.__Functions:
            self.__Functions.insert(0, function(self._app, self.__listEntities).createPageElement)
            # else:
            #     pass
        print(f"Menu = {len(self.__Functions)}")
        for function, label in zip(self.__Functions, self.__Labels):
            if label == "Déconnexion":
                self.__menu.add_separator()
            self.__menu.add_command(label=label, command=function)

        self.__topBar.add_cascade(label= "MENU", menu=self.__menu)

        self._app.configure(menu=self.__topBar)