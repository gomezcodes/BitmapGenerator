from PIL import Image

#cargar imagen 
img = Image.open("circulo.png")
#obtener una lista de los valores de los pixeles
pixels = list(img.getdata())

threshold = 10

"""
    Convertir los valores de la lista <pixels> en 0's o 1's
"""
newPixels = []
for pixel in pixels:
    # if looks like black, convert to black
    if pixel <= threshold:
        newPixel = (0)
    # if looks like white, convert to white
    else:
        newPixel = (1)
    newPixels.append(newPixel)


"""
    Crear de la lista <newPixels> un string de 0's y 1's
"""
stringpix = ""

for char in newPixels:
    stringpix = stringpix + str(char)


"""
    Ordenar los bits en bytes y agregar a preOrderListOfBytes
"""
preOrderListOfBytes = []
start = 0

for i in range(128):

    byte = stringpix[start:start+8]

    preOrderListOfBytes.append(byte)
    start += 8

print(len(preOrderListOfBytes))

print(preOrderListOfBytes[2])

""" TO DO: 
    1.  REORGANIZAR LOS BYTES PARA ENCAJAR EN LA LOGICA DEL 
        PANEL 32X32
    2.  LOS BYTES EN POSICIONES PARES, INVERTIRLOS.
"""









