import csv

# fichier formaté correct

fichier_circo = open("election2022_circo.csv")
table_circo = list(csv.DictReader(fichier_circo))
for l in table_circo[0:5]:
    print(l)
fichier_circo.close()

def valide(data):
    id_dpt = data['Code du département']
    dpt = data['Libellé du département']
    id_circo = data['Code de la circonscription']
    circo = data['Libellé de la circonscription']
    etat = data['Etat saisie']
    inscrits = data['Inscrits']
    abstentions = data['Abstentions']
    votants = data['Votants']
    blancs = data['Blancs']
    nuls = data['Nuls']
    exprimes = data['Exprimés']

    return {'id_dpt': id_circo, 'dpt': dpt, 'id_circo': id_circo, 
            'circo': circo, 'etat': etat, 'inscrits': inscrits, 
            'abstentions': abstentions, 'votants': votants, 'blancs': blancs, 'nuls': nuls, 'exprimes': exprimes}

table_validee = [valide(l) for l in table_circo[0:5]]

for l in table_validee:
    print(l)

# fichier avec erreurs de format

# fichier_dpt = open("election2022_dpt_erreurs.csv", encoding="ISO-8859-1")
# table_dpt = list(csv.DictReader(fichier_dpt, delimiter=";"))
# for l in table_dpt[0:3]:
#     print(l)
# fichier_dpt.close()