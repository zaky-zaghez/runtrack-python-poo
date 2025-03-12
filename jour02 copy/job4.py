import mysql.connector

# Connexion à la base de données
connexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="laplateforme123",
    database="laplateforme"
)

curseur = connexion.cursor()

# Exécution de la requête
requete = "SELECT nom, capacite FROM salle"
curseur.execute(requete)

# Récupération des résultats
resultats = curseur.fetchall()

# Affichage en console
print("Liste des salles et leur capacité :")
for salle in resultats:
    print(f"- {salle[0]} : {salle[1]} places")

# Fermeture de la connexion
curseur.close()
connexion.close()
