import mysql.connector

connexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password = "laplateforme123",
    database = "laplateforme"

)

cursor = connexion.cursor()


request = "SELECT * FROM etudiant;"
cursor.execute(request)

results = cursor.fetchall()


print("Liste des etudiants : ")
for etudiant in results :
    print(etudiant)


cursor.close()
connexion.close()