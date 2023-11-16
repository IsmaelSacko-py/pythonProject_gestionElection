
from pagesEntities.pageElecteur import *
from pagesEntities.pageCandidat import *
from pagesEntities.pageFaireVote import *
from pagesEntities.pageResultat import *
from pagesEntities.pageAccueil import *
from pagesEntities.pageConnexion import *
# from entities.appConnexion import AppConnexion

gui = tkinter.Tk()
gui.geometry("600x500+350+100")
# gui.iconbitmap("Icones/icone1.ico") # Permet de mettre une icone au niveau de la fenetre
gui.resizable(width = False, height= False)
gui.config(bg = "#0E6A85")

listEntites = [pageCandidat, pageElecteur, pageFaireVote, pageResultat, pageConnexion]

pageElect = pageConnexion(gui, listEntites)

pageElect.createPageElement()


gui.mainloop()


# liste1 = ['mangue', 'citron']
# liste2 = ['banane', 'avocat', 'patate']
# liste2 = liste2[::-1]
# for fruit in liste2:
#     liste1.insert(0, fruit)

# print(liste1)