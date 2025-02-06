class Personne:
    def __init__(self, age=14):
        self.age = age
    
    def afficherAge(self):
        print(f"J'ai {self.age} ans")
    
    def bonjour(self):
        print("Hello")
    
    def modifierAge(self, nouvel_age):
        self.age = nouvel_age

class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")
    
    def afficherAge(self):
        print(f"J’ai {self.age} ans")

class Professeur(Personne):
    def __init__(self, age, matiereEnseignee):
        super().__init__(age)
        self.__matiereEnseignee = matiereEnseignee
    
    def enseigner(self):
        print("Le cours va commencer")

# Instanciation d'une Personne et d'un Eleve
personne = Personne()
eleve = Eleve()

# Affichage de l'âge par défaut de l'élève
eleve.afficherAge()

# Faire dire bonjour à l'élève et aller en cours
eleve.bonjour()
eleve.allerEnCours()

# Modifier l'âge de l'élève à 15 ans
eleve.modifierAge(15)
eleve.afficherAge()

# Création d'un professeur de 40 ans
professeur = Professeur(40, "Mathématiques")

# Faire dire bonjour au professeur et commencer le cours
professeur.bonjour()
professeur.enseigner()

import math
import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur
    
    def get_valeur(self):
        if self.valeur in ['J', 'Q', 'K']:
            return 10
        elif self.valeur == 'A':
            return 11  # L'As peut être 1 ou 11, cela sera géré dans le jeu
        else:
            return int(self.valeur)
    
    def __str__(self):
        return f"{self.valeur} de {self.couleur}"

class Jeu:
    def __init__(self):
        valeurs = [str(i) for i in range(2, 11)] + ['J', 'Q', 'K', 'A']
        couleurs = ['Coeur', 'Carreau', 'Trèfle', 'Pique']
        self.paquet = [Carte(valeur, couleur) for valeur in valeurs for couleur in couleurs]
        random.shuffle(self.paquet)
    
    def piocher(self):
        return self.paquet.pop() if self.paquet else None

def calculer_score(main):
    score = sum(carte.get_valeur() for carte in main)
    as_count = sum(1 for carte in main if carte.valeur == 'A')
    while score > 21 and as_count:
        score -= 10  # Convertir un As de 11 à 1
        as_count -= 1
    return score

def jouer_blackjack():
    jeu = Jeu()
    joueur_main = [jeu.piocher(), jeu.piocher()]
    croupier_main = [jeu.piocher(), jeu.piocher()]
    
    print("Main du joueur:", ", ".join(str(carte) for carte in joueur_main))
    print("Carte visible du croupier:", croupier_main[0])
    
    while calculer_score(joueur_main) < 21:
        action = input("Voulez-vous prendre une carte (p) ou passer (s) ? ")
        if action.lower() == 'p':
            joueur_main.append(jeu.piocher())
            print("Nouvelle main du joueur:", ", ".join(str(carte) for carte in joueur_main))
        else:
            break
    
    joueur_score = calculer_score(joueur_main)
    if joueur_score > 21:
        print("Vous avez dépassé 21. Vous avez perdu!")
        return
    
    print("Main complète du croupier:", ", ".join(str(carte) for carte in croupier_main))
    while calculer_score(croupier_main) < 17:
        croupier_main.append(jeu.piocher())
        print("Le croupier pioche une carte. Nouvelle main du croupier:", ", ".join(str(carte) for carte in croupier_main))
    
    croupier_score = calculer_score(croupier_main)
    print(f"Score du joueur: {joueur_score}, Score du croupier: {croupier_score}")
    
    if croupier_score > 21 or joueur_score > croupier_score:
        print("Félicitations, vous avez gagné!")
    elif joueur_score < croupier_score:
        print("Le croupier gagne.")
    else:
        print("Égalité!")

# Lancer une partie de Blackjack
jouer_blackjack()

