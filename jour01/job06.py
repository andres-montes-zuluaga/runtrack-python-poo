"""
This file demonstrates how to define an `Animal` class 
with methods to age the animal and change its name.
"""
class Animal:
    
    def __init__(self, prenom):
        self.age = 0
        self.prenom = prenom
    
    def vieillir(self):
        self.age += 1
        return None
    
    def nommer(self, prenom):
        self.prenom = prenom
        return None

animal1 = Animal("Rex")

print(f"L'âge de l'animal est {animal1.age} ans")

animal1.vieillir()

print(f"L'âge de l'animal est {animal1.age} ans")

animal1.nommer("Max")

print(f"L'animal se nomme {animal1.prenom}")