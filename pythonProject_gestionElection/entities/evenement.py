

# from main import *

class Events:

    def __init__(self, event):
        self.__event = event

    def gestionEvents(self):
        global Session

        # Permet de d'afficher le parti du candidat sélectionné
        if self.__event.keysym == '??':
            Value = listeCandidats.get(listeDeroulante.get(), 0)
            listeDeroulante.set(Value)
        
        if self.__event.keysym == 'Escape':
            app.destroy()

        if self.__event.keysym == "Alt_R": # Pour se deconnecter de l'appli
            if Check_Menu:
                Deconnexion()

        # Pour effectué les mêmes actions que les bouttons lorsque l'on clique sur la touche 'Enter'
        if self.__event.keysym == 'Return':
            if labelsConnexion: # Verifie s'il s'agit de la touche 'Enter' de la page de connexion
                verifUser()
            if divisionsCandidats: # Verifie s'il s'agit de la touche 'Enter' de la page candidat
                addCandidat()
            if divisionsElecteurs: # Verifie s'il s'agit de la touche 'Enter' de la page electeur
                addElecteur()
            if divisionsFaireVote: # Verifie s'il s'agit de la touche 'Enter' de la page faire vote
                addVote()


    # # Pour la gestion des évenements tkinter
    # app.bind('<KeyPress-Return>', Events) # Pour enregistrer les données du formulaire en cliquant sur la touche 'Enter'
    # app.bind('<Escape>', Events) # Pour quitter l'appli
    # app.bind('<Shift-Alt_R>', Events) # Pour se deconnecter de l'appli