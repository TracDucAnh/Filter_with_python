import math
from PIL import Image
file_name = input("Input file name.format(must be bmp): ")

try:
    file = Image.open(file_name)
    height = file.size[0]
    width = file.size[1]
    original_pixel = file.load()
    image = Image.new('RGB', (height, width))
    pixel = image.load()
    for i in range(height):
        for j in range(width):
            red = original_pixel[i , j][0]
            green = original_pixel[i , j][1]
            blue = original_pixel[i , j][2]
            sepiaRed = 0.393 * red + 0.769 * green + 0.189 * blue
            if (sepiaRed > 255):
                sepiaRed = 255
            sepiaGreen = 0.349 * red + 0.686 * green + 0.168 * blue
            if (sepiaGreen > 255):
                sepiaGreen = 255
            sepiaBlue = 0.272 * red + 0.534 * green + 0.131 * blue
            if (sepiaBlue > 255):
                sepiaBlue = 255
            red = round(sepiaRed)
            green = round(sepiaGreen)
            blue = round(sepiaBlue)
            pixel[i , j] = (red , green , blue)
    image.save('Sepia_out.bmp')
    print("Successfully filtered")
except:
    print("File does not exist")