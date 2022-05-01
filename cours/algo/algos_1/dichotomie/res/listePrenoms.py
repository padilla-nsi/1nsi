import csv

fichier = open("listePrenoms.csv")
prenoms = list(csv.DictReader(fichier))
fichier.close()

# prenoms = []
# for eleve in prenoms_brut:
#     if eleve["Prénom"] not in prenoms:
#         prenoms.append(eleve["Prénom"])

prenoms_valides = []
for p in prenoms:
    if p not in prenoms_valides:
        prenoms_valides.append(p)


prenoms_valides.sort(key=lambda p: p["Prénom"])

fichier = open("listePrenomsTries.csv", 'w')
w = csv.DictWriter(fichier, ["Prénom"])
w.writeheader()
w.writerows(prenoms_valides)

fichier.close()

import random


def prenoms_to_list(prenoms: list) -> list:
    tab = []
    for eleve in prenoms:
        tab.append(eleve["Prénom"])
    return tab

def prenoms_to_dict(prenoms: list) -> list:
    tab = []
    for prenom in prenoms:
        tab.append({"Prénom": prenom})
    return tab

prenom_tab  = prenoms_to_list(prenoms_valides)
random.shuffle(prenom_tab)
prenoms_valides = prenoms_to_dict(prenom_tab)

fichier = open("listePrenomsShuffle.csv", 'w')
w = csv.DictWriter(fichier, ["Prénom"])
w.writeheader()
w.writerows(prenoms_valides)

fichier.close()
