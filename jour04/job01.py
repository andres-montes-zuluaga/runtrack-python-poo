class Personne:
    def __init__(self, age):
        self.age = 14
    
    def afficherAge(self):
        print(self.age)
    
    def bonjour(self):
        print("Hello!")
    
    def modifierAge(self, nouvel_age):
        self.age = nouvel_age

class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours.")
    
    def afficherAge(self):
        print(f"J'ai {self.age} ans")
    
class Professeur(Personne):
    def __init__(self, age, matiereEnseignee):
        super().__init__(age)
        self.__matiereEnseignee = matiereEnseignee
    
    def enseigner(self):
        print("Le cours va commencer")



personne1 = Personne(14)
personne1.bonjour()
personne1.modifierAge(25)
personne1.afficherAge()

professeur1 = Professeur(40, "Mathématiques")
professeur1.enseigner()


eleve1 = Eleve(16)
eleve1.afficherAge()
eleve1.allerEnCours()