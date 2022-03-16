""" 
auteur : Pascal Padilla
"""


def recherche_dichotomique(elem, tab: list) -> int:
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
        
        print (g, d)
    
    return -1

print(recherche_dichotomique(12, list(range(10))))