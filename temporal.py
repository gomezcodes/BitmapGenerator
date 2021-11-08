import os

ejemplo_dir = '/home/sistron/Documentos/Programacion/TrafficLights/GraphicUserInterface/'

contenido = os.listdir(ejemplo_dir)

imagenes = []

for fichero in contenido:
    if os.path.isfile(os.path.join(ejemplo_dir, fichero)) and fichero.endswith('.png'):
        imagenes.append(fichero)

print(imagenes)

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

a="BRIGHTH"




if a in commands:
    print("yes")
else:
    print("no")


def queseyo():
    lista=[]
    for i in range(10):
        lista.append(i)
    return lista[0:5], lista[5:10]
parte1,parte2 = queseyo()
print(parte1)
print(parte2)

listaA=[0x50,0x51,0x52]

listaB=listaA
listaB.append(0x00);listaB.append(0x01)

print(listaB)

