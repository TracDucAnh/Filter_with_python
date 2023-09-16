import math
from PIL import Image

file_name = input("Input file name.format(must be bmp): ")
try:
    file = Image.open(file_name)
    height = file.size[0]
    width = file.size[1]
    origin_pixel = file.load()
    image = Image.new('RGB', (height,width))
    pixel = image.load()
    for i in range(0,height):
        for j in range(0,width):
            pixel[i,j] = origin_pixel[i, width - j - 1];
    image.save("Flip_vertically.bmp")
    print("Successfully flipped image.")
except:
    print("File does not exist")