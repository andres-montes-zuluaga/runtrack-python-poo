class Livre:
    def __init__(self, titre, auteur, pages, disponible):
        self.__titre = titre
        self.__auteur = auteur
        self.__pages = pages
        self.__disponible = True
    
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
    
    def verification(self):
        if self.__disponible:
            return True
        else:
            return False
    
    def emprunter(self, livre):
        if livre.verification():
            self.__disponible = False
    
    def rendre(self, livre):
        if not livre.verification():
            self.__disponible = True
            print("Le livre est déjà disponible.")
        else:
            print("Le livre est déjà disponible.")

livre1 = Livre("Le Seigneur des Anneaux", "J.R.R. Tolkien", 1137, True)
livre1.afficher()
livre1.emprunter(livre1)
livre1.verification()
livre1.rendre(livre1)
livre1.verification()
