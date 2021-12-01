import serial

puerto = serial.Serial()

puertoID = input("Nombre del Puert:")
baudratePuerto = 19200

puerto.baudrate = baudratePuerto
puerto.port = puertoID

print(puerto)

print(puerto.is_open)

input("open Port?")

puerto.open()

print(puerto.is_open)

puerto.close()

print(puerto.is_open)

