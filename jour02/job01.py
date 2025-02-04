class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur  # __longueur est un attribut privé
        self.__largeur = largeur    # __largeur est un attribut privé

    def afficher(self):
        print(f"Longueur: {self.__longueur}")
        print(f"Largeur: {self.__largeur}")
    
    def modifier(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

rectangle1 = Rectangle(10, 5) # Création d'un objet de type Rectangle
rectangle1.afficher()       # Affichage des attributs de l'objet rectangle1

rectangle1.modifier(20, 10)    # Modification des attributs de l'objet rectangle1
rectangle1.afficher()    # Affichage des attributs de l'objet rectangle1