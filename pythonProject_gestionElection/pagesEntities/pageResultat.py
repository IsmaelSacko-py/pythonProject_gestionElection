from pagesEntities.pageAccueil import *
callPage()
# from main import *
from operator import itemgetter # Pour trier les resultat du vote
from entities.personne import *
from entities.admin import *
# from entities.appConfig import appConfiguration
# from entities.appMenu import AppMenu

# from pagesEntities.pageCandidat import pageCandidat
# from pagesEntities.pageElecteur import pageElecteur
# from pagesEntities.pageFaireVote import pageFaireVote
# from pagesEntities.pageResultat import pageResultat
# from pagesEntities.test import *
import os



import tkinter
# from entities.electeur import *

class pageResultat(appConfiguration):
        # global divisionsElecteurs, labelsElecteurs, inputsElecteurs, Label_namesElecteurs
        # global divisionsCandidats, labelsCandidats, inputsCandidats, Label_namesCandidats 
        # global divisionsFaireVote, labelsFaireVote, inputFaireVote, label_namesFaireVote, VerifEtatPageResultat, ListeBoxe
        global VerifEtatPageResultat, ListeBoxe, label_result
        admin = Admin("Sacko", "Ismael")
        DB = DB()
        cursor, connexion = DB.getConnexion()
        
        def __init__(self, app:tkinter.Tk, listEntites:list, title:str = "Resultat de l'election"):
            super().__init__(app, listEntites, title)
            super().objectCrees.append(self)

            # self.__app = tkinter.Tk()
            # self.__app.geometry("600x500+350+100")
            # #self.__app.iconbitmap("Icones/icone1.ico") # Permet de mettre une icone au niveau de la fenetre
            # self.__app.resizable(width = False, height= False)
            # self.__app.config(bg = bg)
            # self.__app.title("Resultat de l'election".upper())

            # self.__main_div = tkinter.Frame(self.__app, bg=bg)
            # self.__main_div.pack(expand='YES')

            # # sous_main_div = tkinter.Frame(main_div, bg=re)
            # # sous_main_div.pack(expand=1)

            # # Pour la partie qui affichera des infos dans le cas où l'ajout s'est bien passee ou s'il y a eu une erreur
            # self.__infoDiv = tkinter.Frame(self.__main_div)
            # self.__infoText = tkinter.Label(self.__infoDiv, bg=bg)
            # self.__infoDiv.pack(pady=(0, 10))
            # self.__infoText.pack()


        

        # Verification_des_differentes_pages()
        
        # if VerifEtatPageResultat:
        #     ListeBoxe.destroy()
        #     label_result.destroy()

        # VerifEtatPageResultat = True
        

        def createPageElement(self):
            page_candidat = os.environ.get('page_candidat')
            page_electeur = os.environ.get('page_electeur')
            page_faire_vote = os.environ.get('page_faire_vote')
            page_resultat = os.environ.get('page_resultat')


            self.destruction(self.objectCrees)

            # appMenu = AppMenu(self._app, self._listEntities)
        
            # appMenu.createMenu()
            
            super().appCreation()

            # Selection des candidats et leurs voix
            cursor.execute("SELECT C.nomCandidat, C.prenomCandidat, COUNT(C.idCandidat) AS `Nombre de voix` FROM candidat C, vote V WHERE C.idCandidat = V.idCandidat GROUP BY C.nomCandidat, C.prenomCandidat")
            Candidats_et_leurs_votes = cursor.fetchall()
            ListeBoxe = tkinter.Listbox(self._main_div, width=50, height=13, bg=self._btnInput, font=("Arial", 10, "bold")) # Permet de creer une liste d'elements
            Candidats_et_leurs_votes_Sorted = sorted(Candidats_et_leurs_votes, key = itemgetter(2))
            NbrVote = 0
            for i in range(len(Candidats_et_leurs_votes_Sorted)):
                ListeBoxe.insert(i,f"{len(Candidats_et_leurs_votes_Sorted)-i} - {Candidats_et_leurs_votes_Sorted[i][0]} {Candidats_et_leurs_votes_Sorted[i][1]} (Nombre de voix : {Candidats_et_leurs_votes_Sorted[i][2]})")
                NbrVote +=Candidats_et_leurs_votes_Sorted[i][2]
                # insert(<valeur>, <texte>)

            label_result = tkinter.Label(self._main_div, width=40, bg=self._bg, font=("Arial", 20, "bold"))
            label_result.config(text=f"Le vainqueur est {Candidats_et_leurs_votes_Sorted[-1][0]} {Candidats_et_leurs_votes_Sorted[-1][1]}\nPourcentage de voix : {(Candidats_et_leurs_votes_Sorted[-1][2]*100)/NbrVote:.2f}%")
            label_result.pack(pady=(0, 20))
            ListeBoxe.pack(expand="YES")
        
        # def mainloop(self):
        #      return self.mainloop()
        

# pageResult = pageResultat()
# pageResult.createElementPage()
# pageResult.mainloop()