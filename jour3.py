class Ville:
    def __init__(self, nom: str, habitants: int):
        self.__nom = nom
        self.__habitants = habitants
    
    def ajouter_habitant(self):
        self.__habitants += 1
    
    def get_habitants(self):
        return self.__habitants
    
    def get_nom(self):
        return self.__nom

class Personne:
    def __init__(self, nom: str, age: int, ville: Ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville
        self.__ville.ajouter_habitant()
    
    def get_nom(self):
        return self.__nom
    
    def get_age(self):
        return self.__age
    
    def get_ville(self):
        return self.__ville.get_nom()

# Création des villes
paris = Ville("Paris", 1000000)
marseille = Ville("Marseille", 861635)

# Affichage des habitants initiaux
print(f"Population de la ville de {paris.get_nom()} : {paris.get_habitants()} habitants\n")
print(f"Population de la ville de {marseille.get_nom()} : {marseille.get_habitants()} habitants\n")

# Création des personnes
john = Personne("John", 45, paris)
myrtille = Personne("Myrtille", 4, paris)
chloe = Personne("Chloé", 18, marseille)

# Affichage des habitants après ajout des personnes
print(f"Mise a jour de la population de la ville de {paris.get_nom()} {paris.get_habitants()} habitants\n")
print(f"Mise a jour de la population de la ville de {marseille.get_nom()} {marseille.get_habitants()} habitants\n")

class CompteBancaire:
    def __init__(self, numero: int, nom: str, prenom: str, solde: float, decouvert: bool = False):
        self.__numero = numero
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert
    
    def afficher(self):
        print(f"Compte N°{self.__numero} - Titulaire: {self.__prenom} {self.__nom} - Solde: {self.__solde} €")
    
    def afficherSolde(self):
        print(f"Solde du compte {self.__numero}: {self.__solde} €")
    
    def versement(self, montant: float):
        if montant > 0:
            self.__solde += montant
            print(f"Versement de {montant} € effectué. Nouveau solde: {self.__solde} €")
        else:
            print("Le montant du versement doit être positif.")
    
    def retrait(self, montant: float):
        if montant > 0:
            if self.__solde - montant >= 0 or self.__decouvert:
                self.__solde -= montant
                print(f"Retrait de {montant} € effectué. Nouveau solde: {self.__solde} €")
            else:
                print("Fonds insuffisants pour effectuer le retrait.")
        else:
            print("Le montant du retrait doit être positif.")
    
    def agios(self, taux: float = 0.05):
        if self.__solde < 0:
            self.__solde *= (1 + taux)
            print(f"Agios appliqués. Nouveau solde: {self.__solde} €")
    
    def virement(self, compte_destinataire, montant: float):
        if montant > 0 and (self.__solde - montant >= 0 or self.__decouvert):
            self.__solde -= montant
            compte_destinataire.versement(montant)
            print(f"Virement de {montant} € effectué vers le compte {compte_destinataire.__numero}")
        else:
            print("Virement impossible: fonds insuffisants.")

# Création des comptes
compte1 = CompteBancaire(12345, "Dupont", "Jean", 1000.0)
compte2 = CompteBancaire(67890, "Martin", "Sophie", -200.0, decouvert=True)

# Affichage des comptes
compte1.afficher()
compte2.afficher()

# Vérification du solde
compte1.afficherSolde()
compte2.afficherSolde()

# Effectuer un virement du premier compte vers le second
compte1.virement(compte2, 200.0)

# Affichage des soldes après virement
compte1.afficherSolde()
compte2.afficherSolde()

class Tache:
    def __init__(self, titre: str, description: str, statut: str = "À faire"):
        self.titre = titre
        self.description = description
        self.statut = statut

    def marquerCommeFinie(self):
        self.statut = "Terminée"

    def __str__(self):
        return f"{self.titre} - {self.description} [{self.statut}]"

class ListeDeTaches:
    def __init__(self):
        self.taches = []
    
    def ajouterTache(self, tache: Tache):
        self.taches.append(tache)
    
    def supprimerTache(self, titre: str):
        self.taches = [t for t in self.taches if t.titre != titre]
    
    def marquerCommeFinie(self, titre: str):
        for t in self.taches:
            if t.titre == titre:
                t.marquerCommeFinie()
                break
    
    def afficherListe(self):
        return [str(t) for t in self.taches]
    
    def filterListe(self, statut: str):
        return [str(t) for t in self.taches if t.statut == statut]

# Test du code
tache1 = Tache("Faire les courses", "Acheter du pain et du lait")
tache2 = Tache("Réviser Python", "Pratiquer les classes et objets")
tache3 = Tache("Sport", "Faire 30 minutes de course")

listeTaches = ListeDeTaches()
listeTaches.ajouterTache(tache1)
listeTaches.ajouterTache(tache2)
listeTaches.ajouterTache(tache3)

# Marquer une tâche comme terminée
listeTaches.marquerCommeFinie("Faire les courses")

# Supprimer une tâche
listeTaches.supprimerTache("Sport")

# Afficher toutes les tâches
print("Toutes les tâches:", listeTaches.afficherListe())

# Afficher uniquement les tâches à faire
print("Tâches à faire:", listeTaches.filterListe("À faire"))

class Joueur:
    def __init__(self, nom: str, numero: int, position: str):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.buts = 0
        self.passes_decisives = 0
        self.cartons_jaunes = 0
        self.cartons_rouges = 0

    def marquerUnBut(self):
        self.buts += 1

    def effectuerUnePasseDecisive(self):
        self.passes_decisives += 1

    def recevoirUnCartonJaune(self):
        self.cartons_jaunes += 1

    def recevoirUnCartonRouge(self):
        self.cartons_rouges += 1

    def afficherStatistiques(self):
        return (f"Joueur {self.nom} (#{self.numero}, {self.position}) - Buts: {self.buts}, 
                Passes décisives: {self.passes_decisives}, Cartons jaunes: {self.cartons_jaunes}, 
                Cartons rouges: {self.cartons_rouges}")

class Equipe:
    def __init__(self, nom: str):
        self.nom = nom
        self.joueurs = []
    
    def ajouterJoueur(self, joueur: Joueur):
        self.joueurs.append(joueur)
    
    def afficherStatistiquesJoueurs(self):
        for joueur in self.joueurs:
            print(joueur.afficherStatistiques())
    
    def mettreAJourStatistiquesJoueur(self, nom: str, action: str):
        for joueur in self.joueurs:
            if joueur.nom == nom:
                if action == "but":
                    joueur.marquerUnBut()
                elif action == "passe":
                    joueur.effectuerUnePasseDecisive()
                elif action == "jaune":
                    joueur.recevoirUnCartonJaune()
                elif action == "rouge":
                    joueur.recevoirUnCartonRouge()
                break

# Création des équipes
equipe1 = Equipe("Tigers")
equipe2 = Equipe("Eagles")

# Création des joueurs
joueur1 = Joueur("Alice", 10, "Attaquant")
joueur2 = Joueur("Bob", 5, "Milieu")
joueur3 = Joueur("Charlie", 1, "Gardien")

# Ajout des joueurs aux équipes
equipe1.ajouterJoueur(joueur1)
equipe1.ajouterJoueur(joueur2)
equipe2.ajouterJoueur(joueur3)

# Affichage des statistiques avant match
print("Statistiques avant match :")
equipe1.afficherStatistiquesJoueurs()
equipe2.afficherStatistiquesJoueurs()

# Simulation du match
equipe1.mettreAJourStatistiquesJoueur("Alice", "but")
equipe1.mettreAJourStatistiquesJoueur("Bob", "passe")
equipe2.mettreAJourStatistiquesJoueur("Charlie", "jaune")

# Affichage des statistiques après match
print("\nStatistiques après match :")
equipe1.afficherStatistiquesJoueurs()
equipe2.afficherStatistiquesJoueurs()


import random

class Personnage:
    def __init__(self, nom: str, vie: int):
        self.nom = nom
        self.vie = vie

    def attaquer(self, adversaire):
        degats = random.randint(5, 15)
        adversaire.vie -= degats
        print(f"{self.nom} attaque {adversaire.nom} et inflige {degats} points de dégâts!")
        if adversaire.vie < 0:
            adversaire.vie = 0
        print(f"Il reste {adversaire.vie} points de vie à {adversaire.nom}.")

    def est_vivant(self):
        return self.vie > 0

class Jeu:
    def __init__(self):
        self.niveau = None

    def choisirNiveau(self):
        while True:
            try:
                niveau = int(input("Choisissez un niveau de difficulté (1: Facile, 2: Moyen, 3: Difficile) : "))
                if niveau in [1, 2, 3]:
                    self.niveau = niveau
                    break
                else:
                    print("Veuillez entrer un nombre entre 1 et 3.")
            except ValueError:
                print("Entrée invalide. Veuillez entrer un nombre entier.")

    def lancerJeu(self):
        if self.niveau == 1:
            vie_joueur, vie_ennemi = 100, 50
        elif self.niveau == 2:
            vie_joueur, vie_ennemi = 75, 75
        else:
            vie_joueur, vie_ennemi = 50, 100

        joueur = Personnage("Joueur", vie_joueur)
        ennemi = Personnage("Ennemi", vie_ennemi)

        print(f"Le combat commence ! {joueur.nom} ({joueur.vie} PV) contre {ennemi.nom} ({ennemi.vie} PV)")

        while joueur.est_vivant() and ennemi.est_vivant():
            input("Appuyez sur Entrée pour attaquer...")
            joueur.attaquer(ennemi)
            if ennemi.est_vivant():
                ennemi.attaquer(joueur)

        if joueur.est_vivant():
            print("Félicitations ! Vous avez vaincu l'ennemi !")
        else:
            print("Game Over. L'ennemi vous a battu.")

# Lancer le jeu
jeu = Jeu()
jeu.choisirNiveau()
jeu.lancerJeu()

