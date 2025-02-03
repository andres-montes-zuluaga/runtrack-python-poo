"""
This file demonstrates how to define a `Personne` class 
with a method to display a person's introduction.
"""
class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
    
    def sePresenter(self):
        message = f"Je suis {self.prenom} {self.nom}"
        print(message)
        return None

personne1 = Personne("Lispector", "Clarisse")
personne1.sePresenter()

personne2 = Personne("Parra", "Violeta")
personne2.sePresenter()

personne3 = Personne("Allende", "Isabel")
personne3.sePresenter()

personne4 = Personne("Mistral", "Gabriela")
personne4.sePresenter()