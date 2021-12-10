"""
exercices/activités Python données durant ce chapitre
"""


from doctest import testmod


def conversion_binaire(nb_decimal: int) -> str:
    """
    convertit le nombre entier 'nb_decimal' en binaire
    renvoie une chaîne de caractère contenant
    l'écriture binaire du nombre

    Args:
        nb_decimal (int): nombre entier écrit en base 10

    Returns:
        str: écriture binaire du nb (en chaîne de caractères)

    Exemples et tests:
    >>> conversion_binaire(8) == '1000'
    True
    >>> conversion_binaire(8) == 1000
    False
    >>> conversion_binaire(15) == '1111'
    True
    """
    nb = nb_decimal

    binaire = ""

    for i in range(nb_decimal):
        reste = nb % 2
        quotient = nb // 2
        nb = quotient

        binaire = str(reste) + binaire

        if nb == 0:
            return binaire

    return 'erreur, ne dois jamais arriver...'




if __name__ == '__main__':
    testmod()
