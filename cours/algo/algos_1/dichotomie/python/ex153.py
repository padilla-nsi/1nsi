def nb_de_tours(n):
    """
    Renvoie le plus petit entier k tel que 2**k > n
    (c'est-à-dire le nombre maximal de valeurs 
    examinées par la recherche dichotomique
    dans un tableau de taille n).
    """
    # BOUCLE: parcourir k de 0 à .. jusqu'à dépasser n
    # -> invariant: 2**k est inférieure ou égal à n
    k = 0

    # -> condition d'arrêt: 2**k dépasse n
    while not (2**k > n):
        # augmentation de k
        k = k + 1
    
    # fin BOUCLE: 2**k est le plus petit k
    # strictement supérieure à n

    return k


print(nb_de_tours(1_000_000))