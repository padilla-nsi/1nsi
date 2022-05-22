from __future__ import annotations
from cellule import Cellule
from typing import List
from random import random


class Grille():
    """
    Grille du Jeu de la Vie
    """
    def __init__(self: Grille, hauteur: int, largeur: int) -> None:
        """
        Initialisations des attributs
        """
        self.hauteur = hauteur
        self.largeur = largeur
        # Grille de cellules
        self.matrix = self.set_matrix()

    def set_matrix(self: Grille) -> List[Cellule]:
        """
        Construction de la grille de cellules
        """
        matrix = []
        for i in range(self.largeur):
            liste = []
            for j in range(self.hauteur):
                liste.append(Cellule())
            matrix.append(liste)
        return matrix

    def dans_grille(self: Grille, i: int, j: int) -> bool:
        """
        Vérifie que le point de coordonnées (i,j) est dans la grille
        """
        return 0 <= i < self.largeur and 0 <= j < self.hauteur

    def setXY(self: Grille, i: int, j: int, cellule: Cellule) -> None:
        """
        Affecte une nouvelle cellule à la case (i,j) de la grille
        """
        if self.dans_grille(i, j):
            self.matrix[i][j] = cellule
        else:
            raise IndexError(str(i, j))

    def getXY(self: Grille, i: int, j: int) -> Cellule:
        """
        Récupère la cellule située dans la case (i,j) de la grille
        """
        if self.dans_grille(i, j):
            return self.matrix[i][j]
        else:
            raise IndexError(str(i, j))

    def get_largeur(self: Grille) -> int:
        """
        Récupère la largeur de la grille
        """
        return self.largeur

    def get_hauteur(self: Grille) -> int:
        """
        Récupère la hauteur de la grille
        """
        return self.hauteur

    @staticmethod
    def est_voisin(i: int, j: int, x: int, y: int) -> bool:
        """
        Vérifie si les cases (i,j) et (x,y) sont voisines dans la grille
        """
        return (abs(x - i) == 1) or (abs(y - j) == 1)

    def get_voisins(self: Grille, x: int, y: int) -> List[Cellule]:
        """
        Renvoie la liste des voisins d’une cellule
        """
        voisins = []
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if self.dans_grille(i, j) and Grille.est_voisin(x, y, i, j):
                    voisins.append(self.getXY(i, j))
        return voisins

    def affecte_voisins(self: Grille):
        """
        Affecte à chaque cellule de la grille la liste de ses voisins
        """
        for i in range(self.largeur):
            for j in range(self.hauteur):
                cellule = self.getXY(i, j)
                cellule.set_voisins(self.get_voisins(i, j))

    def __str__(self: Grille) -> str:
        """
        Représentation de l'objet
        """
        chaine = ""
        for i in range(self.largeur):
            for j in range(self.hauteur):
                chaine += str(self.getXY(i, j))
            chaine += "\n"
        return chaine

    def remplir_alea(self, taux: int) -> None:
        """
        Remplir aléatoirement la Grille avec un certain taux de Cellule vivantes
        """
        for i in range(self.largeur):
            for j in range(self.hauteur):
                if random() <= (taux / 100):
                    cellule = self.getXY(i, j)
                    cellule.naitre()
                    cellule.basculer()
                    print(cellule)

    def jeu(self: Grille) -> None:
        """
        Passe en revue toutes les Cellules de la Grille, calcule leur état futur
        """
        for i in range(self.largeur):
            for j in range(self.hauteur):
                cellule = self.getXY(i, j)
                cellule.calcule_etat_futur()

    def actualise(self: Grille) -> None:
        """
        Bascule toutes les cellules de la Grille dans leur état futur
        """
        for i in range(self.largeur):
            for j in range(self.hauteur):
                cellule = self.getXY(i, j)
                cellule.basculer()


if __name__ == "__main__":
    grille = Grille(4, 5)
    print(grille)