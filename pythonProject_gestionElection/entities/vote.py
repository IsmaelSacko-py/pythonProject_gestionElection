

class Vote:

    def __init__(self, id_candidat, id_electeur):
        # self.__id = Id
        self.__idCandidat = id_candidat
        self.__idElecteur = id_electeur

    @property
    def id(self):
        return self.__id
    
    @property
    def idCandidat(self):
        return self.__idCandidat
    
    @property
    def idElecteur(self):
        return self.__idElecteur
    
    def __repr__(self):
        return "vote"