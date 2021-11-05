import serial
import time
from convertidordeimagen import generateBitmap
from termcolor import colored,cprint
import serial.tools.list_ports_linux
import os


BYTES = 64


def writeBitmap():
	imagePath = os.getcwd()
	imagesOnPath = os.listdir(imagePath)
	imagenes = []

	for fichero in imagesOnPath:
		if (os.path.isfile(os.path.join(imagePath, fichero))) and (fichero.endswith('.png')):
			imagenes.append(fichero)
		
	cprint("Available Images: ","green")		
	for image in imagenes:
		string = str(imagenes.index(image))+ ". " + image		
		cprint(string,'green')  

	selectedImage = int(input("Select image (index)\n>"))
	imagePath = imagenes[selectedImage]
	
	bitmapList = generateBitmap(imagePath)
	bitmapPart1 = bitmapList[0:64]
	bitmapPart2 = bitmapList[64:128]
	bitmapCommandPart1 = [0x5A,0X08,0X43,0X82,0X00,0X00]
	bitmapCommandPart2 = [0x5A,0X08,0X43,0X82,0X00,0X40]

	for i in range(BYTES):
		bitmapCommandPart1.append(bitmapPart1[i])
		bitmapCommandPart2.append(bitmapPart2[i])

	commandWriteBitmap1 = bytearray(bitmapCommandPart1)
	commandWriteBitmap2 = bytearray(bitmapCommandPart2)

	device.write(commandWriteBitmap1)
	time.sleep(1)
	device.write(commandWriteBitmap2)

def changeColor(bitmap,Color):
	basicColorCommand = [0x5A,0X08,0X05,0X80,0x00]
	basicColorCommand.append(int(bitmap[-1:])+2)
	basicColorCommand.append(0x00)
	color = {
		"RED":"0",
		"GREEN":"1",
		"BLUE":"2",
		"YELLOW":"3",
		"PINK":"4",
		"CYAN":"5",
		"WHITE":"6",
		"BLACK":"7",
	}
	basicColorCommand.append(int(color.get(Color)))
	colorCommand = bytearray(basicColorCommand)
	device.write(colorCommand)


commandDemoOn = b'\x5A\x08\x04\x84\x00\x00\x01'
commandDemoOff = b'\x5A\x08\x04\x84\x00\x00\x00'
commandSaveData = b'\x5A\x08\x04\x84\x00\x01\x01'
commandBlinkOff = b'\x5A\x08\x05\x80\x00\x01\x00\x00'
commandBlinkOn = b'\x5A\x08\x05\x80\x00\x01\x00\x01'
commandBitmap1 = b'\x5A\x08\x05\x80\x00\x00\x00\x00'
commandBitmap2 = b'\x5A\x08\x05\x80\x00\x00\x00\x01'
commandBitmap3 = b'\x5A\x08\x05\x80\x00\x00\x00\x02'
commandBitmap4 = b'\x5A\x08\x05\x80\x00\x00\x00\x03'
commandBrightHigh = b'\x5A\x08\x05\x80\x00\x08\x07\xD0'
commandBrightLow = b'\x5A\x08\x05\x80\x00\x08\x00\x03'

cprint('''
		__________________________________________
		|                                         |
		| TRAFFIC LIGHT SIMPLE CONTROL INTERFACE  |
		|                 V0.0.0                  |
		|_________________________________________|

 		''', 'magenta',attrs=['bold'])

ports = serial.tools.list_ports_linux.comports()
cprint("Available ports","red")
for port in ports:
	string = str(ports.index(port))+ ". " + port.device + " " + port.description
	cprint(string,'green')           

devicePort = int(input("Select usb device (index)\n>"))
portID= ports[devicePort].device 
portDescription = ports[devicePort].description

try:
	device = serial.Serial(portID,baudrate = 19200)
	string = "Succesfully conected to: " + portDescription
	cprint(string,"green")
except:
	cprint("Unable to connect","red")

while True:

	commandSelected = input(">").upper()
	commandSelected = commandSelected.split(' ')

	if commandSelected[0] == "DEMOON":
		device.write(commandDemoOn)
		print("<Demo on>")
	elif commandSelected[0] == "DEMOOFF":
		device.write(commandDemoOff)
		print("<Demo off>")
	elif commandSelected[0] == "SAVE":
		device.write(commandSaveData)
		print("<EEPROM updated>")
	elif commandSelected[0] == "BITMAP1":
		device.write(commandBitmap1)
		print("<BITMAP 1 SELECTED>")
	elif commandSelected[0] == "BITMAP2":
		device.write(commandBitmap2)
		print("<BITMAP 2 SELECTED>")
	elif commandSelected[0] == "BITMAP3":
		device.write(commandBitmap3)
		print("<BITMAP 3 SELECTED>")
	elif commandSelected[0] == "BITMAP4":
		device.write(commandBitmap4)
		print("<BITMAP 4 SELECTED>")
	elif commandSelected[0] == "BLINKON":
		device.write(commandBlinkOn)
		print("<BLINK ON>")		
	elif commandSelected[0] == "BLINKOFF":
		device.write(commandBlinkOff)
		print("<BLINK OFF>")	
	elif commandSelected[0] == "LOAD":
		writeBitmap()
		print("<BITMAP WRITED>")	
	elif commandSelected[0] == "BRIGHT+":
		device.write(commandBrightHigh)
		print("<BRIGHTNESS CHANGED (HIGH)>")	
	elif commandSelected[0] == "BRIGHT-":
		device.write(commandBrightLow)
		print("<BRIGHTNESS CHANGED (LOW)>")
	elif commandSelected[0] == "COLOR":
		changeColor(commandSelected[1],commandSelected[2])
		print("<" + str(commandSelected[1]) + " COLOR CHANGED TO: " + str(commandSelected[2]) + ">")
	elif commandSelected[0] == "HELP":
		cprint('''

		traffic light simple control interface v0.0.0	

	[DEMOON]....................Enter demo mode
	[DEMOOFF]...................Exit demo mode
	[BITMAP1]...................Display bitmap1
	[BITMAP2]...................Display bitmap2
	[BITMAP3]...................Display bitmap3
	[BITMAP4]...................Display bitmap4
	[COLOR <BITMAP> <COLOR>]....Changes <COLOR> of <BITMAP>
	[BLINKON]...................Blink Display
	[BLINKOFF]..................Stop blink 
	[LOAD]......................Write to bitmap
	[SAVE]......................Save data to EEPROM
	[BRIGHT+]...................Higher brightness
	[BRIGHT-]...................Lower brightness
	
	[EXIT] 
			''','green',attrs=['dark'])
	elif commandSelected[0] == "EXIT":
		break	
	else:
		print("comando incorrecto!")
#except:
#	print("No serial Device Detected")
device.close()

