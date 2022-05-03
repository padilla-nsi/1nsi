tab = [1] * 2


def dichotomie(tab, elem):
    """
    Modification de la fontion dichotomie
    pour afficher, en plus de l'indice, le nombre
    de tours de boucles nécessaires
    """
    # BOUCLE: 
    # -> invariant 0: elem n'a pas été trouvé
    # -> invariant 1: si elem existe, il est dans la
    #               portion tab[g .. d]
    g = 0
    d = len(tab) - 1

    # -> invariant 2: cpt est le nombre de tours de boucles
    cpt = 0

    # -> condition d'arrêt: la zone de recherche est vide
    while not (g > d):
        # maintient invariant 2
        # nouveau tour de boucle
        cpt += 1

        # indice médian (arrondis inférieur)
        med = (g + d) //2

        # elem a été trouvé
        if tab[med] == elem:
            # renvoie anticipé correct
            return (med, cpt)

        # elem est dans la zone supérieure        
        elif elem > tab[med]:
            # mise à jour invariant 1
            # élimination de la zone inférieure
            g = med + 1
        
        # elem est dans la zone inférieure
        else:
            # mise à jour invariant 1
            # élimination de la zone supérieure
            d = med - 1
    
    # fin BOUCLE: la zone de recherche est vide et elem non trouvé
    # => renvoie -1 et du compteur
    return (-1, cpt)

print(dichotomie(tab, 0))

tab = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
print(dichotomie(tab, 40))
print(dichotomie(tab, 20))
print(dichotomie(tab, 15))
print(dichotomie(tab, 100))
