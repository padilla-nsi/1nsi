from PIL import Image

batman = Image.open("batman.png")
joker = Image.open("joker.png")

bits = 3

w,h = batman.size  # same for joker

# normalize joker to bits
for i in range(w):
    for j in range(h):
        r_0, g_0, b_0 = joker.getpixel((i,j))
        r = int(r_0 * (2**bits -1) / 255)
        g = int(g_0 * (2**bits -1) / 255)
        b = int(b_0 * (2**bits -1) / 255)
        joker.putpixel((i,j), (r,g,b))
        print(bin(r_0)[2:], bin(r)[2:])

# add joker to batman image
# 1. clear the least significant bits
# 2. copy the bits from the joker
for i in range(w):
    for j in range(h):
        r,g,b = batman.getpixel((i,j))
        rj,gj,bj = joker.getpixel((i,j))
        r = r & (255 - (2**bits -1))
        r = r | rj
        g = g & (255 - (2**bits -1))
        g = g | gj
        b = b & (255 - (2**bits -1))
        b = b | bj
        batman.putpixel((i,j), (r,g,b))
        
batman.show()
batman.save("batman_stegano.png")

