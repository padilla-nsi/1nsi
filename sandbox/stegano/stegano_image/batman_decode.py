from PIL import Image

batman = Image.open("batman_stegano.png")
out = Image.new("RGB", batman.size)

bits = 3

w,h = batman.size  # same for out

# get hidden image
for i in range(w):
    for j in range(h):
        r,g,b = batman.getpixel((i,j))
        r = r & (2**bits -1)
        g = g & (2**bits -1)
        b = b & (2**bits -1)
        out.putpixel((i,j), (r,g,b))


# normalize joker to 8bits
for i in range(w):
    for j in range(h):
        r,g,b = out.getpixel((i,j))
        r = int(r * 255 / (2**bits -1))
        g = int(g * 255 / (2**bits -1))
        b = int(b * 255 / (2**bits -1))
        out.putpixel((i,j), (r,g,b))

out.show()
out.save("decoded.png")