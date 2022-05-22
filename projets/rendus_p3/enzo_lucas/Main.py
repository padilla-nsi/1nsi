from grille import Grille
import time

"""
fonctionnement du jeu, changer les valeurs entre parenthese de Frille() et remplir_alea()
pour personnaliser le jeu
"""
def main():
    vie = Grille(20, 30)
    vie.remplir_alea(55)
    vie.affecte_voisins()
    while True:
        print("\u001B[H\u001B[J")
        print(vie)
        print("\n")
        time.sleep(0.5)
        vie.jeu()
        vie.actualise()


main()  