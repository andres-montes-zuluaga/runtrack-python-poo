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
        Personne.__init__(self, age)
        self.__matiereEnseignee = matiereEnseignee
    
    def enseigner(self):
        print("Le cours va commencer")



eleve1 = Eleve(0)
eleve1.bonjour()
eleve1.allerEnCours()
eleve1.modifierAge(16)
eleve1.afficherAge()

prof1 = Professeur(40, "Mathématiques")
prof1.modifierAge(40)
prof1.afficherAge()
prof1.bonjour()
prof1.enseigner()