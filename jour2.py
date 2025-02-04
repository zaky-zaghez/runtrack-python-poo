class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def get_longueur(self):
        return self.__longueur

    def set_longueur(self, longueur):
        self.__longueur = longueur

    def get_largeur(self):
        return self.__largeur

    def set_largeur(self, largeur):
        self.__largeur = largeur

rectangle = Rectangle(10, 5)
print("Longueur:", rectangle.get_longueur())
print("Largeur:", rectangle.get_largeur())

rectangle.set_longueur(15)
rectangle.set_largeur(8)
print("Nouvelle longueur:", rectangle.get_longueur())
print("Nouvelle largeur:", rectangle.get_largeur())

class Livre:
    def __init__(self, titre, auteur, nombre_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nombre_pages = nombre_pages if isinstance(nombre_pages, int) and nombre_pages > 0 else 0

    def get_titre(self):
        return self.__titre

    def set_titre(self, titre):
        self.__titre = titre

    def get_auteur(self):
        return self.__auteur

    def set_auteur(self, auteur):
        self.__auteur = auteur

    def get_nombre_pages(self):
        return self.__nombre_pages

    def set_nombre_pages(self, nombre_pages):
        if isinstance(nombre_pages, int) and nombre_pages > 0:
            self.__nombre_pages = nombre_pages
        else:
            print("Erreur : Le nombre de pages doit etre un entier positif.")

livre = Livre("Le Petit Prince", "Antoine de Saint-Exupery", 96)
print("Titre:", livre.get_titre())
print("Auteur:", livre.get_auteur())
print("Nombre de pages:", livre.get_nombre_pages())

livre.set_nombre_pages(120)
print("Nouveau nombre de pages:", livre.get_nombre_pages())

livre.set_nombre_pages(-5) 

class Livre:
    def __init__(self, titre, auteur, nombre_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nombre_pages = nombre_pages if isinstance(nombre_pages, int) and nombre_pages > 0 else 0
        self.__disponible = True

    def get_titre(self):
        return self.__titre

    def set_titre(self, titre):
        self.__titre = titre

    def get_auteur(self):
        return self.__auteur

    def set_auteur(self, auteur):
        self.__auteur = auteur

    def get_nombre_pages(self):
        return self.__nombre_pages

    def set_nombre_pages(self, nombre_pages):
        if isinstance(nombre_pages, int) and nombre_pages > 0:
            self.__nombre_pages = nombre_pages
        else:
            print("Erreur : Le nombre de pages doit etre un entier positif.")

    def verification(self):
        return self.__disponible

    def emprunter(self):
        if self.verification():
            self.__disponible = False
            print("Le livre a ete emprunte.")
        else:
            print("Le livre n'est pas disponible.")

    def rendre(self):
        if not self.verification():
            self.__disponible = True
            print("Le livre a ete rendu.")
        else:
            print("Le livre etait deja disponible.")

livre = Livre("Le Petit Prince", "Antoine de Saint-Exupery", 96)
print("Titre:", livre.get_titre())
print("Auteur:", livre.get_auteur())
print("Nombre de pages:", livre.get_nombre_pages())
print("Disponible:", livre.verification())

livre.emprunter()
print("Disponible apres emprunt:", livre.verification())

livre.rendre()
print("Disponible apres retour:", livre.verification())

class Student:
    def __init__(self, nom, prenom, numero_etudiant):
        self.__nom = nom
        self.__prenom = prenom
        self.__numero_etudiant = numero_etudiant
        self.__credits = 0
        self.__level = self.__student_eval()

    def get_nom(self):
        return self.__nom

    def get_prenom(self):
        return self.__prenom

    def get_numero_etudiant(self):
        return self.__numero_etudiant

    def get_credits(self):
        return self.__credits

    def add_credits(self, credits):
        if isinstance(credits, int) and credits > 0:
            self.__credits += credits
            self.__level = self.__student_eval()
        else:
            print("Erreur : Le nombre de credits doit etre un entier positif.")

    def __student_eval(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Tres bien"
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"

    def student_info(self):
        print(f"Nom = {self.__nom}")
        print(f"Prenom = {self.__prenom}")
        print(f"id = {self.__numero_etudiant}")
        print(f"Niveau = {self.__level}")

student = Student("John", "Doe", 145)
student.add_credits(70)
print(f"Le nombre de credits de {student.get_nom()} {student.get_prenom()} est de {student.get_credits()} points")
student.student_info()

class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = False
        self.__reservoir = 50

    def get_marque(self):
        return self.__marque

    def set_marque(self, marque):
        self.__marque = marque

    def get_modele(self):
        return self.__modele

    def set_modele(self, modele):
        self.__modele = modele

    def get_annee(self):
        return self.__annee

    def set_annee(self, annee):
        self.__annee = annee

    def get_kilometrage(self):
        return self.__kilometrage

    def set_kilometrage(self, kilometrage):
        self.__kilometrage = kilometrage

    def get_en_marche(self):
        return self.__en_marche

    def demarrer(self):
        if self.__verifier_plein() > 5:
            self.__en_marche = True
            print("La voiture demarre.")
        else:
            print("Carburant insuffisant pour demarrer.")

    def arreter(self):
        self.__en_marche = False
        print("La voiture est arretee.")

    def __verifier_plein(self):
        return self.__reservoir

voiture = Voiture("Toyota", "Corolla", 2020, 30000)
print(f"Marque: {voiture.get_marque()}")
print(f"Modele: {voiture.get_modele()}")
print(f"Annee: {voiture.get_annee()}")
print(f"Kilometrage: {voiture.get_kilometrage()} km")
print(f"En marche: {voiture.get_en_marche()}")

voiture.demarrer()
print(f"En marche apres demarrage: {voiture.get_en_marche()}")

voiture.arreter()
print(f"En marche apres arret: {voiture.get_en_marche()}")

class Commande:
    def __init__(self, numero_commande):
        self.__numero_commande = numero_commande
        self.__plats = {}  # Dictionnaire contenant les plats et leurs prix
        self.__statut = "en cours"

    def ajouter_plat(self, nom_plat, prix):
        if nom_plat not in self.__plats:
            self.__plats[nom_plat] = prix
            print(f"Le plat {nom_plat} a ete ajoute a la commande.")
        else:
            print(f"Le plat {nom_plat} est deja dans la commande.")

    def annuler_commande(self):
        self.__statut = "annulee"
        self.__plats.clear()
        print("La commande a ete annulee.")

    def __calculer_total(self):
        return sum(self.__plats.values())

    def calculer_tva(self, taux=0.2):
        total = self.__calculer_total()
        return total * taux

    def afficher_commande(self):
        print(f"Commande n°{self.__numero_commande}")
        print(f"Statut: {self.__statut}")
        print("Plats commandes:")
        for plat, prix in self.__plats.items():
            print(f"- {plat}: {prix}€")
        total = self.__calculer_total()
        tva = self.calculer_tva()
        print(f"Total a payer (hors TVA): {total}€")
        print(f"TVA (20%): {tva}€")
        print(f"Total a payer (TTC): {total + tva}€")


# Test de la classe
commande = Commande(101)
commande.ajouter_plat("Pizza Margherita", 12)
commande.ajouter_plat("Pates Carbonara", 15)
commande.ajouter_plat("Tiramisu", 7)
commande.afficher_commande()
commande.annuler_commande()
commande.afficher_commande()
