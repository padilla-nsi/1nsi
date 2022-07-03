"""
    Text Steganography... Decode
"""

from PIL import Image

iron_patriot = Image.open("iron_patriot_stegano.png")
w,h = iron_patriot.size

text = b""

def i_to_image_coordinates(i, w, h):
    """translate an index to x,y of image"""
    return i%w, i//w

i_bits = 0
octet = 0

for i_pixel in range(w*h):
    # get the current pixel
    p = iron_patriot.getpixel(i_to_image_coordinates(i_pixel, w, h))
    # get the 2 least significant bits and move them on the right place
    bits = (p & 0b00000011) << i_bits
    # integrate them in the byte
    octet |= bits
    # move to the next bits to add
    i_bits += 2
    # is it time to change byte ?
    if i_bits > 6:
        # add the byte to the string
        text += octet.to_bytes(1, byteorder="little")
        # go to the first bit
        i_bits = 0
        # clear the byte
        octet = 0
    # have we found the NULL character (value of 0)
    if len(text) != 0 and text[-1] == 0:
        # stop decoding...
        break
    
# decode bytes as utf-8 string
text = text[:-1].decode("utf-8")

# tada !
print(text)
    