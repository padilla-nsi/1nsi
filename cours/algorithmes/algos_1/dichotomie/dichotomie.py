""" 
auteur : Pascal Padilla
"""


def recherche_dichotomique(elem, tab: list) -> int:
    """Recherche dichotomique dans un tableau trié

    Args:
        elem (type): élément à rechercher
        tab (list): tableau dans lequel on cherche

    Returns:
        int:  * si trouvé     : indice de l'élément
              * si non trouvé : None
    """
    g = 0
    d = len(tab) - 1

    while g <= d:

        # indice et élément médians
        i_median = (g + d) // 2
        elem_median = tab[i_median]

        # elem trouvé !
        if elem == elem_median:
            return i_median
        
        # elem non trouvé
        # on poursuit la recherche à gauche
        if elem < elem_median:
            d = i_median - 1
        
        # ou bien on poursuit la recherche à droite
        else:
            g = i_median + 1
    
    return None


def recherche_brute(elem, tab):
    for i in range(len(tab)):
        if tab[i] == elem:
            return i
    
    return None


# taille des tableaux (en million)
elements = [2, 4, 8, 16, 32, 64]

from time import time
for elem in elements:
    tab = [0] * (elem * 1_000_000)
    t0 = time()
    recherche_dichotomique(elem, tab)
    duree = time() - t0
    print(elem, "\t", round(duree, 6))


for elem in elements:
    tab = [0] * (elem * 1_000_000)
    t0 = time()
    recherche_brute(elem, tab)
    duree = time() - t0
    print(elem, "\t", round(duree, 1))
