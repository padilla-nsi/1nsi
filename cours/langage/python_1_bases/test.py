def recherche(tab, n):
    assert tab != []

    longueur = len(tab)
    i_max = longueur

    for i in range(longueur):
        if tab[i] == n:
            i_max = i

    return i_max


assert recherche([5, 3], 1) == 2
assert recherche([2, 4], 2) == 0
assert recherche([2,3,5,2,4],2) == 3