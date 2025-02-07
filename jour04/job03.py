class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur
    
    def perimetre(self):
        return 2 * (self.__longueur + self.__largeur)
    
    def surface(self):
        return self.__longueur * self.__largeur
    
    def afficher(self):
        print(f"\nLongueur: {self.__longueur}")
        print(f"Largeur: {self.__largeur}")
        print(f"Perimetre: {self.perimetre()}")
        print(f"Surface: {self.surface()}")
    
    def mutateurs(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur
    
class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.__hauteur = hauteur
    
    def volume(self):
        return self.surface() * self.__hauteur
    
    def afficher(self):
        super().afficher()
        print(f"Hauteur: {self.__hauteur}")
        print(f"Volume: {self.volume()}")
    
    def mutateurs(self, longueur, largeur, hauteur):
        super().mutateurs(longueur, largeur)
        self.__hauteur = hauteur



rectangle = Rectangle(5, 10)
rectangle.afficher()
rectangle.mutateurs(10, 20)
rectangle.afficher()


parallelepipede = Parallelepipede(4, 8, 20)
parallelepipede.afficher()
parallelepipede.mutateurs(8, 16, 40)
parallelepipede.afficher()