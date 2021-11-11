a = int(input("Saisir la première valeur : "))
b = int(input("Saisir la deuxième nombre : "))

if a == 0 or (b != 0 and a % b == 0):
    print("divisible")
else:
    print("non divisible")