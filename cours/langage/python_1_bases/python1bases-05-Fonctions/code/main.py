from doctest import testmod

# 2.7 - Pythagore

def test_pythagore(a, b, c):
    """
    Est ce que le triangle dont les côtés mesurent
    a, b et c est rectangle ?

    Args:
        a (int): mesure côté 1
        b (int): mesure côté 2
        c (int): mesure côté 3

    Returns:
        bool: True ssi le triangle est rectangle
    
    Exemples:
    >>> print(test_pythagore(3, 4, 5))
    True
    >>> print(test_pythagore(7, 2, 12))
    False
    >>> print(test_pythagore(3, 5, 4))
    True
    >>> print(test_pythagore(5, 4, 3))
    True
    """
    est_rectangle = a*a + b*b == c*c \
                    or b*b + c*c == a*a \
                    or c*c + a*a == b*b
    return est_rectangle


# 2.7 - valeur absolue

def valeur_absolue(n):
    """
    Valeur absolue du nombre entier n

    Args:
        n (int): entier dont on veut la valeur absolue

    Returns:
        int: valeur absolue de n

    Exemples et tests:
    >>> print(valeur_absolue(5))
    5
    >>> print(valeur_absolue(-5))
    5
    >>> print(valeur_absolue(0))
    0
    >>> print(valeur_absolue(-42))
    42
    """
    if n >= 0:
        return n
    else:
        return -n


# 2.7 - multiples

def multiples_3_ou_5(borne_sup):
    """
    Renvoie la somme des multiples de 3 ou 5
    compris entre 1 et borne_sup (inclue)

    Args:
        borne_sup (int): limite supérieure

    Returns:
        int: somme des multiples
    
    Exemples et tests:
    >>> print(multiples_3_ou_5(2))
    0
    >>> print(multiples_3_ou_5(6))
    14
    >>> print(multiples_3_ou_5(10))
    33
    >>> print(multiples_3_ou_5(100))
    2418
    """
    somme = 0
    for i in range(borne_sup+1):
        if i % 3 == 0 or i % 5 == 0:
            somme += i
    return somme


if __name__ == '__main__':
    testmod()