import wave
from PIL import Image

# open the wave file (mono, 8bits per sample, 48000Hz)
wave_file = wave.open("heroes.wav", 'rb')

# creat output file and set identical header
wave_file_out = wave.open("heroes_stegano.wav", "wb")
wave_file_out.setnchannels(wave_file.getnchannels())
wave_file_out.setsampwidth(wave_file.getsampwidth())
wave_file_out.setframerate(wave_file.getframerate())

# open image and get size
image = Image.open("bowie.png")
w,h = image.size

def i_to_image_coordinates(i, w, h):
    """translate an index to x,y of image"""
    return i%w, i//w

# we must encode the size of the image to get things back

# encode width as 2bytes int
bin_w = w.to_bytes(2, byteorder='little')
i_bit_bin_w = 0
i_byte_bin_w = 0

while i_byte_bin_w < 2:
    s = wave_file.readframes(1)
    s = int.from_bytes(s, byteorder='little')
    s &= 0b11111100
    s |= (bin_w[i_byte_bin_w] & (2**i_bit_bin_w + 2**(i_bit_bin_w + 1))) >> i_bit_bin_w
    wave_file_out.writeframesraw(s.to_bytes(1, byteorder='little'))
    i_bit_bin_w += 2
    if i_bit_bin_w > 6:
        i_byte_bin_w += 1
        i_bit_bin_w = 0


# encode height as 2bytes int
bin_h = h.to_bytes(2, byteorder='little')
i_bit_bin_h = 0
i_byte_bin_h = 0

while i_byte_bin_h < 2:
    s = wave_file.readframes(1)
    s = int.from_bytes(s, byteorder='little')
    s &= 0b11111100
    s |= (bin_h[i_byte_bin_h] & (2**i_bit_bin_h + 2**(i_bit_bin_h + 1))) >> i_bit_bin_h
    wave_file_out.writeframesraw(s.to_bytes(1, byteorder='little'))
    i_bit_bin_h += 2
    if i_bit_bin_h > 6:
        i_byte_bin_h += 1
        i_bit_bin_h = 0

# copy image data (coded on 2bits) on the 2 least significant bits of each sample
for i in range(w*h):
    f = wave_file.readframes(1)
    p = image.getpixel(i_to_image_coordinates(i, w, h))
    f = int.from_bytes(f, byteorder='little')
    f &= 0b11111100
    p = int(p * 3 / 255)
    f |= p
    wave_file_out.writeframesraw(f.to_bytes(1, byteorder='little'))
    
# copy remaining data
for i in range(wave_file.tell(), wave_file.getnframes()):
    f = wave_file.readframes(1)
    wave_file_out.writeframesraw(f)
    
wave_file.close()
wave_file_out.close()