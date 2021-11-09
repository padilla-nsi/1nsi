def act1():
    n = 3
    produit = 1
    for _ in range(n):
        produit = produit * 2
    print(produit)

def act2():
    cumul = 1
    for i in range(100):
        cumul = cumul * (i+1)
    print(cumul)


def act3():
    n = int(input("entrer un nombre"))

    # Question 1
    r = 0
    for i in range(n):
        r = r + i + 1
    print(r)

    # Question 2
    print(n*(n+1)//2)


def act6():
    n = int(input())
    r = 0
    for i in range(n):
        chiffre = int(input())
        r = chiffre * 10**i + r

    print(r)


def act7():
    n = int(input("Entrer un nombre entier : "))
    k = int(input("Entrer un nombre de chiffres : "))

    for _ in range(k):
        print(n % 10)
        n = n // 10

n = int(input("Entrer un nombre entier : "))

fib_m = 0   # valeur en n-1
fib_n = 1   # valeur en n

for _ in range(2, n+1):
    tmp = fib_m
    fib_m = fib_n
    fib_n = fib_m + tmp

print(fib_n)