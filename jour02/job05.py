class Voiture:
    def __init__(self, marque, modele, anne, km, en_marche, reservoir):
        self.__marque = marque
        self.__modele = modele
        self.__anne = anne
        self.__km = km
        self.__en_marche = False
        self.__reservoir = 50
    
    def demarrer(self):
        if not self.__en_marche:
            if self.__verifier_plein(self.__reservoir) < 5:
                print("Le réservoir est vide.")
            else:
                self.__en_marche = True
                print("La voiture démarre.")
        else:
            self.__en_marche = True
            print("La voiture est déjà en marche.")
    
    def arreter(self):
        if not self.__en_marche:
            print("La voiture est déjà arrêtée.")
        else:
            self.__en_marche = False
            print("La voiture s'arrête.")
    
    def __verifier_plein(self, reservoir):
        return reservoir
    
voiture1 = Voiture("Peugeot", "208", 2015, 100000, False, 4) # reservoir = 4, mais est initialisé à 50 par defaut
voiture1.demarrer()
voiture1.demarrer()
voiture1.arreter()
voiture1.arreter()
# Expected output:
# La voiture démarre.
# La voiture est déjà en marche.
# La voiture s'arrête.
# La voiture est déjà arrêtée.