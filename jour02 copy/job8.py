import mysql.connector

class Employe:
    def __init__(self):
        self.connexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="laplateforme123", 
            database="entreprise"
        )
        self.curseur = self.connexion.cursor()

    def create(self, nom, prenom, salaire, id_service):
        self.curseur.execute(
            "INSERT INTO employe (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)",
            (nom, prenom, salaire, id_service)
        )
        self.connexion.commit()

    def read_all(self):
        self.curseur.execute("SELECT * FROM employe")
        return self.curseur.fetchall()

    def update_salaire(self, id_employe, nouveau_salaire):
        self.curseur.execute(
            "UPDATE employe SET salaire = %s WHERE id = %s",
            (nouveau_salaire, id_employe)
        )
        self.connexion.commit()

    def delete(self, id_employe):
        self.curseur.execute("DELETE FROM employe WHERE id = %s", (id_employe,))
        self.connexion.commit()

    def close(self):
        self.curseur.close()
        self.connexion.close()


if __name__ == "__main__":
    emp = Employe()
    print("Tous les employés :")
    for ligne in emp.read_all():
        print(ligne)
    emp.close()
