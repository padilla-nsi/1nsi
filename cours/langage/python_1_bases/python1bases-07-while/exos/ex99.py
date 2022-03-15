"""
auteur : Pascal Padilla
source : NSI, Balabonski et al., exercice 97 p 97
"""


from doctest import testmod


def longueur_plus_grande_seq(tab: list) -> int:
    """
    Renvoie la longueur de la plus grande séquence
    d'élément identiques consécutifs

    Args:
        tab (list): tableau à analyser

    Returns:
        int: longueur

    Tests et Exemples:
    >>> longueur_plus_grande_seq ([1, 2, 2, 4, 4, 4, 4, 3, 3, 3])
    4
    >>> longueur_plus_grande_seq ([1, 2, 2, 3, 3, 3])
    3
    >>> longueur_plus_grande_seq ([])
    0
    >>> longueur_plus_grande_seq ([5])
    1
    >>> longueur_plus_grande_seq ([1, 2, 3])
    1
    """
    n = len(tab)

    # cas du tableau vide
    if n == 0:
        return 0

    # le tableau a au moins 1 élément et
    # on commence le parcours à partir de la 2e case
    longueur_courante = 1
    longueur_max = 1
    for i in range (1, n):
        # augmentation de la longueur courante
        if tab[i] == tab[i-1]:
            longueur_courante = longueur_courante + 1
        # réinitialisation de la longueur courante
        else:
            longueur_courante = 1

        # mise à jour de la longueur maximale
        if longueur_courante > longueur_max:
            longueur_max = longueur_courante

    return longueur_max


testmod()

print([1, 2, 3][:3])
