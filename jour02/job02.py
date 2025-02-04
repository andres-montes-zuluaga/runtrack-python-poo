class Livre:
    def __init__(self, titre, auteur, pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__pages = pages
    
    def afficher(self):
        print(f"Titre: {self.__titre}")
        print(f"Auteur: {self.__auteur}")
        print(f"Nombre de pages: {self.__pages}")
    
    def modifier(self, titre, auteur, pages):
        if pages <= 0:
            print("Le changement n'est pas possible, le nombre de pages doit être un nombre entier positif.")
        else:
            self.__titre = titre
            self.__auteur = auteur
            self.__pages = pages

livre1 = Livre("Le Seigneur des Anneaux", "J.R.R. Tolkien", 1137)
livre1.afficher()
livre1.modifier("Le Hobbit", "J.R.R. Tolkien", -300)
livre1.afficher()