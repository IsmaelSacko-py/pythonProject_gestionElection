import os
print("Chemein dans admin : "+ os.path.abspath(os.path.join(os.path.dirname(__file__))))
from entities.personne import *
from entities.candidat import Candidat
from entities.electeur import Electeur


callDB()
class Admin(Personne):
    global cursor, connexion
    DB = DB()
    cursor, connexion = DB.getConnexion()

    def __init__(self, Name, Surname):
        super().__init__(Name, Surname)

    def add(self, entity):
        if isinstance(entity, Candidat):
            print(f"surname = {entity.surname}")
            query = "INSERT INTO candidat(nomCandidat, prenomCandidat, idParti) VALUES(?, ?, ?)"
            cursor.execute(query, (entity.name, entity.surname, entity.parti))
            connexion.commit()
        elif isinstance(entity, Electeur):
            query = "INSERT INTO electeur(nomElecteur, prenomElecteur, Nci, codeZone) VALUES(?, ?, ?, ?)"
            cursor.execute(query, (entity.name, entity.surname, entity.nci, entity.zone))
            connexion.commit()
        else:
            query = "INSERT INTO vote(idCandidat, idElecteur) VALUES(?, ?)"
            cursor.execute(query, (entity.idCandidat, entity.idElecteur))
            connexion.commit()

    def getAll(self, entity:str):
        # entity = "candidat" if entity.lower() == "candidat" else "electeur"
        cursor.execute(f"SELECT * FROM {entity}")
        return cursor.fetchall()

    def getOne(self, entity:str, id):
        entity = entity.__repr__()
        query = f"SELECT * FROM {entity} WHERE id{entity.capitalize()} = ? "
        cursor.execute(query, (id,))
        return cursor.fetchone()

ad = Admin('ad33', 'ad33')
c = Candidat("test333", "test333", 5)
# v = Electeur(1)
# ad.add(e)
print(ad.getAll("vote"))