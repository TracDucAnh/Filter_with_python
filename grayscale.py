import math
from PIL import Image
file_name = input("Input file name.format(must be bmp): ")
try:
    file = Image.open(file_name)
    height = file.size[0]
    width = file.size[1]
    image = Image.new('RGB', (height , width))
    pixel = image.load()
    original_pixel = file.load()
    for i in range(height):
        for j in range (width):
            average = round((original_pixel[i , j][0] + original_pixel[i , j][1] + original_pixel[i , j][2])/3)
            pixel[i , j] = (average , average , average)

    image.save("Grayscale_out.bmp")
    print("Grayscaled successfully")
except:
    print("File does not exist")