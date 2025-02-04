class Commande:
    def __init__(self, numero, plats, prix_total, statut):
        self.__numero = numero
        self.__plats = {}  # dictionnaire des plats de la commande avec leurs prix
        self.__prix_total = prix_total
        self.__statut = statut  # en cours, terminée ou annulée
    
    def ajouter_plat(self, plat, prix):
        self.__plats[plat] = prix
        self.__prix_total += prix
    
    def calculer_total(self):
        self.__prix_total = 0
        for plat, prix in self.__plats.items():
            if prix < 0:
                print("Le prix d'un plat ne peut pas être négatif.")
                return
            elif not isinstance(prix, (int, float)):
                print("Le prix d'un plat doit être un nombre.")
                return
            else:
                self.__prix_total += prix
        self.__prix_total += self.calculer_TVA()
    
    def afficher(self):
        print(f"Numéro: {self.__numero}")
        print(f"Plats: {self.__plats}")
        print(f"Prix total: {self.__prix_total}")
        print(f"Statut: {self.__statut}")
    
    def calculer_TVA(self):
        return self.__prix_total * 0.2

commande1 = Commande(1, {}, 0, "en cours")
commande1.ajouter_plat("Pizza", 10)
commande1.ajouter_plat("Pâtes", 8)
commande1.ajouter_plat("Salade", 5)
commande1.calculer_total()
commande1.afficher()
