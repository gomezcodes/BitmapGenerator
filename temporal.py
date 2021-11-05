import os

ejemplo_dir = '/home/sistron/Documentos/Programacion/TrafficLights/GraphicUserInterface/'

contenido = os.listdir(ejemplo_dir)

imagenes = []

for fichero in contenido:
    if os.path.isfile(os.path.join(ejemplo_dir, fichero)) and fichero.endswith('.png'):
        imagenes.append(fichero)

print(imagenes)

print (u"\u00a9")