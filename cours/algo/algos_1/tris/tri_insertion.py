def tri_insertion(tab: list):
    n = len(tab)
    for i in range(n):
        j = i
        while not (j==0 or tab[j] >= tab[j-1]):
            tab[j], tab[j-1] = tab[j-1], tab[j]
            j = j - 1

tab_1 = [50, 400, 3000, 200000, 100]
tri_insertion(tab_1)
print(tab_1)