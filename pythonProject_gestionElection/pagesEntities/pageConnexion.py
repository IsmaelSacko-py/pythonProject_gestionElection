
import tkinter
from entities.personne import callDB
# from appConfig import appConfiguration
# from appMenu import AppMenu
callDB()
# from entities.appConfig import appConfiguration
from pagesEntities.pageAccueil import AppMenu, appConfiguration, pageAccueil

# import pagesEntities.pageAccueil
# from entities.appMenu import AppMenu

class pageConnexion(appConfiguration):

    def __init__(self, app : tkinter.Tk, list_entites:list , title:str = "ELECTION PROJECT BY SACKO ISMAEL"):
        super().__init__(app, list_entites, title)
        # super().objectCrees.append(self)
        print(f'listes entitees = {list_entites}')
        self.__Users = {"Ismael":"1001","Olsen":"2002", "Hance":"3003"}
        self.__Session = []
        self.__labelsConnexion = []
        self.__inputConnexion = []
        self.__nom_labelConnexion = ['Login', 'Password']



    def connexion(self):
        global labelsConnexion, inputConnexion

        Value = self.__Users.get(self.__inputConnexion[0].get(), 0)
        if Value != 0 and Value == self.__inputConnexion[1].get():
            # Bienvenu()
            self.__Session.extend([self.__inputConnexion[0].get(), Value])

            for i in range(2):
                self.__labelsConnexion[i].destroy()
                self.__inputConnexion[i].destroy()
            label_alerte.destroy()
            btnConnexion.destroy()
            self.__labelsConnexion, self.__inputConnexion = [], []

            # return True
            page_accueil = pageAccueil(self._app, self._listEntities)
            # page_accueil.createObject()
            # print(f"liste des entitees = {page_accueil.listEntities}")
            # page_accueil.addObject()
            page_accueil.createPageElement()
            # return True

                        # Parametrage de la fenêtre
            # self._app.title(self._title.upper())

            # self._app.geometry("600x500+350+100")
            # #self._app.iconbitmap("Icones/icone1.ico") # Permet de mettre une icone au niveau de la fenetre
            # self._app.resizable(width = False, height= False)
            # self._app.config(bg = self._bg)

            # self._main_div = tkinter.Frame(self._app, bg=self._bg)
            # self._main_div.pack(expand='YES')

            # # sous_main_div = tkinter.Frame(main_div, bg=re)
            # # sous_main_div.pack(expand=1)

            # # Pour la partie qui affichera des infos dans le cas où l'ajout s'est bien passee ou s'il y a eu une erreur
            # self._infoDiv = tkinter.Frame(self._main_div)
            # self._infoText = tkinter.Label(self._infoDiv, bg=self._bg)
            # self._infoDiv.pack(pady=(0, 10))
            # self._infoText.pack()
            
            # appMenu = AppMenu(self._app, self._listEntities)
            
            # appMenu.createMenu()

        

        else:
            label_alerte.config(text="Mot de passe ou login incorrect")
            self.__inputConnexion[1].delete(0, 'end')
            # return False

    def deconnexion(self, topBar:tkinter.Menu):
        global Session

        # Verification_des_differentes_pages()
        self.__Session = []

        topBar.destroy()
        # del menu # Pour supprimer le menu=[-[[]]]
        self.createPageElement()
    
    
    def destruction(self, objectCrees):
        super().destruction(objectCrees)
        self.__labelsConnexion = []
        self.__inputConnexion = []

    def createPageElement(self):
        global labelsConnexion, inputConnexion, label_alerte, btnConnexion
        self.__labelsConnexion, self.__inputConnexion = [], []
        super().objectCrees.append(self)

        #Verification_des_differentes_pages()

        self.destruction(self.objectCrees)
 

        super().appCreation()


        for i in range(2):
            self.__labelsConnexion.append(tkinter.Label(self._main_div, text=self.__nom_labelConnexion[i], bg=self._bg, font=("Arial", 15, "bold"), width=40))
            self.__inputConnexion.append(tkinter.Entry(self._main_div, bg=self._btnInput, width=25, border=3, font=("Arial", 12), show= "" if (self.__nom_labelConnexion[i] == "Login") else "*"))
            # Pour donner le focus au 1er champs de saisie
            if self.__nom_labelConnexion[i] == "Login":
                self.__inputConnexion[i].focus()
            self.__labelsConnexion[i].pack()
            self.__inputConnexion[i].pack(pady = (0, 20) if (self.__nom_labelConnexion[i] == "Login") else 0) 

        label_alerte = tkinter.Label(self._main_div, fg=self._msgAlert, bg=self._bg, width=30, font=self._msgAlertFont)
        btnConnexion = tkinter.Button(self._main_div, text="CONNEXION", bg=self._btnBg, fg=self._btnInput, width=15, border=3, command=self.connexion, font=self._btnFont)
        
        label_alerte.pack()
        btnConnexion.pack(pady=(3, 0))

    def __repr__(self):
        return "pageConnexion"

# app = tkinter.Tk()
# pageCon = AppConnexion(app)
# pageCon.createPageElement()
# app.mainloop()