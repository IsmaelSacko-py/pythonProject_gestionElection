import sqlite3 as sql3
import os
DB_NAME = "DB/projet_election.db"


class DB:

    def getConnexion(self):
        try:
            self.__connexion = sql3.connect(DB_NAME)
            # Activer les contraintes de clé étrangère. Cette commande ("PRAGMA foreign_keys = ON;") permet qu'elles soient appliquées dans SQLite.
            # self.__connexion.execute("PRAGMA foreign_keys = ON;")
            self.__cursor = self.__connexion.cursor()
            print("Connexion reussie!")

        except Exception as e:
            print(f"Erreur lors de la connexion a la base de donnees [{e}]")
            exit(-1)
        finally:
            return self.__cursor, self.__connexion

    def executeSelectAll(self, sql) -> list:
        self.getConnexion()
        self.__cursor.execute(sql)
        return self.__cursor.fetchall()
    
    def executeMaj(self, sql):
        self.getConnexion()
        self.__cursor.execute(sql)
        self.__connexion.commit()

    def closeConnection(self):
        self.getConnexion()
        if (self.__connexion):
            try :
                self.__connexion.close()
            except Exception as f:
                print(f"Erreur : [{f}]")

    @property
    def connexion(self):
        return self.__connexion
    
    @property
    def cursor(self):
        return self.__cursor
    

db = DB()

db.getConnexion()

db.closeConnection()

        
"""
    INTEGER : Pour les valeurs entières, y compris les nombres positifs et négatifs. SQLite stocke automatiquement 
    les valeurs entières en tant qu'entiers s'ils sont dans la plage des entiers. Sinon, il utilise un stockage dynamique 
    pour des valeurs plus grandes.

    REAL : Pour les valeurs numériques à virgule flottante (avec une précision double en virgule flottante).

    TEXT : Pour les chaînes de caractères. SQLite prend en charge les chaînes de texte, les chaînes Unicode et les chaînes binaires.

    BLOB : Pour les données binaires brutes, telles que les images, les fichiers, etc.

    NULL : Pour les valeurs nulles (absence de valeur).

    NUMERIC : Pour les valeurs numériques stockées sous forme de texte.

    BOOLEAN : SQLite ne possède pas de type de données spécifique pour les booléens. Cependant, les booléens sont souvent représentés 
    sous forme d'entiers 0 (faux) et 1 (vrai).
"""