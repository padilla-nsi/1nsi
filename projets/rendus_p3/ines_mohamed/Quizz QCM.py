from random import *


def melange(tab):
    """ mélange de façon aléatoire
    le tableau """
    sauv = tab[2]
    tab[2] = tab[1]
    tab[1] = sauv
    return tab

point=0
question = [ "q1:  Quelle partie de l'oeuf dois-je cuisiner pour préparer avec succès une mayonnaise ?", "q2: L'un des plus grands chefs-d'oeuvre de la littérature de la Grèce antique est...","q3 : En physique, quelle unité utilise-t-on pour mesurer la tension électrique ?", " En physique, quelle unité utilise-t-on pour mesurer la tension électrique ?", " q4 Lequel de ces quatres mots de la langue française est mal orthographié ?", "Les quatre pays qui ont disputé les demi-finales de la coupe du monde de football en 1998 sont la France, le Brésil, la Croatie et ...", " q5 Dans quelle partie du corps humain trouve-t-on le nerf dit pudendal ?", " q6 Dans lequel de ces départements français l'altitude minimale n'excède pas 200 mètres ?", "q7 Il faut entendre par le terme de climacophobie la peur incontrôlable ...","q8 Où la plupart des algues poussent-elles ?", "q9 L'interieur du kiwi est le plus souvent de couleur...", "q10 L'interieur du kiwi est le plus souvent de couleur...", "q11 Si vous voyagez en R.E.R, vous êtes en région...", "q12 Dans la mythologie grecque, Ulysse a su résister au charme envoûtant du chant des...", "q13 A l'état naturel, quelle est la couleur des cristaux de soufre ?", "q14 Les héros du film Avatar, ont la peau bleue et...", "q15 Qu'est-ce qui a lieu en 1er chaque année, au mois de Mars ?", "q16 De 2009 à 2018, le télescope spatial Kepler avait pour mission de recenser les...", "q17 En sport, la Vasaloppet est une célèbre course de...", "q18 La Loire est le plus long fleuve de France qui s'étire sur environ...", "q19 Quel président américain est apparu dans la série TV Laugh-In ?", "q20 Lequel de ces aliments peut être noir ou au lait ?", "q21 Dans Les Visiteurs, Christian Clavier dit souvent...", "q22 Un plateau de cinéma est éclairé par des...", "q23 Dans la série TV, quelle est la voiture de Columbo ?", "q24 Quelle proposition ne fait pas vraiment référence a un président de la République Française ?", "q25  En sport, le tacle est une technique propre au...", "q26 De quel métal la tour Eiffel est-elle essentiellement constituée ?", "q27  Sous quel nom le duo Simon & Garfunkel a-t-il débuté sa carrière musicale ?", "q28 Dans un sous-marin, lorsque la lumière rouge est allumée, cela indique...", "q29 Quelle bataille napoléonienne est la plus récente de ces 4 ?", "q30 Quelle bataille napoléonienne est la plus récente de ces 4 ?"]
 
prop= [" Le jaune ", " / Le violet  ", " / Le bleu ", " / Le rose ", " L'Odyssée (Homère) ", " / L'Expédition (Bart) ", " / La Thalassothérapie (Marge)", " / Le Road-Trip (Moe)", " Le volt ", " / Le hertz ", " / Le watt", " / Le décibel ", " / Intermittance ", " / Gaufre ", " / Inondation ", " / Trottinette ", "Les Pays-Bas", "/ Le Chili", " / L'Argentine", "/ L'Allemagne", "/ Dans le bassin", "/ Dans la cheville", "/ Dans la cuisse", "/ Dans l'épaule", " La Lozère (48)", "/ Les Alpes-de-Haute-Provence (04)", "/ La Savoie (73)", "/ Les Vosges (88)" "Des escaliers", "/ De la boue", "/ Des forêts", "/ De l'encre", "/ Dans l'eau", "/ En montagne", "/ Dans la jungle", "/ Sur les routes", "Vert ", "/ Marron", "/ Orange", "/ Blanc", " Parisienne", "/ Lyonnaise", "/ Toulousaine", "/ Stéphanoise", " Sirènes", "/ Six reines", "/ Six rennes", "/ Six rênes", " Jaune", "/ Rose", "/ Bleu", "/ Blanc", "Les oreilles pointues ", "/ Les yeux rouges", "/ Une longue barbe", "/ De petites cornes", " Fête des grands-mères", "/ Passage à l'heure d'été", "/ Journée de la femme", "/ Saint-Patrick", " Exoplanètes", "/ Trous noirs", "/ Lunes de Saturne", "/ Comètes", " Ski de fond", "/ Formule 1", "/ Natation", "/ Planche à voile", "1020 Km", "/ 920 Km", "/ 1120 Km", "/ 1220 Km", " Le chocolat", "/ L'oeuf", "/ Le sucre", "/ La farine", " Projecteurs", "/ Lampions", "/ Enseigne", "/ Lampadaires", " Une 403 ", "/ Une Ferrari", "/ Une Rolls Royce", "/ Une 2 CV", " Gilets jaunes de Macron ", "/ Charles de Gaulle de l'Etoile", "/ Bibliothèque Mittrand", "/ Centre Pompidou", " Football", "/ Tennis", "/ Ski de fond", "/ Squash", " De fer", "/ D'aluminium", "/ D'acier", "/ De plomb", " Tom & Jerry", " Heckle & Jeckle", "/ Chip & Dale", "/ Dr. Jekill & Mr. Hyde", " Les heures de nuits", "/ Qu'un ennemi approche", "/ Que le navire plonge", "/ Un tir de torpille", " A rayures rouges", "/ A carreaux rouges", "/ Avec une étoile bleue", "/ Avec un rond bleu", " Wagram", "/ Marengo", "/ Iéna", "/ Austerlitz"]

nbq= int(input("Choisir le nombre de question souhauté .../30:"))
d = 0
for i in range (nbq):

    print(question[i])
    i=+1
    print("     1                  2                    3                   4")
    tab_prop = prop[d:d+4]
    tab_melange = melange(tab_prop)
    print(tab_melange)

    rep = int(input ("Entrée le numéro correspondent à la de la bonne réponse :  " ))
    rpcorrecte = 1
    if rep != rpcorrecte:
        print("FAUX")
        point= point - 0.25
    else :
        print("BIEN")
        point= point + 1
    d = d+4
point = point*20/nbq
print(point,"/20")
print ("vous avez gagné 3 neurones!!!!")
