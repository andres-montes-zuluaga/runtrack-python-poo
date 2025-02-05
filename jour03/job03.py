class Tache:
    def __init__(self, titre, description, statut):
        self._titre = titre
        self._description = description
        self._statut = statut  # à faire ou terminée

class ListeDesTaches:
    def __init__(self, taches):
        self.__taches = taches
    
    def ajouterTache(self, tache):
        self.__taches.append(tache)
    
    def supprimerTache(self, tache):
        self.__taches.remove(tache)
    
    def marquerCommeFinie(self, tache):
        tache._statut = "terminée"
    
    def afficherListe(self):
        for tache in self.__taches:
            print(f"Titre: {tache._titre}")
            print(f"Description: {tache._description}")
            print(f"Statut: {tache._statut}")
            print()
    
    def filterListe(self, statut):
        for tache in self.__taches:
            if tache._statut == statut:
                print(f"Titre: {tache._titre}")
                print(f"Description: {tache._description}")
                print(f"Statut: {tache._statut}")
                print()

tache1 = Tache("Entraîner le modèle", "Entraîner le modèle de reconnaissance d'images", "à faire")
tache2 = Tache("Collecter des données", "Collecter des données pour le dataset d'entraînement", "à faire")
tache3 = Tache("Évaluer le modèle", "Évaluer la performance du modèle entraîné", "terminée")
tache4 = Tache("Optimiser les hyperparamètres", "Ajuster les hyperparamètres du modèle", "terminée")

liste = ListeDesTaches([tache1, tache2, tache3, tache4])
liste.afficherListe()

print("Filtrage des tâches à faire:")
liste.filterListe("à faire")

print("Filtrage des tâches terminées:")
liste.filterListe("terminée")

tache5 = Tache("Implémenter le modèle", "Implémenter le modèle dans le système de production", "à faire")
liste.ajouterTache(tache5)

print("Ajout d'une tâche:")
liste.afficherListe()