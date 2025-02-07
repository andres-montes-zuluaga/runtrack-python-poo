class Vehicule:
    def __init__(self, marque, modele, anne, prix):
        self.marque = marque
        self.modele = modele
        self.anne = anne
        self.prix = prix
    
    def demarrer(self):
        print("\nAttention, je roule")
    
class Voiture(Vehicule):
    def __init__(self, marque, modele, anne, prix, portes):
        super().__init__(marque, modele, anne, prix)
        self.portes = 4
    
    def informationsVehicule(self):
        print(f"\nMarque = {self.marque}")
        print(f"Modele = {self.modele}")
        print(f"Annee = {self.anne}")
        print(f"Prix = {self.prix}")
        print(f"Portes = {self.portes}")
    
    def demarrer(self):
        print(f"\nVoiture {self.marque} demarree")

class Moto(Vehicule):
    def __init__(self, marque, modele, anne, prix, roue):
        super().__init__(marque, modele, anne, prix)
        self.roue = 2
    
    def informationsVehicule(self):
        print(f"\nMarque = {self.marque}")
        print(f"Modele = {self.modele}")
        print(f"Annee = {self.anne}")
        print(f"Prix = {self.prix}")
        print(f"Roue = {self.roue}")
    
    def demarrer(self):
        print(f"\nMoto {self.marque} demarree")


voiture = Voiture("Mercedes", "Classe A", 2020, 18500, 4)
voiture.informationsVehicule()
voiture.demarrer()

moto1 = Moto("Yamaha", "1200 Vmax", 1987, 4500, 2)
moto1.informationsVehicule()
moto1.demarrer()