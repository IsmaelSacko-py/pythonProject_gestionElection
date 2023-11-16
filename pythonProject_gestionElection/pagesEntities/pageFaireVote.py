
from pagesEntities.pageAccueil import *
callPage()

from entities.personne import *
from entities.admin import *
from entities.candidat import *
# from entities.appConfig import appConfiguration
from entities.vote import Vote
# from entities.appMenu import AppMenu

# from pagesEntities.pageCandidat import pageCandidat
# from pagesEntities.pageElecteur import pageElecteur
# # from pagesEntities.pageFaireVote import pageFaireVote
# from pagesEntities.pageResultat import pageResultat
# from pagesEntities.test import *
import os


import tkinter
from tkinter import ttk
# from main import *


class pageFaireVote(appConfiguration):
    global admin, addVote, btnFaireVoteDiv, label_alerte_Nci, entry_Nci, listeCandidats
    DB = DB()
    cursor, connexion = DB.getConnexion()
    admin = Admin("Sacko", "ismael")
    def __init__(self, app:tkinter.Tk, listEntites:list, title:str = "Faie le vote"):

        super().__init__(app, listEntites, title)
        super().objectCrees.append(self)

        

        self.__divisionsFaireVote = []
        self.__labelsFaireVote = []
        self.__inputFaireVote = []
        self.__label_namesFaireVote = ['Nci de l\'électeur', 'Choix du candidat']

    # def pageFaireVote():
    #     # global divisionsCandidats, labelsCandidats, inputsCandidats
    #     # global divisionsElecteurs, labelsElecteurs, inputsElecteurs, btnElecteur
    #     # global divisionsFaireVote, labelsFaireVote, inputFaireVote
    #     global addVote, btnFaireVoteDiv, listeDeroulante, label_alerte_Nci, entry_Nci, listeCandidats




    def ajoutVote(self):

        if entry_Nci.get():
            print(f"Candidat : {listeDeroulante.get().split()[0]}")
            cursor.execute("SELECT C.idCandidat FROM candidat C, parti P WHERE C.idParti = P.idParti AND C.nomCandidat = ?", (listeDeroulante.get().split()[0], ))
            idCandidat = cursor.fetchone()
            print(f"idCandidat : {idCandidat}")

            cursor.execute("SELECT * FROM electeur WHERE Nci = ?", (entry_Nci.get(), ))
            Electeur = cursor.fetchone()    

            # Permet de verifier si le Nci de l'electeur est correct
            if not Electeur: 
                label_alerte_Nci.config(text="Nci incorrect")
                self._infoText.config(text='', bg=self._bg, width=0, height=0)

            else:
                global hasVote
                cursor.execute("SELECT * FROM vote V WHERE V.idElecteur = ?", (Electeur[0], ))
                hasVote = cursor.fetchall()

                # Permet de verifier si l'electeur n'a pas deja voté
                if not hasVote:
                    global idElecteur
                    idElecteur = Electeur[0]
                    label_alerte_Nci.config(text="")

                    # Permet de verifier si tous les champs ont été renseigné
                    if entry_Nci.get() and listeDeroulante.get():
                        print(f"idCnadidat = {idCandidat} et idElecteur = {idElecteur}")
                        vote = Vote(idCandidat[0], idElecteur)
                        print(f"idCnadidat = {vote.idCandidat} et idElecteur = {vote.idElecteur}")
                        admin.add(vote)
                        connexion.commit()

                        self._infoText.config(text="Vote effectué avec success", bg=self._infoTextBgSuccess, fg ='white', width = 28, height=2,font=("Arial", 10, "bold"))

                        entry_Nci.delete(0, 'end')
                        listeDeroulante.set('')

                    else:
                        self._infoText.config(text="Tous les champs sont obligatoires", bg=self._infoTextBgEchec, fg='white', width = 30, height=2,font=("Arial", 10, "bold"))

                else:
                    label_alerte_Nci.config(text="Ce électeur à déjà effectué un vote")
                    if not entry_Nci.get() or not listeDeroulante.get():
                        self._infoText.config(text="Tous les champs sont obligatoires", bg=self._infoTextBgEchec, fg='white',width = 30, height=2,font=("Arial", 10, "bold"))
                    else:
                        self._infoText.config(text='', bg=self._bg, width=0, height=0)


        else:
            #Electeur = None
            label_alerte_Nci.config(text="Veuillez entrer votre Nci")
            self._infoText.config(text="Tous les champs sont obligatoires", bg=self._infoTextBgEchec, fg='white',width = 30, height=2,font=("Arial", 10, "bold"))


    # Verification_des_differentes_pages()
    def destruction(self, objectCrees):
        super().destruction(objectCrees)
        self.__divisionsFaireVote = []
        self.__labelsFaireVote = []
        self.__inputFaireVote = []

    
    def createPageElement(self):
        global listeCandidats, entry_Nci, listeDeroulante, label_alerte_Nci

        # Selection des candidats
        cursor.execute("SELECT * FROM candidat C, parti P WHERE C.idParti = P.idParti")
        Candidats = cursor.fetchall()

        listeCandidats = {f"{Cand[1]} {Cand[2]}":f"{Cand[5]}" for Cand in Candidats}
        print(f"liste des candidats : {listeCandidats}")

        self.destruction(self.objectCrees)


        # appMenu = AppMenu(self._app, self._listEntities)
        
        # appMenu.createMenu()

        super().appCreation()

        for i in range(2):
            self.__divisionsFaireVote.append(tkinter.Frame(self._main_div, bg=self._bg))
            self.__labelsFaireVote.append(tkinter.Label(self.__divisionsFaireVote[i], text=self.__label_namesFaireVote[i],width=40, bg=self._bg, font=("Arial", 15, "bold")))
            if self.__label_namesFaireVote[i] == 'Choix du candidat':
                # Pour le message d'alerte qui s'affichera lorsque le Nci sera incorrecte
                label_alerte_Nci = tkinter.Label(self._main_div, bg=self._bg, fg=self._msgAlert, width=30, font=self._msgAlertFont)
                label_alerte_Nci.pack()

                self.__inputFaireVote.append(ttk.Combobox(self.__divisionsFaireVote[i], width=23, values=list(listeCandidats.keys()) ,  font=("Arial", 12), state="readonly"))
                
                # Pour déclencher un évènment suite à la sélection d'une option
                listeDeroulante = self.__inputFaireVote[i]
                # listeDeroulante.bind("<<ComboboxSelected>>", Events)

            else:
                self.__inputFaireVote.append(tkinter.Entry(self.__divisionsFaireVote[i], width=25, borderwidth=3, bg=self._btnInput, font=("Arial", 12)))
                entry_Nci = self.__inputFaireVote[i]
                entry_Nci.focus() # Pour donner le focus au 1er champs de saisie
                
                # entry_Nci.bind('<FocusOut>', check_Nci)
                
                # # Pour déclencher un évènment après que l'utilisqteur soit sorti du champs de saisie du Nci 
                # entry_Nci = self.__inputFaireVote[i]
                # entry_Nci.bind('<FocusOut>', Events)

            self.__divisionsFaireVote[i].pack()
            self.__labelsFaireVote[i].pack()
            self.__inputFaireVote[i].pack()   

        label_alerte_Nci = tkinter.Label(self._main_div, bg=self._bg, fg=self._msgAlert, width=30, font=self._msgAlertFont)
        label_alerte_Nci.pack()
        btnFaireVoteDiv = tkinter.Frame(self._main_div, bg=self._bg)
        btnFaireVoteDiv.pack(pady=(25, 0))
        btnFaireVote = tkinter.Button(btnFaireVoteDiv, text="ENREGISTRER", bg=self._btnBg, fg=self._btnInput, width=12, border=3, font=self._btnFont, command=self.ajoutVote)
        btnFaireVote2 = tkinter.Button(btnFaireVoteDiv, text="ANNULER", bg=self._infoTextBgEchec, fg=self._btnInput, width=12, border=3, font=self._btnFont, command=lambda : print("Hello"))
        btnFaireVote.grid(row=0, column=1)
        btnFaireVote2.grid(row=0, column=0, padx=(0, 10)) 

        # btnFaireVote = tkinter.Button(main_div, text="VALIDER", width=15, bg=btnBg, fg=btnInput, activebackground="light blue", font=btnFont, command=addVote)
        # btnFaireVote.pack(pady=(10, 0))


# pageVote = pageFaireVote()
# pageVote.createPageElement()
# pageVote.mainloop()