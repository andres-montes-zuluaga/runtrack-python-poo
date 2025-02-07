"""
This script demonstrates the use of classes and objects in managing a football team.
The `Joueur` class represents a player with various statistics.
The `EquipeDeFoot` class manages a team of players and their statistics.
"""

class Joueur:
    def __init__(self, nom, numero, position, buts_marques, passes_decisives, cartons_jaunes, cartons_rouges):
        self._nom = nom
        self._numero = numero
        self._position = position
        self._buts_marques = buts_marques
        self._passes_decisives = passes_decisives
        self._cartons_jaunes = cartons_jaunes
        self._cartons_rouges = cartons_rouges
    
    def marquerUnBut(self):
        self._buts_marques += 1
    
    def effectuerUnePasseDecisive(self):
        self._passes_decisives += 1
    
    def recevoirUnCartonJaune(self):
        self._cartons_jaunes += 1
    
    def recevoirUnCartonRouge(self):
        self._cartons_rouges += 1
    
    def afficherStatistiques(self):
        print(f"Nom: {self._nom}")
        print(f"Numéro: {self._numero}")
        print(f"Position: {self._position}")
        print(f"Buts marqués: {self._buts_marques}")
        print(f"Passes décisives: {self._passes_decisives}")
        print(f"Cartons jaunes: {self._cartons_jaunes}")
        print(f"Cartons rouges: {self._cartons_rouges}")
        print()

class EquipeDeFoot:
    def __init__(self, nom, liste_joueurs):
        self.__nom = nom
        self.__liste_joueurs = liste_joueurs
    
    def ajouterJoueur(self, joueur):
        self.__liste_joueurs.append(joueur)
    
    def afficherStatistiquesJoueurs(self):
        print(f"Statistiques de l'équipe {self.__nom}:")
        for joueur in self.__liste_joueurs:
            joueur.afficherStatistiques()
    
    def mettreAJourStatistiquesJoueur(self, nom, buts_marques, passes_decisives, cartons_jaunes, cartons_rouges):
        for joueur in self.__liste_joueurs:
            if joueur._nom == nom:
                joueur._buts_marques = buts_marques
                joueur._passes_decisives = passes_decisives
                joueur._cartons_jaunes = cartons_jaunes
                joueur._cartons_rouges = cartons_rouges

# Add 5 players to OM
joueur1_om = Joueur("Camille Cousin", 10, "Attaquant", 5, 3, 1, 0)
joueur2_om = Joueur("Mélissa Dupont", 7, "Milieu", 2, 4, 2, 0)
joueur3_om = Joueur("Jean Dupuis", 3, "Défenseur", 0, 1, 3, 1)
joueur4_om = Joueur("Marie Durand", 1, "Gardien", 0, 0, 0, 0)
joueur5_om = Joueur("Paul Dupont", 9, "Attaquant", 3, 2, 0, 0)
# OM team creation
equipe_om = EquipeDeFoot("Olympique de Marseille", [joueur1_om, joueur2_om, joueur3_om, joueur4_om, joueur5_om])

# Add 5 players to Paris Saint-Germain
joueur1_psg = Joueur("Amelie Dupont", 10, "Attaquant", 7, 3, 2, 0)
joueur2_psg = Joueur("Clarisse Martin", 11, "Milieu", 4, 6, 2, 0)
joueur3_psg = Joueur("Justine Telmat", 3, "Défenseur", 0, 1, 3, 1)
joueur4_psg = Joueur("Delia Gorog", 1, "Gardien", 0, 0, 1, 0)
joueur5_psg = Joueur("Melissa Felenbok", 7, "Attaquant", 6, 3, 0, 0)
# Paris Saint-Germain team creation
equipe_psg = EquipeDeFoot("Paris Saint-Germain", [joueur1_psg, joueur2_psg, joueur3_psg, joueur4_psg, joueur5_psg])

# Print the statistics of all players in each team
equipe_om.afficherStatistiquesJoueurs()
equipe_psg.afficherStatistiquesJoueurs()

# Simuler un match de football
joueur5_om.marquerUnBut()
joueur5_om.effectuerUnePasseDecisive()
joueur5_om.recevoirUnCartonJaune()
joueur5_om.afficherStatistiques()

joueur2_om.recevoirUnCartonRouge()
joueur2_psg.effectuerUnePasseDecisive()
joueur1_psg.marquerUnBut()

joueur3_om.effectuerUnePasseDecisive()
joueur3_psg.recevoirUnCartonJaune()

# Print the updated statistics of all players in each team
equipe_om.afficherStatistiquesJoueurs()
equipe_psg.afficherStatistiquesJoueurs()