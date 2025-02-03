"""
This file demonstrates how to define a `Personnage` class 
with methods to move a character 
in a 2D plane and display its position.
"""
class Personnage:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def gauche(self):
        self.x -= 1
        return None
    
    def droite(self):
        self.x += 1
        return None
    
    def bas(self):
        self.y -= 1
        return None
    
    def haut(self):
        self.y += 1
        return None
    
    def position(self):
        print(f"({self.x}, {self.y})")
        return None

personnage1 = Personnage(2, 3)
personnage1.gauche()
personnage1.bas()
personnage1.position()
personnage1.droite()
personnage1.haut()
personnage1.position()
# Expected: (1, 2) and (2, 3)