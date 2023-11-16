
import tkinter
# from entities.evenement import Events

# events = Events()
class appConfiguration:
    
    objectCrees = []
    def __init__(self, app:tkinter.Tk, list_entites:list , title:str):
        self._app = app
        # # Pour la gestion des évenements tkinter
        # self._app.bind('<KeyPress-Return>', events.gestionEvents()) # Pour enregistrer les données du formulaire en cliquant sur la touche 'Enter'
        # self._app.bind('<Escape>', events.gestionEvents()) # Pour quitter l'appli
        # self._app.bind('<Shift-Alt_R>', events.gestionEvents()) # Pour se deconnecter de l'appli
        self._title = title
        # self._menu = AppMenu
        self._listEntities = list_entites
        # Pour la gestion des couleurs de fond et du style des textes
        self._bg = "#0E6A85" # Couleur de fond de l'appli
        self._btnBg = "#0A5F14" # Couleur de fond des bouttons
        self._btnInput = "#E5EDE6" # Couleur de fond des inputs
        self._btnFont = ("Arial", 9, "bold")
        self._msgAlert = '#FC0725'
        self._msgAlertFont = ('Arial', 9)
        self._infoTextBgSuccess , self._infoTextBgEchec = '#33ff33', '#ff6666'

        self._main_div = None
        self._infoDiv = None
        self._infoText = None
        self._objectCreate = None
        self._isCreate = True
        

    def addObject(self, object):
        appConfiguration.objectCrees.append(object)
        # self._objectCreate = appConfiguration.objectCrees
        # print(f'object = {self._objectCreate} - objectCreer = {appConfiguration.objectCrees}')


    def appCreation(self):    
        # Parametrage de la fenêtre
        self._app.title(self._title.upper())

        # self._app.geometry("600x500+350+100")
        # # self._app.iconbitmap("Icones/icone1.ico") # Permet de mettre une icone au niveau de la fenetre
        # # self._app.resizable(width = False, height= False)
        # self._app.config(bg = self._bg)

        self._main_div = tkinter.Frame(self._app, bg=self._bg)
        self._main_div.pack(expand='YES')

        # sous_main_div = tkinter.Frame(main_div, bg=re)
        # sous_main_div.pack(expand=1)

        # Pour la partie qui affichera des infos dans le cas où l'ajout s'est bien passee ou s'il y a eu une erreur
        self._infoDiv = tkinter.Frame(self._main_div)
        self._infoText = tkinter.Label(self._infoDiv, bg=self._bg)
        self._infoDiv.pack(pady=(0, 10))
        self._infoText.pack()


    def destruction(self, objectCrees):


        # for i, obj in enumerate(objectCrees): 
        #     print(f' tour = {i+1} - main_div = {obj._main_div}')
        #     if obj._main_div:
        #         # obj.destruction()
        if len(objectCrees) > 1:
            # print(f'object crees avant suppression page Cand = {self.objectCrees}')
        # self.appCreation()
            for i, obj in enumerate(objectCrees): 
                print(f' tour = {i+1} - main_div = {obj._main_div}')
                if obj._main_div:
                    # obj.destruction() 
                    obj._main_div.destroy()
                    obj._infoDiv.destroy()
            
        # print("Hello")

    @property
    def main_div(self):
        return self._main_div

     
