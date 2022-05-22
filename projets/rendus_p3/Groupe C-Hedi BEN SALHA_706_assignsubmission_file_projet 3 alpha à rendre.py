def creation_bateaux(grille_5x5_j1, lettres_colonnes):
    """
    ajoute des bateaux dans la grille tab
    en utilisant pour nom de colonne le dictionnaire colonnes
    """
    for i in range(5):
        lettre_col = input("lettre pour la colonne [a..e](PAS DE MAJUSCULES ATTENTION): ")
        colonne = lettres_colonnes[lettre_col]
        ligne = int(input("numéro de la ligne [1..5]: "))
        ligne -= 1
        if grille_5x5_j1[ligne][colonne] == 0:
            grille_5x5_j1[ligne][colonne] = 1
        tableau_j1 = grille_5x5_j1
    print(tableau_j1)
    for i in range(5):
        lettre_col = input("lettre pour la colonne [a..e](PAS DE MAJUSCULES ATTENTION): ")
        colonne = lettres_colonnes[lettre_col]
        ligne = int(input("numéro de la ligne [1..5]: "))
        ligne -= 1
        if grille_5x5_j2[ligne][colonne] == 0:
            grille_5x5_j2[ligne][colonne] = 1
        tableau_j2= grille_5x5_j2
    print(tableau_j2)
def affichage(tab):
    """ affiche le tableau tab ligne par ligne """
    for i in range(len(tab)):
        print(tab[i])

def tester_tir(j1):
    """ Demande à l'utilisateur une ligne (a..e) et 
    une colonne (1..5) et affiche "raté" "touché"
    """

    if j1 ==0:
        j1 = input("lettre pour la colonne [a..e](PAS DE MAJUSCULES ATTENTION): ")
        j1_ligne = int(input("numéro de la ligne [1..5]: "))
        j1_ligne -= 1
        if j1 == colonnes:
          if tableau_j1[j1][j1_ligne] == 1:
              print('toucher')
              tableau_j1[j1][j1_ligne] = 'X'
          else:
            print('rater')
    else:
        j2 = input("lettre pour la colonne [a..e](PAS DE MAJUSCULES ATTENTION): ")
        j2_ligne = int(input("numéro de la ligne [1..5]: "))
        j2_ligne -=1
        if j1 == colonnes:
          if tableau_j2[j2][j2_ligne] == 1:
              print('toucher')
              tableau_j2[j2][j2_ligne] = 'X'
          else:
            print('rater')
j1 = 0
j1_ligne=0
j2 = 0
j2_ligne=0
colonnes = {"a":0, "b":1, "c":2, "d":3, "e":4}
grille_5x5_j1 =  [[0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0]]
grille_5x5_j2 =  [[0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0]]
bateau_max_j1 = 5
bateau_max_j2 = 5
tableau_j1 = grille_5x5_j1
tableau_j2 = grille_5x5_j2
# saisie = input()
# int_col = colonne[saisie]


def enregistrer_cible():
    pass

def mise_a_jour_score():
    pass



creation_bateaux(grille_5x5_j1, colonnes)
if j1 ==0:
    affichage(tableau_j1)
    tester_tir(j1)
    j1 = 0
    j1_ligne = 0
    score_j1 = 0
    score_j2 = 0
    
else:
    affichage(tableau_j2)
    tester_tir(j2)
    j2 = 0
    j2_ligne = 0
    
def conditons_victoire():
  """ Affiche à la fin le gagant de la partie """
  for i in range(len(grille_5x5_j1)):
    if grille_5x5_j1[ligne][colonne] == X:
      bateau_max_j1 = bateau_max_j1 - 1
    elif grille_5x5_j2[ligne][colonne] == X:
      bateau_max_j2 = bateau_max_j2 - 1
  if bateau_max_j1 == 0:
    print('Victoire joueur 1')
    score_j1 += 1
  elif bateau_max_j2 == 0:
    print('Victoire joueur 2')
    score_j2 += 1
  else: 
    pass
    
    
      

