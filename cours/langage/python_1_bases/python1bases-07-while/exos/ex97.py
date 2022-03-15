"""
auteur : Pascal Padilla
source : NSI, Balabonski et al., exercice 97 p 97
"""


from doctest import testmod


def sous_mot(tab1: list, tab2: list) -> bool:
    """
    Renvoie vrai si et seulement les éléments de tab1
    apparaissent dans l'ordre dans tab2.

    Args:
        tab1 (list): tableau source
        tab2 (list): tableau à comparer

    Returns:
        bool

    Tests et exemples:
    >>> sous_mot([2, 4, 6], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    True
    >>> sous_mot([2, 6, 4], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    False
    >>> sous_mot([], [])
    True
    >>> sous_mot([1, 2, 1], [1, 2, 1])
    True
    """
    n_1 = len(tab1)
    n_2 = len(tab2)

    # conditions d'arrêts :
    #  * i == n1 : tout tab1 a été parcouru et donc
    #    tous les éléments de tab1 sont dans tab2
    #  * j == n2 : tout tab2 a été parcouru et donc il reste
    #    des éléments de tab1 qui ne sont pas dans tab2
    # boucle :
    #  * tester si tab1[i] == tab2[j] (et si oui incrémenter i)
    #  * incrémenter j pour passer à la case suivante de tab2
    # conditions initiales :
    #  * i ← 0 : positionner i au début de tab1
    #  * j ← 0 : positionner j au début de tab2
    i = 0
    j = 0
    while not (i == n_1 or j == n_2):
        if tab1[i] == tab2[j]:
            i = i + 1

        j = j + 1

    # tab1 entièrement parcouru
    if i == n_1:
        return True

    # tab2 entièrement parcouru
    return False


# Tests et exemples
testmod()
