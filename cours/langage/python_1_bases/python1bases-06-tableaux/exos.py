from doctest import testmod



# Exo 1
pda = [691754, 714585, 723589, 741105, 761638, 782397, 806296, 813727, 830361, 836626,
       857412, 846079, 853732, 844444, 859144, 843717, 839171, 830450, 823756, 824021, 
       825068, 771160, 758647, 732962, 739197, 732521, 715066, 719576, 756910, 774944, 
       796258, 802788, 815670, 818399, 832977, 832461, 825974, 817778, 865383, 871959, 
       881060, 833394, 813784, 816353, 795349, 820771, 861730, 906113, 924323, 919896, 
       899550, 886276, 875462, 871272, 891426, 892392, 899362, 886362, 856619, 855441, 
       848042, 841009, 820136, 812492, 804014, 793523, 786152, 768512, 775095, 751752, 
       773191, 754577, 747317, 725950, 679274, 507127, 490957, 471618, 430510, 376688, 
       383970, 392579, 373969, 355308, 341153, 314805, 301041, 269011, 253855, 222346, 
       198098, 158712, 134827, 108837, 88250, 69403, 52436, 38806, 27854, 27497]


def somme_pda(age_min, age_max):
    """
    >>> somme_pda(0, 1)
    691754
    >>> somme_pda(1, 0)
    0
    >>> somme_pda(0, 100)
    67387330
    >>> somme_pda(50, 67)
    14519530
    """
    n = 0

    for age in range(age_min, age_max):
        n += pda[age]
    
    return n



# Exo 69
pda = [691754, 714585, 723589, 741105, 761638, 782397, 806296, 813727, 830361, 836626,
       857412, 846079, 853732, 844444, 859144, 843717, 839171, 830450, 823756, 824021, 
       825068, 771160, 758647, 732962, 739197, 732521, 715066, 719576, 756910, 774944, 
       796258, 802788, 815670, 818399, 832977, 832461, 825974, 817778, 865383, 871959, 
       881060, 833394, 813784, 816353, 795349, 820771, 861730, 906113, 924323, 919896, 
       899550, 886276, 875462, 871272, 891426, 892392, 899362, 886362, 856619, 855441, 
       848042, 841009, 820136, 812492, 804014, 793523, 786152, 768512, 775095, 751752, 
       773191, 754577, 747317, 725950, 679274, 507127, 490957, 471618, 430510, 376688, 
       383970, 392579, 373969, 355308, 341153, 314805, 301041, 269011, 253855, 222346, 
       198098, 158712, 134827, 108837, 88250, 69403, 52436, 38806, 27854, 27497]



def somme_pda(age_min, age_max):
    """
    >>> somme_pda(0, 1)
    691754
    >>> somme_pda(1, 0)
    0
    >>> somme_pda(0, 100)
    67387330
    >>> somme_pda(0, 101)
    67387330
    >>> somme_pda(0, 150)
    67387330
    >>> somme_pda(50, 67)
    14519530
    >>> somme_pda(50, 100)
    26884855
    >>> somme_pda(50, 242)
    26884855
    >>> somme_pda(50, 40)
    0
    """
    n = 0
    if age_max > len(pda):
        age_max = len(pda)

    for age in range(age_min, age_max):
        n += pda[age]
    
    return n



# Exo 70
def occurences(val, tab):
    """
    >>> occurences(0, [0, 1, 1, 3, 1])
    1
    >>> occurences(1, [0, 1, 1, 3, 1])
    3
    >>> occurences("a", ["abc", "a", "b", "c"])
    1
    """
    n = 0
    for i in range(0, len(tab)):
        if tab[i] == val:
            n = n + 1

    return n



# Exo 71
from random import *
def tab_alea():
    seed(42)
    tab = [0] * 100
    for i in range(100):
        tab[i] = randint(1, 1000)
    print(tab)

# tab_alea()



# Exo 72
def maxi_tab(t):
    """
    >>> maxi_tab([1, 2, 3])
    3
    >>> maxi_tab([10, 11, 3, 4])
    11
    """
    maxi = t[0]
    for i in range(1, len(t)):
        if t[i] > maxi:
            maxi = t[i]
    return maxi



# Exo 73
from random import *
def effectifs(generateur):
    seed(generateur)
    effectifs = [0] * 10
    for i in range(1000):
        n = randint(1, 10)
        effectifs[n - 1] += 1
    
    for i in range(len(effectifs)):
        print("le nombre", i+1, "a été tiré", effectifs[i], "fois")

gen = 42 #int(input("saisir une valeur pour le générateur aléatoire : "))
# effectifs(gen)



# exo 74
tab = [0] * 30
tab[0] = 0
tab[1] = 1

for i in range(2, 30):
    tab[i] = tab[i-2] + tab[i-1]

# print(tab)




# exo 75 (exo 8 de moodle)
# à faire sur codeboard... pour tester

def copie(tab):
    """
    >>> u = []          # u est un tableau vide
    >>> t = [1, 2, 3]
    >>> u = copie(t)
    >>> print(u)        # vérifier que u contient les mêmes valeurs que t
    [1, 2, 3]
    >>> t[2] = 7        # vérifier que lorsqu'on modifie t
    >>> print(t)        #   alors u n'est PAS modifié par effets de bords
    [1, 2, 7]
    >>> print(u)
    [1, 2, 3]
    """
    n = len(tab)
    tab_2 = [0] * n

    for i in range(n):
        tab_2[i] = tab[i]
    
    return tab_2


# exo 76
def ajout(val, tab):
    """
    >>> print( ajout(42, []) )
    [42]
    
    >>> print( ajout(10, [5, 4, 3, 2, 1]) )
    [5, 4, 3, 2, 1, 10]

    >>> u = []
    >>> t = [1, 2, 3]
    >>> u = ajout(4, t)
    >>> print(u)        # u est une copie de t avec 4 ajouté à la fin
    [1, 2, 3, 4]
    >>> print(t)        # t inchangé
    [1, 2, 3]
    """
    n = len(tab)
    tab_2 = [0] * (n + 1)
    for i in range(n):
        tab_2[i] = tab[i]
    tab_2[n] = val
    return tab_2



# exo 10 (77)
def concatenation(t1, t2):
    


testmod()
