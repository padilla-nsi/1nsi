def act1():
    score = int(input("Entrer le score : "))
    gain  = int(input("Entrer le gain : "))
    nouveau_score = score + gain
    if nouveau_score == 51:
        print("Victoire")
    elif nouveau_score < 51:
        print("Nouveau score :", nouveau_score)
    else:
        print("Nouveau score : 25")


def act2():
    n = int(input("Entrer un nombre entier positif : "))
    for i in range(1, n+1):
        if n % i == 0:
            print(i)


def act2_bis():
    n = int(input("Entrer un nombre entier positif : "))
    if n < 0:
        print(n, "n'est pas positif")
    else:
        print(1)
        for i in range(2, n//2 + 1):
            if n % i == 0:
                print(i)
        print(n)


def act3():
    n = int(input("Entrer un nombre entier positif : "))
    if n < 0:
        print(n, "n'est pas positif")
    else:
        nb_diviseurs = 2
        print(1)
        for i in range(2, n//2 + 1):
            if n % i == 0:
                nb_diviseurs = nb_diviseurs + 1
                print(i)
        print(n)
        if nb_diviseurs == 2:
            print(n, "est premier")
        else:
            print(n, "n'est pas premier")

def act4():
    score_1 = int(input("Score première boule : "))
    score_2 = int(input("Score deuxième boule : "))
    if score_1 == 10:
        print("X")
    elif score_1 + score_2 == 10:
        print("/")
    else:
        print(score_1 + score_2)


def act5():
    score_1 = int(input("Score première boule : "))
    if score_1 == 10:
        print("X")
    else:
        score_2 = int(input("Score deuxième boule : "))
        if score_1 + score_2 == 10:
            print("/")
        else:
            print(score_1 + score_2)

def act6():
    score_1 = int(input("Score première boule : "))
    if score_1 < 0 or score_1 > 10:
        print("!")
    elif score_1 == 10:
        print("X")
    else:
        score_2 = int(input("Score deuxième boule : "))
        if score_2 < 0 or score_1 + score_2 > 10:
            print("!")
        elif score_1 + score_2 == 10:
            print("/")
        else:
            print(score_1 + score_2)

def act7():
    a = int(input("Entrer la première distance : "))
    b = int(input("Entrer la deuxième distance : "))
    c = int(input("Entrer la troisième distance : "))
    if a+b >= c and b+c >= a and c+a >= b:
        print("Ceci est un triangle")
        if a == b and b == c:
            print("équilatéral")
        elif a == b or b == c or c == a:
            print("isocèle")
        else:
            print("scalène")
        
        if a*a+b*b == c*c or b*b+c*c == a*a or c*c+a*a == b*b:
            print("rectangle")
        
    else:
        print("Ceci n'est pas un triangle")


def act8():
    l1 = input("Première lettre : ")
    l2 = input("Deuxième lettre : ")
    if l1 == l2:
        print(l1)
    else:
        print("X")


# def act8()
    l1 = input("Première lettre : ")
    l2 = input("Deuxième lettre : ")
    l3 = input("Troisième lettre : ")

    if l1 == l2 or l1 == l3:
        print(l1)
    else:
        print(l3)

n = 0
k = int(input("Entrer l'ordre du code : "))
for _ in range(k):
    l = input("Saisir le lettre : ")
    if l == "1":
        n = n + 1
if n > k - n:
    print("1")
elif n < k - n:
    print("0")
else:
    print("X")
