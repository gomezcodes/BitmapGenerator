import serial
import time
from convertidordeimagen import generateBitmap
from termcolor import colored,cprint
import serial.tools.list_ports_linux
import os


BYTES = 64

uartCommands = {
	"DEMOON" 	: b'\x5A\x08\x04\x84\x00\x00\x01',
	"DEMOOFF" 	: b'\x5A\x08\x04\x84\x00\x00\x00',
	"SAVE" 		: b'\x5A\x08\x04\x84\x00\x01\x01',
	"BLINKOFF" 	: b'\x5A\x08\x05\x80\x00\x01\x00\x00',
	"BLINKON" 	: b'\x5A\x08\x05\x80\x00\x01\x00\x01',
	"BITMAP1" 	: b'\x5A\x08\x05\x80\x00\x00\x00\x00',
	"BITMAP2" 	: b'\x5A\x08\x05\x80\x00\x00\x00\x01',
	"BITMAP3" 	: b'\x5A\x08\x05\x80\x00\x00\x00\x02',
	"BITMAP4" 	: b'\x5A\x08\x05\x80\x00\x00\x00\x03',
	"BRIGHTH" 	: b'\x5A\x08\x05\x80\x00\x08\x07\xD0',
	"BRIGHTL" 	: b'\x5A\x08\x05\x80\x00\x08\x00\x03',
	"COLOR"	  	: [0x5A,0X08,0X05,0X80,0x00],
	"LOAD"	  	: None,
}

def scanUARTPorts():
	ports = serial.tools.list_ports_linux.comports()
	cprint("Available ports","red")
	for port in ports:
		string = str(ports.index(port))+ ". " + port.device + " " + port.description
		cprint(string,'green')           

	devicePort = int(input("Select usb device (index)\n>"))
	portIDSelected= ports[devicePort].device 
	portSelectedDescription = ports[devicePort].description

	return portIDSelected,portSelectedDescription

def switchMenuCommand(receivedCommand):

	if receivedCommand in uartCommands:
		processUARTCommand(receivedCommand)
	elif receivedCommand == "HELP":
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
	else:
		print("comando incorrecto!")

def processUARTCommand(command):

	if command == "LOAD":
		processLoadCommand()
	elif command == "COLOR":
		changeColor(commandSelected[1],commandSelected[2])
	else:
		device.write(uartCommands.get(command))
	print("<Command: " + command + " sent correctly!>")

	"""
		TO DO: VERIFICAR LA RESPUESTA DEL ESCLAVO
		validateSlaveAnswer()
	"""

def processLoadCommand():

	selectedImagePath = selectImage()
	
	bitmapPart1,bitmapPart2 = generateBitmap(selectedImagePath)
	
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

def selectImage():
	imagesPath = os.getcwd()
	imagesOnPath = os.listdir(imagesPath)
	imagenes = []

	for fichero in imagesOnPath:
		if (os.path.isfile(os.path.join(imagesPath, fichero))) and (fichero.endswith('.png')):
			imagenes.append(fichero)
		
	cprint("Available Images: ","green")		
	for image in imagenes:
		string = str(imagenes.index(image))+ ". " + image		
		cprint(string,'green')  

	selectedImage = int(input("Select image (index)\n>"))
	imagePath = imagenes[selectedImage]

	return imagePath

def changeColor(bitmap,Color):

	basicColorCommand = uartCommands.get("COLOR")
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

cprint('''
		__________________________________________
		|                                         |
		| TRAFFIC LIGHT SIMPLE CONTROL INTERFACE  |
		|                 V0.0.0                  |
		|_________________________________________|

 		''', 'magenta',attrs=['bold'])

portID,portDescription = scanUARTPorts()

try:
	device = serial.Serial(portID,baudrate = 19200)
	string = "Succesfully conected to: " + portDescription
	cprint(string,"green")
except:
	cprint("Unable to connect","red")

while True:

	commandSelected = input(">").upper()
	commandSelected = commandSelected.split(' ')
	
	if commandSelected[0] == "EXIT":
		break	
	switchMenuCommand(commandSelected[0])


device.close()

