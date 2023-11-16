# from personne import *
# from admin import *
# from electeur import *
import os
from pagesEntities.pageAccueil import *
import tkinter
from tkinter import ttk
callPage()
# from main import *
# from main import app, bg, btnBg, btnInput, infoText, Verification_des_differentes_pages, videuseDeChamps, main_div,  btnFont, msgAlert, msgAlertFont, infoTextBgSuccess, self._infoTextBgEchec
# bg = "#0E6A85" # Couleur de fond de l'appli
# btnBg = "#0A5F14" # Couleur de fond des bouttons
# btnInput = "#E5EDE6" # Couleur de fond des inputs
# btnFont = ("Arial", 9, "bold")
# msgAlert = '#FC0725'
# msgAlertFont = ('Arial', 9)
# infoTextBgSuccess , self._infoTextBgEchec = '#33ff33', '#ff6666'

from entities.personne import *
from entities.admin import *
from entities.electeur import *
# from pagesEntities.pageAccueil import *
# from entities.appConfig import appConfiguration
# from entities.appMenu import AppMenu

# from pagesEntities.pageCandidat import pageCandidat
# # from pagesEntities.pageElecteur import pageElecteur
# from pagesEntities.pageFaireVote import pageFaireVote
# from pagesEntities.pageResultat import pageResultat

# from pagesEntities.test import *
# import os



# # Parametrage de la fenêtre
# app = tkinter.Tk()
# app.geometry("600x500+350+100")
# #app.iconbitmap("Icones/icone1.ico") # Permet de mettre une icone au niveau de la fenetre
# app.resizable(width = False, height= False)
# app.title("ELECTION PROJECT BY SACKO ISMAEL")
# app.config(bg = bg)

class pageElecteur(appConfiguration):
    global admin, addElecteur, btnElecteurDiv, electeurTrouve, listeZones
    admin = Admin("Sacko", "Ismael")
    DB = DB()
    cursor, connexion = DB.getConnexion()

    def __init__(self, app:tkinter.Tk, listEntites:list, title:str = "Ajout d'un electeur"):
        super().__init__(app, listEntites, title)

        super().objectCrees.append(self)

        self.__divisionsElecteurs = []
        self.__labelsElecteurs = []
        self.__inputsElecteurs = []
        self.__Label_namesElecteurs = ['Nom', 'Prenom', 'Nci', 'Zone']
        # self.__app.mainloop()

    # def pageElecteur():
    # global divisionsElecteurs, labelsElecteurs, inputsElecteurs, Label_namesElecteurs, btnElecteur
    # global divisionsFaireVote, labelsFaireVote, inputFaireVote
    # global addElecteur, btnElecteurDiv, electeurTrouve
    # app.title("Ajout d'un electeur".upper())
    
    # # Selection des Zones
    # cursor.execute("SELECT * FROM zone")
    # Zones = cursor.fetchall()

    # listeZones = {Zone[1]:Zone[0] for Zone in Zones}

    def ajoutElecteur(self):
        Valeurs = []
        for entry in self.__inputsElecteurs:
            Valeurs.append(entry.get())

        electeur  = Electeur(Valeurs[0], Valeurs[1], Valeurs[2], listeZones.get(Valeurs[3]))

        # Pour verifier si un champs est vide
        electeurTrouve = False
        for Value in Valeurs:
            if Value == '':
                electeurTrouve = True
                break
            
        if not electeurTrouve:

            #cursor.execute(f"INSERT INTO candidat(nomCandidat, prenomCandidat, idParti) VALUES({str(Nom)}, {str(Prenom)}, {IdParti}) ") # 2eme methode
            # cursor.execute("INSERT INTO electeur(nomElecteur, prenomElecteur, Nci, codeZone) VALUES(%s, %s, %s, %s)", (Nom, Prenom, Nci, codeZone))
            admin.add(electeur)
            connexion.commit() # Permet de retrouver, dans le fichier sql, les données inserées dans la base

            self._infoText.config(text="Informations enregistrées avec success", bg=self._infoTextBgSuccess, fg='white',width = 32, height=3,font=("Arial", 10, "bold"))
            for label_name, entry in zip(self.__Label_namesElecteurs, self.__inputsElecteurs):
                entry.delete(0, 'end') if label_name != 'Zone' else entry.set("")
        else:

            self._infoText.config(text="Tous les champs sont obligatoires", bg=self._infoTextBgEchec, fg='white',width = 30, height=3,font=("Arial", 10, "bold"))


    # Permet de supprimer les widgets de la page Ajout d'un candidat apres que l'utilisateur l'ait visité
    # Verification_des_differentes_pages()

    # def destroy_main_div(self):
    #     self._main_div.config(background = 'red')
    #     super().main_div.config(background = 'green')

        # self._main_div = tkinter.Frame(self._app, bg=self._bg)
        # self._main_div.pack(expand='YES')

    def destruction(self, objectCrees):
        super().destruction(objectCrees)
        self.__divisionsElecteurs = []
        self.__labelsElecteurs = []
        self.__inputsElecteurs = []

    
    def createPageElement(self):
        global listeZones
         
        # super().objectCrees[0](self._app, self._listEntities).t
        # Selection des Zones
        cursor.execute("SELECT * FROM zone")
        Zones = cursor.fetchall()
        listeZones = {Zone[1]:Zone[0] for Zone in Zones}
        
        # if super().objectCrees:
        # print(f"Hello objets crees {super().objectCrees}")

        self.destruction(self.objectCrees)

             
        print(f'object crees apres suppression page Elec = {super().objectCrees}')

        #     del super().objectCrees[:]
        # print(f'cand = {super().objectCrees[:]}')
        super().appCreation()
        # super().main_div.config(background='green')
        
        # print('hello page electeur')
        # self.destroy_main_div()
        # appMenu = AppMenu(self._app, self._listEntities)
        
        # appMenu.createMenu()
        # self._main_div = tkinter.Frame(self._app, bg=self._bg)
        # self._main_div.pack(expand='YES')
        for i in range(4):  
            self.__divisionsElecteurs.append(tkinter.Frame(self._main_div, bg=self._bg))
            self.__labelsElecteurs.append(tkinter.Label(self.__divisionsElecteurs[i], text=self.__Label_namesElecteurs[i], width=40, bg=self._bg, font=("Ariel", 15, "bold")))
            if self.__Label_namesElecteurs[i] == 'Zone':
                self.__inputsElecteurs.append(ttk.Combobox(self.__divisionsElecteurs[i], width=23, values=list(listeZones.keys()) ,  font=("Arial", 12), state="readonly"))
            else:
                self.__inputsElecteurs.append(tkinter.Entry(self.__divisionsElecteurs[i], width=25, borderwidth=3, bg=self._btnInput, font=("Arial", 12)))
                
                # Pour donner le focus au 1er champs de saisie
                if self.__Label_namesElecteurs[i] == "Nom":
                    self.__inputsElecteurs[i].focus()

            # positionnement des differents widgets
            self.__divisionsElecteurs[i].pack(pady=10)
            self.__labelsElecteurs[i].pack()
            self.__inputsElecteurs[i].pack()

        btnElecteurDiv = tkinter.Frame(self._main_div, bg=self._bg)
        btnElecteurDiv.pack()
        btnElecteur = tkinter.Button(btnElecteurDiv, text="ENREGISTRER", bg=self._btnBg, fg=self._btnInput, width=12, border=3, font=self._btnFont, command=self.ajoutElecteur)
        btnElecteur2 = tkinter.Button(btnElecteurDiv, text="ANNULER", bg=self._infoTextBgEchec, fg=self._btnInput, width=12, border=3, font=self._btnFont, command=lambda: print("Hello"))
        btnElecteur.grid(row=0, column=1, pady=(10, 0))
        btnElecteur2.grid(row=0, column=0,pady=(10, 0), padx=(0, 10))




    # btnElecteur = tkinter.Button(main_div, text="ENREGISTRER", bg=btnBg, fg=btnInput, width=15, border=3,activebackground="light blue", font=btnFont, command=addElecteur)
    # btnElecteur.pack(pady=(10, 0))

    #pageElecteurWindow.mainloop()

# print("Hello")
# app = tkinter.Tk()
# pageElec = pageElecteur(app)
# pageElec.createPageElement()
# pageElec.mainloop()