import os
from convertidordeimagen import generateBitmap

"""___________________________________________________________________________________________"""
ejemplo_dir = os.getcwd()

contenido = os.listdir(ejemplo_dir)

imagenes = []

for fichero in contenido:
    if os.path.isfile(os.path.join(ejemplo_dir, fichero)) and fichero.endswith('.png'):
        imagenes.append(fichero)

print(imagenes)
"""___________________________________________________________________________________________"""

"""___________________________________________________________________________________________"""


commands = {
    "DEMOON" : b'\x5A\x08\x04\x84\x00\x00\x01',
    "DEMOOFF" : b'\x5A\x08\x04\x84\x00\x00\x00',
    "SAVE" : b'\x5A\x08\x04\x84\x00\x01\x01',
    "BLINKOFF" : b'\x5A\x08\x05\x80\x00\x01\x00\x00',
    "BLINKON" : b'\x5A\x08\x05\x80\x00\x01\x00\x01',
    "BITMAP1" : b'\x5A\x08\x05\x80\x00\x00\x00\x00',
    "BITMAP2" : b'\x5A\x08\x05\x80\x00\x00\x00\x01',
    "BITMAP3" : b'\x5A\x08\x05\x80\x00\x00\x00\x02',
    "BITMAP4" : b'\x5A\x08\x05\x80\x00\x00\x00\x03',
    "BRIGHTH" : b'\x5A\x08\x05\x80\x00\x08\x07\xD0',
    "BRIGHTL" : b'\x5A\x08\x05\x80\x00\x08\x00\x03',
}

a= b'\x5A\x08\x05\x80\x00\x01\x00\x00'
b= b'\xFF\xff'
c = a + b

print(c)
if a in list(commands.values()):
    print("yes")
else:
    print("no")
print(len(commands.get("BLINKOFF")))

 
"""___________________________________________________________________________________________"""

"""___________________________________________________________________________________________"""

def queseyo():
    lista=[]
    for i in range(10):
        lista.append(i)
    return lista[0:5], lista[5:10]
parte1,parte2 = queseyo()
print(parte1)
print(parte2)

"""___________________________________________________________________________________________"""

"""___________________________________________________________________________________________"""

listaA=[0x50,0x51,0x52]

listaB=listaA
listaB.append(0x00);listaB.append(0x01)

print(listaB)

"""___________________________________________________________________________________________"""

"""___________________________________________________________________________________________"""

brightValue = 100
brightValue = int((brightValue*2000)/100.0)
tobytes = brightValue.to_bytes(2, byteorder='big')
BRIGHt = list(b'\x5A\x08\x05\x80\x00\x08')

BRIGHt.append(tobytes[0])
BRIGHt.append(tobytes[1])

if 90 in BRIGHt:
    print(BRIGHt)
print(len(BRIGHt))

"""___________________________________________________________________________________________"""

"""___________________________________________________________________________________________"""
#a,b = generateBitmap('d:\VSCode\Folders\TrafficLights\GUI\BitmapGenerator\circulo.png')

a= [0,1]
b= [(0,1),(2,3)]

if type(a[0]) == int:
    print(a)

if type(b[0]) == tuple:
    print(b)

"""___________________________________________________________________________________________"""

"""___________________________________________________________________________________________"""


"""hexadecimalI = int(input("numero:"),16)
hexadecimalII = hexadecimalI
hexadecimalII += 64

addressValueToBytes = hexadecimalI.to_bytes(2, byteorder='big')
print(addressValueToBytes[1],addressValueToBytes[0])
print(hexadecimalI,hexadecimalII,type(hexadecimalI))
"""
print(type(None))

"""___________________________________________________________________________________________"""

"""___________________________________________________________________________________________"""

bitmap = "BITMAP1"
x = (int(bitmap[-1:])+2)

print(x)

btmaddr = 1024
bitmapAddress = [0X0000,0X0400,0X0180,0X0580,0X0200,0X0600,0X0380,0X0780]

if btmaddr in bitmapAddress:
    print("it is    !!")
else:
    print("it's not  :c!")

"""___________________________________________________________________________________________"""

"""___________________________________________________________________________________________"""
