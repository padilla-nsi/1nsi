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
        
    return -n


# 2.7 - multiples

# def somme_multiples_lent(n, sup):
#     somme = 0
#     for i in range(1, sup+1):
#         if i % n == 0:
#             somme = somme + i
#     print(somme)

# def somme_multiples_rapide(n, sup):
#     somme = n*(sup//n * (1+sup//n) )//2
#     print(somme)

# somme_multiples_rapide(17, 20_000_000)
# somme_multiples_lent(17, 20_000_000)


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
            print(i)
            somme += i
    return somme


multiples_3_ou_5(10)



# 2.7 - max2
def max2(a, b):
    """
    Renvoie le plus grand des nombres a ou b

    Args:
        a (int): premier entier à comparer
        b (int): deuxième entier à comparer

    Returns:
        int: le max des deux
    
    Exemples et tests:
    >>> print(max(0, 0))
    0
    >>> print(max(1, 2))
    2
    >>> print(max(-2, -1))
    -1
    """
    if a >= b:
        return a
    
    return b

# 2.7 - max3
def max3(a, b, c):
    """
    Renvoie le plus grand de trois nombres entiers

    Args:
        a (int): premier nombre
        b (int): deuxième nombre
        c (int): troisième nombre

    Returns:
        int: max des trois nombres
    
    Exemples et tests:
    >>> max3(0, 0, 0)
    0
    >>> print(max3(0,5,2))
    5
    >>> print(max3(-10,5,21))
    21
    """
    return max2(a, max2(b, c))


# 2.7 - puissance
def puissance(x, k):
    """
    Renvoie x à la puissance k
    (équivalent à x**k)

    Args:
        x (int): base de la puissance
        k (int): exposant

    Returns:
        int: x puissance k
    
    Exemples et tests:
    >>> print(puissance(5, 2))
    25
    >>> print(puissance(100, 0))
    1
    >>> print(puissance(2, 10))
    1024
    """
    resultat = 1
    for i in range(k):
        resultat = resultat * x
    
    return resultat


# 2.7 - bissextile
def est_bissextile(annee):
    """
    Est ce que l'année annee est bissextile ?

    Args:
        annee (int): année à tester

    Returns:
        bool: True si et seulement si annee
              est une année bissextile
    
    Exemples et tests:
    >>> print(est_bissextile(1996))
    True
    >>> print(est_bissextile(2024))
    True
    >>> print(est_bissextile(2022))
    False
    """
    est_div_4   = annee % 4   == 0
    est_div_100 = annee % 100 == 0
    est_div_400 = annee % 400 == 0
    if (est_div_4 and not est_div_100) \
        or est_div_400:
        return True
    
    return False



# 2.7 - nb jours d'une année
def nb_jours_annee(annee):
    """
    renvoie le nombre de jours de l'année annee

    Args:
        annee (int): année à étudier

    Returns:
        int: 365 ou 366 (ça dépend)
    
    Exemples et tests:
    >>> print(nb_jours_annee(1996))
    366
    >>> print(nb_jours_annee(2024))
    366
    >>> print(nb_jours_annee(2022))
    365
    """
    if est_bissextile(annee):
        return 366
    return 365


# 2.7 - nb jours par mois
def nb_jours_mois(annee, mois):
    """
    Renvoie le nombre de jour du mois `mois` de l'année `annee`

    Args:
        annee (int): année à étudier
        mois (int): mois de l'année (1..12)

    Returns:
        int: 28, 29, 30 ou 31 jours en fonction du mois et de l'année
    
    Exemples et tests:
    >>> print(nb_jours_mois(1900, 1))
    31
    >>> print(nb_jours_mois(1900, 2))
    28
    >>> print(nb_jours_mois(1904, 2))
    29
    >>> print(nb_jours_mois(2021, 9))
    30
    """
    if mois == 2:
        if est_bissextile(annee):
            return 29
        else:
            return 28
    
    if mois == 4 or mois == 6 or mois == 9 or mois == 11:
        return 30
    
    return 31


# 2.7 - nb de jours entre deux dates
def nb_jours(j_debut, m_debut, a_debut, j_fin, m_fin, a_fin):
    """
    Nombre de jours entre deux dates données
    (jours de début et de fin compris).

    Args:
        j_depart (int): jour du mois de départ (1..31)
        m_depart (int): mois de départ (1..12)
        a_depart (int): année de départ
        j_fin (int): jour du mois de fin (1..31)
        m_fin (int): mois de fin (1..12)
        a_fin (int): année de fin

    Returns:
        int: durée entre les deux dates (en jours)
    
    
    Exemples et tests:
    >>> print(nb_jours(1,1,2021,15,1,2021))
    15
    >>> print(nb_jours(1,1,2021,31,12,2021))
    365
    >>> print(nb_jours(1,1,2024,31,12,2024))
    366
    >>> print(nb_jours(1,1,1970,31,12,2021))
    18993
    """
    # nombre de jours avant la date de
    # départ pour compléter la première année
    nbjours_avant = 0
    nbjours_avant = nbjours_avant + j_debut - 1
    for m in range (1, m_debut):
        nbjours_avant = nbjours_avant + nb_jours_mois(a_debut, m)

    # nombre de jours après la date de
    # fin nécessaires pour compléter la dernière année
    nbjours_apres = 0
    nbjours_apres = nbjours_apres + nb_jours_mois(a_fin, m_fin) - j_fin
    for m in range(m_fin + 1, 13):
        nbjours_apres = nbjours_apres + nb_jours_mois(a_fin, m)

    # nombres de jours entre l'année de début et l'année de fin
    total = 0
    for a in range(a_debut, a_fin+1):
        total = total + nb_jours_annee(a)

    # retirer les jours en trop des
    # premières et dernières années
    return total - nbjours_avant - nbjours_apres




if __name__ == '__main__':
    testmod()