import math
from PIL import Image

file_name = input("Input file name.format(must be bmp): ")
h = int(input("Average length to blur: "))
try:
    file = Image.open(file_name)
    height = file.size[0]
    width = file.size[1]
    or_pixel= file.load()
    image = Image.new('RGB', (height,width))
    pixel = image.load()
    for i in range(height):
        for j in range(width):
            red = 0
            green = 0
            blue = 0
            index = 0
            for k in range(i - h,i + h + 1):
                for v in range(j - h, j + h + 1):
                    if (k < 0 or k > height - 1):
                        continue
                    elif(v<0 or v> width - 1):
                        continue
                    else:
                        index = index + 1
                        red = red + or_pixel[k,v][0]
                        green = green + or_pixel[k,v][1]
                        blue = blue + or_pixel[k,v][2]
            pixel[i,j] = (round(red / index), round(green / index), round(blue / index))
    image.save("Blur_image_out.bmp")
    print("Successfully blur image")
except:
    print("File does not exist")