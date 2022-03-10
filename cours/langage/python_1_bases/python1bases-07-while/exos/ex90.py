"""
auteur : Pascal Padilla
source : NSI, Balabonski et al., exercice 90 p 97
"""


from doctest import testmod


def nb_chiffre(nombre: int) -> str:
    """ Renvoie le nombre de chiffre de n

    Exemples et tests:
    >>> nb_chiffre(8)
    1
    >>> nb_chiffre(314)
    3
    >>> nb_chiffre(123456789)
    9
    >>> nb_chiffre(0)
    1
    """
    total = 1
    quotient = nombre
    while not quotient < 10:
        total = total + 1
        quotient = quotient // 10
    return total


# Tests

testmod()
