class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA
    
    def calculerPrixTTC(self):
        prixTTC = self.prixHT * (1 + self.TVA/100)
        return prixTTC
    
    def afficher(self):
        return f"Le produit {self.nom} coûte {self.prixHT} euros et a une TVA de {self.TVA}%. Le prix TTC est de {self.calculerPrixTTC()} euros."



produit1 = Produit("Le deuxième sex", 10, 20)
print(produit1.afficher())

produit2 = Produit("Goupil ou Face", 15, 20)
print(produit2.afficher())