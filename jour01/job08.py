"""
This file demonstrates how to define a `Cercle` class 
with methods to calculate the circumference, 
area, and diameter, as well as to display this information.
"""
class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon
    
    def changerRayon(self, rayon):
        self.rayon = rayon
        return None
    
    def circonference(self):
        circonference = 2 * 3.1415926 * self.rayon
        return circonference
    
    def aire(self):
        aire = 3.1415926 * self.rayon ** 2
        return aire
    
    def diametre(self):
        diametre = 2 * self.rayon
        return diametre
    
    def afficherInfos(self):
        print(f"Le rayon est {self.rayon}")
        print(f"Le diamètre est {self.diametre()}")
        print(f"La circonférence est {self.circonference()}")
        print(f"L'aire est {self.aire()}")
        return None

cercle1 = Cercle(4)
cercle1.afficherInfos()

cercle2 = Cercle(7)
cercle2.afficherInfos()