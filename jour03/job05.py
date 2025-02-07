"""
This script demonstrates the use of classes and objects in a simple game.
The `Personnage` class represents a character with a name and health points.
The `Jeu` class manages the game flow, including selecting difficulty levels and initiating battles.
"""

class Personnage:
    def __init__(self, nom, vie):
        self.nom = str(nom)
        self.vie = int(vie)
    
    def attaquer(self):
        self.vie -= 10

class Jeu:
    def choisirNiveau(self):
        niveau_valid = False
        while not niveau_valid:
            try:
                niveau = int(input("Entrez le niveau de difficulté (1-6): "))
                if niveau < 1 or niveau > 6:
                    print("Niveau invalide!")
                else:
                    niveau_valid = True
                    return niveau
            except ValueError:
                print("Entre un nombre entier!")

    def lancerJeu(self, nom, vie, niveau):
        if niveau == 1:
            self.hero = Personnage(nom, vie)
            self.ennemi = Personnage("GOBLIN", 10)
        elif niveau == 2:
            self.hero = Personnage(nom, vie)
            self.ennemi = Personnage("ORC", 20)
        elif niveau == 3:
            self.hero = Personnage(nom, vie)
            self.ennemi = Personnage("DRAGON", 30)
        elif niveau == 4:
            self.hero = Personnage(nom, vie)
            self.ennemi = Personnage("HYDRE", 40)
        elif niveau == 5:
            self.hero = Personnage(nom, vie)
            self.ennemi = Personnage("CERBÈRE", 50)
        elif niveau == 6:
            self.hero = Personnage(nom, vie)
            self.ennemi = Personnage("TITAN", 60)
    
    def verifierSante(self):
        print(f"Hero: {self.hero.vie} PV")
        print(f"Ennemi: {self.ennemi.vie} PV")
    
    def gagnante(self):
        if self.hero.vie <= 0:
            print("Vous avez perdu!")
        elif self.ennemi.vie <= 0:
            print("Vous avez gagné!")
        else:
            print("Le combat continue...")

# Game starts here
print("Bienvenue dans le jeu!")
nom = input("Entrez le nom de votre personnage: ")


jeu = Jeu() # Objet jeu creation because the Jeu class has no constructor
jeu.lancerJeu(nom, 100, jeu.choisirNiveau())

print(f"Le combat commence! {jeu.hero.nom} vs {jeu.ennemi.nom}")
jeu.hero.attaquer()
jeu.ennemi.attaquer()
jeu.verifierSante()
jeu.gagnante()