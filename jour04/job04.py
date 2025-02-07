class Forme:
    def aire(self):
        return 0

class Rectangle(Forme):
    def __init__(self, largueur, hauteur):
        self.largueur = largueur
        self.hauteur = hauteur
    
    def aire(self):
        return self.largueur * self.hauteur

rect1 = Rectangle(5, 10)
print(rect1.aire()) # 50