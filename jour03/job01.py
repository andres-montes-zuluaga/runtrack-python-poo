"""
This script demonstrates the use of classes and objects.
The `Ville` class represents a city with a name and population.
The `Personne` class represents a person who can increase the population of a city.
"""

class Ville:
    def __init__(self, nom, habitants):
        self.__nom = nom
        self.__habitants = habitants
    
    def afficher(self):
        print(f"Nom: {self.__nom}")
        print(f"Population : {self.__habitants}")

    def ajouterPopulation(self):
        self.__habitants += 1

class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville
        self.__ville.ajouterPopulation() # Add a person to the city

# Add two cities
ville1 = Ville("Paris", 1000000)
ville2 = Ville("Marseille", 861635)

# Print the initial number of inhabitants
print(f"Population de la ville de {ville1._Ville__nom} : {ville1._Ville__habitants}")
print(f"Population de la ville de {ville2._Ville__nom} : {ville2._Ville__habitants}")

# Add three people to the cities
personne1 = Personne("John", 45, ville1)
personne2 = Personne("Myrtille", 4, ville1)
personne3 = Personne("Chloé", 18, ville2)

# Print the updated number of inhabitants
print(f"Mise a jour de la population de la ville de {ville1._Ville__nom} : {ville1._Ville__habitants}")
print(f"Mise a jour de la population de la ville de {ville2._Ville__nom} : {ville2._Ville__habitants}")