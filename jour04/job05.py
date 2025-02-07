class Forme:
    def aire(self):
        return 0

class Rectangle(Forme):
    def __init__(self, largueur, hauteur):
        self.largueur = largueur
        self.hauteur = hauteur
    
    def aire(self):
        return self.largueur * self.hauteur

class Cercle(Forme):
    def __init__(self, radius):
        self.radius = radius
    
    def aire(self):
        return 3.14 * self.radius * self.radius


rect1 = Rectangle(5, 10)
print(rect1.aire()) # 50

cerc1 = Cercle(5)
print(cerc1.aire()) # 78.5