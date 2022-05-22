from __future__ import annotations
from typing import List


class Cellule():
    """
    Cellule du Jeu de la Vie.
    """
    def __init__(self: Cellule) -> None:
        """
        Initialisation des attributs.
        """
        self.actuel = False
        self.futur = False
        self.voisins = None

    def est_vivant(self: Cellule) -> bool:
        """
        Retourne l'état actuel de la cellule.
        """
        return self.actuel

    def set_voisins(self: Cellule, voisins: List[Cellule]) -> None:
        """
        Affecte comme voisins la liste passée en paramètre.
        """
        self.voisins = voisins

    def get_voisins(self: Cellule) -> List[Cellule]:
        """
        Renvoie la liste des voisins de la cellule
        """
        return self.voisins

    def naitre(self: Cellule) -> None:
        """
        Met l’état futur de la cellule à `True`
        """
        self.futur = True

    def mourir(self: Cellule) -> None:
        """
        Met l’état futur de la cellule à `False`
        """
        self.futur = False

    def basculer(self: Cellule) -> None:
        """
        Fait passer l’état futur de la cellule dans l’état actuel
        """
        self.actuel = self.futur

    def __str__(self: Cellule) -> str:
        """
        Représentation de l'objet sous forme d'une chaîne de caractères
        """
        if self.actuel:
            chaine = "X"
        else:
            chaine = "-"
        return chaine

    def calcule_etat_futur(self: Cellule) -> None:
        """
        Implémente les règles d’évolution du jeu de la vie en préparant l’état futur à sa nouvelle valeur
        """
        nbre_voisins_vivants = 0

        for voisin in self.voisins:
            if voisin.est_vivant():
                nbre_voisins_vivants += 1

        if (nbre_voisins_vivants != 2) and (nbre_voisins_vivants != 3) and (self.est_vivant()):
            self.mourir()
        elif (nbre_voisins_vivants == 3) and not (self.est_vivant()):
            self.naitre()
        else:
            self.futur = self.actuel