for i in range (9): 
    grille = [ ["-","-","-"], 
           ["-","-","-"], 
           ["-","-","-"] ]

    print("Joueur X dois jouer...")
    ligne = int(input("  numéro de ligne (0..2): ") )
    colonne =int( input("  numéro de colonne (0..2): "))
    grille [ligne] [colonne] = "X"
    for i in range(3):
        print( grille[i] )

    print("Joueur O dois jouer...")
    ligne = int(input("  numéro de ligne (0..2): ") )
    colonne =int( input("  numéro de colonne (0..2): "))
    grille [ligne] [colonne] = "O"
    for i in range(3):
        print( grille[i] )

