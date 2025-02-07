"""
This script demonstrates the use of classes and objects in managing bank accounts.
The `CompteBancaire` class represents a bank account with various operations such as deposit, withdrawal, and transfer.
"""

class CompteBancaire:
    def __init__(self, num_compte, nom, prenom, solde, decouvert):
        self.__num_compte = num_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.decouvert = decouvert
    
    def afficher(self):
        print(f"Nom: {self.__nom}")
        print(f"Prénom: {self.__prenom}")
        print(f"Numéro de compte: {self.__num_compte}")
        print(f"Solde: {self.__solde}")
    
    def afficherSolde(self):
        print(self.__solde)
    
    def versement(self, montant):
        self.__solde += montant
    
    def retrait(self, montant):
        if self.decouvert:
            self.__solde -= montant
        elif self.decouvert == False and self.__solde < montant:
            print("Solde insuffisant")
        else:
            self.__solde -= montant
    
    def agios(self):
        if self.__solde < 0:
            self.__solde += self.__solde * 0.05
            print("Agios de 5% appliqués")
        else:
            print("Pas d'agios")
    
    def virement(self, autre_compte, montant):
        if self.__solde >= montant:
            self.__solde -= montant
            autre_compte.versement(montant)
            print(f"Virement de {montant} effectué de {self.__num_compte} à {autre_compte.__num_compte}")
        else:
            print("Solde insuffisant pour le virement")


compte1 = CompteBancaire(123, "Doe", "John", 1000, True)
compte1.afficher()
compte1.afficherSolde()
compte1.versement(500)
compte1.afficherSolde()
compte1.retrait(2000)
compte1.afficherSolde()
compte1.retrait(500)
compte1.afficher()
compte1.agios()
compte1.versement(10000)
compte1.afficher()

compte2 = CompteBancaire(456, "Doe", "Jane", -100, True)
compte2.afficher()
compte1.virement(compte2, 100)
compte2.afficher()
compte2.afficher()
compte1.afficher()