"""
This file demonstrates how to define a `Point` class 
with methods to display and change the coordinates 
of a point in a 2D plane.
"""
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def afficherLesPoints(self):
        print(f"({self.x}, {self.y})")
        return None
    
    def afficherx(self):
        print(f"x = {self.x}")
        return None
    
    def affichery(self):
        print(f"y = {self.y}")
        return None
    
    def changerx(self):
        self.x = input("Entrez la nouvelle valeur de x: ")
        return None
    
    def changery(self):
        self.y = input("Entrez la nouvelle valeur de y: ")
        return None

point1 = Point(2, 3)
point1.afficherLesPoints()
point1.afficherx()
point1.affichery()
pointx2 = point1.changerx()
pointy2 = point1.changery()

print(f"Le nouveau point est ({point1.x}, {point1.y})")