import wave
from PIL import Image

# open wave file
wave_file = wave.open("heroes_stegano.wav", 'rb')

# read image width
w = 0
i_bit = 0

while i_bit < 16:
    s = wave_file.readframes(1)
    s = int.from_bytes(s, byteorder='little')
    s &= 0b11
    w |= s << i_bit
    i_bit += 2
    
# read image height
h = 0
i_bit = 0

while i_bit < 16:
    s = wave_file.readframes(1)
    s = int.from_bytes(s, byteorder='little')
    s &= 0b11
    h |= s << i_bit
    i_bit += 2

print("image is a ", w, "x", h)

# create image of the right size
im = Image.new("L", (w,h))

def i_to_image_coordinates(i, w, h):
    """translate an index to x,y of image"""
    return i%w, i//w

# get image data and normalize to 8bits
for i in range(w*h):
    f = wave_file.readframes(1)
    f = int.from_bytes(f, byteorder='little')
    f &= 0b11
    p = int(f * 255 / 3)
    im.putpixel(i_to_image_coordinates(i, w, h), p)

# show result
im.show()