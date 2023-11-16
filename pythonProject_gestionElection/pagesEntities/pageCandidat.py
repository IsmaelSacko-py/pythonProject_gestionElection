
from pagesEntities.pageAccueil import *
callPage()

from entities.personne import *
from entities.admin import *
from entities.candidat import *
import tkinter
from tkinter import ttk
# from main import *

import time



class pageCandidat(appConfiguration):
    global admin, addCandidat, btnCandidatDiv, listePartis
    DB = DB()
    cursor, connexion = DB.getConnexion()
    admin = Admin("Sacko", "Ismael")
    
    def __init__(self, app:tkinter.Tk, listEntites:list, title:str = "Ajout d'un candidat"):
        
        super().__init__(app, listEntites, title)
        # super().objectCrees.append(pageCandidat)
        super().objectCrees.append(self)

        self.__divisionsCandidats = []
        self.__labelsCandidats = []
        self.__inputsCandidats = []
        self.__Label_namesCandidats = ['Nom', 'Prenom', 'Nom du parti']

    # def pageCandidat(self):
    # global addCandidat, btnCandidatDiv




    def ajoutCandidat(self):
        global candidatTrouve

        Values = []
        for entry in self.__inputsCandidats:
            Values.append(entry.get())
        
        # Recuperation des informations d'un candidat
        # Nom, Prenom, IdParti = Values[0], Values[1], listePartis.get(Values[2])
        candidat = Candidat(Values[0], Values[1], listePartis.get(Values[2]))

        # Pour verifier si un champs est vide
        candidatTrouve = False
        for Value in Values:
            if Value == '':
                candidatTrouve = True
                break

        if not candidatTrouve:
            admin.add(candidat)
            # cursor.execute("INSERT INTO candidat(nomCandidat, prenomCandidat, idParti) VALUES(%s, %s, %s) ", (Nom, Prenom, IdParti)) # 1ere methode
            #cursor.execute(f"INSERT INTO candidat(nomCandidat, prenomCandidat, idParti) VALUES({str(Nom)}, {str(Prenom)}, {IdParti}) ") # 2eme methode
            connexion.commit()
            self._infoText.config(text="Informations enregistrées avec success", bg=self._infoTextBgSuccess, fg='white', width = 32, height=3,font=("Arial", 10, "bold"))
            for label_name, entry in zip(self.__Label_namesCandidats, self.__inputsCandidats):
                entry.delete(0, 'end') if label_name != 'Nom du parti' else entry.set("")
        else:

            self._infoText.config(text="Tous les champs sont obligatoires", bg=self._infoTextBgEchec ,fg='white', width = 30, height=3,font=("Arial", 10, "bold"))

    # Verification_des_differentes_pages()

    def test(self):
        # self._main_div.destroy()
        print("Hello")
    

        # time.sleep(1)
        # pageCand = pageCandidat(self._app, self._listEntities)

        # pageCand.createPageElement()

    def destruction(self, objectCrees):
        super().destruction(objectCrees)
        self.__divisionsCandidats = []
        self.__labelsCandidats = []
        self.__inputsCandidats = []

    def createPageElement(self):
        global listePartis
         
        # Selection de Partis
        cursor.execute("SELECT * FROM parti")
        Partis = cursor.fetchall()
        listePartis = {Par[1]:Par[0] for Par in Partis}
        
        
        
        self.destruction(self.objectCrees)
        # if len(self.objectCrees) > 1:
        #     print(f'object crees avant suppression page Cand = {self.objectCrees}')

        #     for i, obj in enumerate(self.objectCrees): 
        #         print(f' tour = {i+1} - main_div = {obj._main_div}')
        #         if obj._main_div:
        #             obj.destruction()  
            # self.objectCrees = []
        
        print(f'object crees apres suppression page Cand = {self.objectCrees}')

        super().appCreation()
        

        # appMenu = AppMenu(self._app, self._listEntities)
        
        # appMenu.createMenu()

        for i in range(3):  
            self.__divisionsCandidats.append(tkinter.Frame(self._main_div, bg=self._bg))
            self.__labelsCandidats.append(tkinter.Label(self.__divisionsCandidats[i], text=self.__Label_namesCandidats[i], width=40, bg=self._bg, font=("Ariel", 15, "bold")))
            if self.__Label_namesCandidats[i] == 'Nom du parti':
                self.__inputsCandidats.append(ttk.Combobox(self.__divisionsCandidats[i], width=23, values=list(listePartis.keys()) ,  font=("Arial", 12), state="readonly"))
            else:
                self.__inputsCandidats.append(tkinter.Entry(self.__divisionsCandidats[i], width=25, borderwidth=3, bg=self._btnInput, font=("Arial", 12)))
                                
                # Pour donner le focus au 1er champs de saisie
                if self.__Label_namesCandidats[i] == "Nom":
                    self.__inputsCandidats[i].focus()

            # positionnement des differents widgets
            self.__divisionsCandidats[i].pack(pady=10)
            self.__labelsCandidats[i].pack()
            self.__inputsCandidats[i].pack()

        btnCandidatDiv = tkinter.Frame(self._main_div, bg=self._bg)
        btnCandidatDiv.pack()
        btnCandidat = tkinter.Button(btnCandidatDiv, text="ENREGISTRER", bg=self._btnBg, fg=self._btnInput, width=12, border=3, font=self._btnFont, command=self.ajoutCandidat)
        btnCandidat2 = tkinter.Button(btnCandidatDiv, text="ANNULER", bg=self._infoTextBgEchec, fg=self._btnInput, width=12, border=3, font=self._btnFont, command=lambda: print("Hello"))
        btnCandidat.grid(row=0, column=1, pady=(10, 0))
        btnCandidat2.grid(row=0, column=0,pady=(10, 0), padx=(0, 10))


# pageCand = pageCandidat()
# pageCand.createPageElement()
# pageCand.mainloop()