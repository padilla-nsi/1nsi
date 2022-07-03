"""
    Text Steganography... Encode
"""

from PIL import Image



iron_patriot: Image = Image.open("iron_patriot.png")
iron_patriot_encoded = Image.new("L", iron_patriot.size)


text_to_encode = """Si vivre c'est lutter, à l'humaine énergie
Pourquoi n'ouvrir jamais qu'une arène rougie ?
Pour un prix moins sanglant que les morts que voilà
L'homme ne pourrait-il concourir et combattre ?
Manque-t-il d'ennemis qu'il serait beau d'abattre ?
Le malheureux ! il cherche, et la Misère est là !

Qu'il lui crie : « A nous deux ! » et que sa main virile
S'acharne sans merci contre ce flanc stérile
Qu'il s'agit avant tout d'atteindre et de percer.
A leur tour, le front haut, l'Ignorance et le Vice,
L'un sur l'autre appuyé, l'attendent dans la lice :
Qu'il y descende donc, et pour les terrasser.

A la lutte entraînez les nations entières.
Délivrance partout ! effaçant les frontières,
Unissez vos élans et tendez-vous la main.
Dans les rangs ennemis et vers un but unique,
Pour faire avec succès sa trouée héroïque,
Certes ce n'est pas trop de tout l'effort humain.

L'heure semblait propice, et le penseur candide
Croyait, dans le lointain d'une aurore splendide,
Voir de la Paix déjà poindre le front tremblant.
On respirait. Soudain, la trompette à la bouche,
Guerre, tu reparais, plus âpre, plus farouche,
Écrasant le progrès sous ton talon sanglant.

C'est à qui le premier, aveuglé de furie,
Se précipitera vers l'immense tuerie.
A mort ! point de quartier ! L'emporter ou périr!
Cet inconnu qui vient des champs ou de la forge
Est un frère ; il fallait l'embrasser, - on l'égorge.
Quoi ! lever pour frapper des bras faits pour s'ouvrir !

Les hameaux, les cités s'écroulent dans les flammes.
Les pierres ont souffert ; mais que dire des âmes ?
Près des pères les fils gisent inanimés.
Le Deuil sombre est assis devant les foyers vides,
Car ces monceaux de morts, inertes et livides,
Étaient des cœurs aimants et des êtres aimés.

Affaiblis et ployant sous la tâche infinie,
Recommence, Travail ! rallume-toi, Génie !
Le fruit de vos labeurs est broyé, dispersé.
Mais quoi ! tous ces trésors ne formaient qu'un domaine ;
C'était le bien commun de la famille humaine,
Se ruiner soi-même, ah ! c'est être insensé !

Guerre, au seul souvenir des maux que tu déchaînes,
Fermente au fond des cœurs le vieux levain des haines ;
Dans le limon laissé par tes flots ravageurs
Des germes sont semés de rancune et de rage,
Et le vaincu n'a plus, dévorant son outrage,
Qu'un désir, qu'un espoir : enfanter des vengeurs.

Ainsi le genre humain, à force de revanches,
Arbre découronné, verra mourir ses branches,
Adieu, printemps futurs ! Adieu, soleils nouveaux !
En ce tronc mutilé la sève est impossible.
Plus d'ombre, plus de fleurs ! et ta hache inflexible,
Pour mieux frapper les fruits, a tranché les rameaux."""

text_to_encode = "%"

text_to_encode += "\0"  # add a NULL character to stop decoding...

w,h = iron_patriot.size
print("length of text to hide", len(text_to_encode), "(max allowed:", w * h // 4 - 1, ")")

# text to bytes (encoded in utf-8)
bytes_to_encode = text_to_encode.encode("utf-8")

# encode the text in the 2 least significant cleared bits of the image
def i_to_image_coordinates(i, w, h):
    """translate an index to x,y of image"""
    return i%w, i//w

i_bytes = 0  # position in bytes_to_encode
i_pixel = 0  # position in image (as index)
i_bit = 0  # position in a byte

while(i_bytes < len(bytes_to_encode)):  # while there're bytes to hide
    # get a pixel
    p = iron_patriot.getpixel(i_to_image_coordinates(i_pixel, w, h))
    # get the current byte to hide
    byte = bytes_to_encode[i_bytes]
    # extract the 2 bits to be encoded and move them to the right
    bits = (byte & (2**i_bit + 2**(i_bit + 1))) >> i_bit

    if i_bytes == 0:
        print("explication")
        print(bin(p))
        print(bin(byte), bin(bits))

    # clear the 2 least significant bits of the image
    p = p & (255 - 3)  # 255-3 = 0b11111100
    # set the same bits with those from the text
    p = p | bits
    # save the pixel in the new image
    iron_patriot_encoded.putpixel(i_to_image_coordinates(i_pixel, w, h), p)
    # move to the next 2 bits
    i_bit += 2
    # move to the next pixel
    i_pixel += 1
    # is it time to change the byte ?
    if i_bit >= 8:
        # get next byte
        i_bytes += 1
        # go to the first bits
        i_bit = 0
    
    if i_bytes == 0:
        print(bin(p))

# copy the remaining pixels without modification
for i in range(i_pixel, w*h):
    p = iron_patriot.getpixel(i_to_image_coordinates(i, w, h))
    iron_patriot_encoded.putpixel(i_to_image_coordinates(i, w, h), p)
        
# iron_patriot_encoded.show()
iron_patriot_encoded.save("iron_patriot_stegano.png")
