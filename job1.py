class Operation:
    def __init__(self, nombre1=0, nombre2=0):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def addition(self):
        resultat = self.nombre1 + self.nombre2
        print(f"Le résultat de l'addition est {resultat}")


operation_instance = Operation(12, 3)


print(operation_instance)


print(f"Le nombre1 est {operation_instance.nombre1}")
print(f"Le nombre2 est {operation_instance.nombre2}")


operation_instance.addition()

class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        return f"Je suis {self.prenom} {self.nom}"


personne1 = Personne("Dupont", "Jean")
personne2 = Personne("Martin", "Sophie")
personne3 = Personne("Durand", "Paul")


print(personne1.SePresenter())
print(personne2.SePresenter())
print(personne3.SePresenter())

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        print(f"Les coordonnées du point sont ({self.x}, {self.y})")
    
    def afficherX(self):
        print(f"Coordonnée X: {self.x}")
    
    def afficherY(self):
        print(f"Coordonnée Y: {self.y}")
    
    def changerX(self, new_x):
        self.x = new_x
    
    def changerY(self, new_y):
        self.y = new_y


point = Point(3, 5)
point.afficherLesPoints()
point.afficherX()
point.afficherY()
point.changerX(10)
point.changerY(15)
point.afficherLesPoints()

class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""
    
    def vieillir(self):
        self.age += 1
    
    def nommer(self, nom):
        self.prenom = nom
    

animal = Animal()
print(f"L'age de l'animal {animal.age} ans.")
animal.vieillir()
print(f"L'age de l'animal apres appel de la methode vieillir {animal.age} ans.")
animal.nommer("Luna")
print(f"L'animal se nomme {animal.prenom}")

class Personnage:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def gauche(self):
        self.x -= 1
    
    def droite(self):
        self.x += 1
    
    def haut(self):
        self.y -= 1
    
    def bas(self):
        self.y += 1
    
    def position(self):
        return (self.x, self.y)


personnage = Personnage(5, 5)
print(f"Position initiale: {personnage.position()}")
personnage.gauche()
print(f"Après déplacement à gauche: {personnage.position()}")
personnage.droite()
personnage.haut()
print(f"Après déplacement en haut: {personnage.position()}")
personnage.bas()
print(f"Après déplacement en bas: {personnage.position()}")

class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon
    
    def changerRayon(self, nouveau_rayon):
        self.rayon = nouveau_rayon
    
    def afficherInfos(self):
        print(f"Cercle de rayon: {self.rayon}")
        print(f"Diamètre: {self.diametre()}")
        print(f"Circonférence: {self.circonference():.2f}")
        print(f"Aire: {self.aire():.2f}")
    
    def circonference(self):
        return 2 * math.pi * self.rayon
    
    def aire(self):
        return math.pi * self.rayon ** 2
    
    def diametre(self):
        return 2 * self.rayon


cercle1 = Cercle(4)
cercle2 = Cercle(7)

print("Informations du premier cercle:")
cercle1.afficherInfos()
print("\nInformations du deuxième cercle:")
cercle2.afficherInfos()


class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    
    def CalculerPrixTTC(self):
        return self.prixHT * (1 + self.TVA / 100)

    
    def afficher(self):
        return f"Nom: {self.nom}, Prix HT: {self.prixHT}€, TVA: {self.TVA}%, Prix TTC: {self.CalculerPrixTTC()}€"

    
    def modifier_nom(self, nouveau_nom):
        self.nom = nouveau_nom

    def modifier_prix(self, nouveau_prix):
        self.prixHT = nouveau_prix

    
    def get_nom(self):
        return self.nom

    def get_prixHT(self):
        return self.prixHT

    def get_TVA(self):
        return self.TVA

    def get_prixTTC(self):
        return self.CalculerPrixTTC()



produit1 = Produit("Produit A", 100, 20)
produit2 = Produit("Produit B", 150, 5)


print(f"Prix TTC de {produit1.get_nom()} : {produit1.get_prixTTC()}€")
print(f"Prix TTC de {produit2.get_nom()} : {produit2.get_prixTTC()}€")


produit1.modifier_nom("Produit A - Modifié")
produit1.modifier_prix(120)

produit2.modifier_nom("Produit B - Modifié")
produit2.modifier_prix(140)


print(produit1.afficher())
print(produit2.afficher())
