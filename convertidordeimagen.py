
from PIL import Image


def generateBitmap(file):
    posicionesbyte =[
    24, 26, 28, 30, 56, 58, 60, 62, 25, 27, 29, 31, 
    57, 59, 61, 63, 16, 18, 20, 22, 48, 50, 52, 54, 
    17, 19, 21, 23, 49, 51, 53, 55, 8, 10, 12, 14, 
    40, 42, 44, 46,9, 11, 13, 15,41, 43, 45, 47, 
    0, 2, 4, 6, 32, 34, 36, 38, 1, 3, 5, 7, 
    33, 35, 37, 39, 88, 90, 92, 94, 120, 122, 124, 126, 
    89, 91, 93, 95, 121, 123, 125, 127, 80, 82, 84, 86, 112, 114, 116, 118, 
    81, 83, 85, 87, 113, 115, 117, 119, 72, 74, 76, 78, 104, 106, 108, 110, 
    73, 75, 77, 79, 105, 107, 109, 111, 64, 66, 68, 70, 
    96, 98, 100, 102, 65, 67, 69, 71, 97, 99, 101, 103]

    #cargar imagen 
    img = Image.open(file)
    #obtener una lista de los valores de los pixeles
    pixels = list(img.getdata())

    threshold = 10
    print(pixels)
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

    print(newPixels)

    """"
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


    invertedListOfBytes = []

    for check in range(128):
        if(posicionesbyte[check] % 2 == 0):
            byteNoInverted=preOrderListOfBytes[check]
            byteInverted=byteNoInverted[::-1]
            invertedListOfBytes.append(byteInverted)

            #print("<" + str(check)+ " " +str(posicionesbyte[check]) + ">")
        else:
            invertedListOfBytes.append(preOrderListOfBytes[check])
            #print(str(check)+ " " +str(posicionesbyte[check]))

    orderListOfBytes = [
    0,0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,]

    for secuence in range(128):
        orderListOfBytes[posicionesbyte[secuence]] = invertedListOfBytes[secuence]

    hexListOfBytes = []

    for i in range(128):
        hexListOfBytes.append(int(orderListOfBytes[i],2))

    return hexListOfBytes[0:64], hexListOfBytes[64:128]
    






