def permute(tab: list, i: int, j: int):
    """Échange les valeurs tab[i] et tab[j]

    Args:
        tab (list): tableau
        i (int): indice du premier élément
        j (int): indice du deuxième élément
    """
    temp = tab[i]
    tab[i] = tab[j]
    tab[j] = temp


def tri_selection(tab: list):
    """Tri un tableau par l'algorithme
    du tri par sélection

    Args:
        tab (list): tableau à trier
    """
    n = len(tab)

    # tous les éléments situés avant i sont :
    #   triés et
    #   inférieurs à tous ceux situés après i (inclus)
    for i in range(n):
        i_min = i

        # tab[i_min] est la valeur minimale de
        #    la portion tab[i..j-1] du tableau
        for j in range(i+1, n):
            if tab[j] < tab[i_min]:
                i_min = j
        
        permute(tab, i, i_min)


tab_1 = [50, 400, 3000, 200000, 100]
tri_selection(tab_1)
print(tab_1)