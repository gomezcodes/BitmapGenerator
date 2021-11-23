import serial
import time
from bitmapGenerator import generateBitmap
from termcolor import colored,cprint
import os
import platform

SYSTEMOS = platform.system()
if SYSTEMOS == "Windows":
	import serial.tools.list_ports_windows
elif SYSTEMOS == "Linux":
	import serial.tools.list_ports_linux
else:
	print(SYSTEMOS)
print("Working on #" + SYSTEMOS)

BASECOMMAND = 0
ATTRIBUTE1 = 1
ATTRIBUTE2 = 2
BYTES = 64

bitmapAddress = [0X0000,0X0400,0X0180,0X0580,0X0200,0X0600,0X0380,0X0780]

uartCommands = {
	"DEMOON" 	: b'\x5A\x08\x04\x84\x00\x00\x01',
	"DEMOOFF" 	: b'\x5A\x08\x04\x84\x00\x00\x00',
	"SAVE" 		: b'\x5A\x08\x04\x84\x00\x01\x01',
	"BLINKOFF" 	: b'\x5A\x08\x05\x80\x00\x01\x00\x00',
	"BLINKON" 	: b'\x5A\x08\x05\x80\x00\x01\x00\x01',
	"BLINKTIME" : b'\x5A\x08\x05\x80\x00\x07',
	"BITMAP1" 	: b'\x5A\x08\x05\x80\x00\x00\x00\x00',
	"BITMAP2" 	: b'\x5A\x08\x05\x80\x00\x00\x00\x01',
	"BITMAP3" 	: b'\x5A\x08\x05\x80\x00\x00\x00\x02',
	"BITMAP4" 	: b'\x5A\x08\x05\x80\x00\x00\x00\x03',
	"BRIGHT" 	: b'\x5A\x08\x05\x80\x00\x08',
	"COLOR"	  	: b'\x5A\x08\x05\x80\x00',
	"LOAD"	  	: b'\x5A\x08\x43\x82',
}


def scanUARTPorts():

	while True:

		if SYSTEMOS == "Windows":
			ports = serial.tools.list_ports_windows.comports()
		else:
			ports = serial.tools.list_ports_linux.comports()

		if len(ports) == 0:
			cprint("No ports available!","red")
			portIDSelected,portSelectedDescription = None, None
			retryOption = input("Rescan y/n \n>")

			if retryOption == ("n" or "N"):
				break

		else:
			cprint("Available ports","green")
			for port in ports:
				string = str(ports.index(port))+ ". " + port.device + " " + port.description
				cprint(string,'green')        
			devicePort = int(input("Select usb device (index)\n>"))
			try:	
				portIDSelected= ports[devicePort].device 
				portSelectedDescription = ports[devicePort].description
				break
			except IndexError:
				cprint("Error! port selected is not available!","red",attrs=["bold"])

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
	[BLINKON]...................Blink Display
	[BLINKOFF]..................Stop blink 
	[BLINKTIME <VALUE>].........Set blink time (miliseconds)
	[BRIGHT <VALUE>]............Set brightness (percentage)
	[COLOR <BITMAP> <COLOR>]....Changes <COLOR> of <BITMAP>
		
		<BITMAP>	<COLOR>
		BITMAP1		RED
		BITMAP2 	GREEN
		BITMAP3		YELLOW
		BITMAP4		BLUE
			    	CYAN
			    	PINK
			    	WHITE

	[LOAD <ADDRESS>]............Write to bitmap

		<ADRESS>
			0X0000	0X0400
			0X0180	0X0580
			0X0200	0X0600
			0X0380	0X0780

	[SAVE]......................Save data to EEPROM
	
	[EXIT] 
			''','green',attrs=['dark'])
	else:
		cprint("Wrong Command!","red",attrs=["bold"])

def processUARTCommand(command):

	#try:
	if command == "LOAD":
		commandSent = processLoadCommand(int(commandSelected[ATTRIBUTE1],16))
	elif command == "COLOR":
		commandSent = processChangeColorCommand(commandSelected[ATTRIBUTE1],commandSelected[ATTRIBUTE2])
	elif command == "BRIGHT":
		commandSent = processBrightCommand(int(commandSelected[ATTRIBUTE1]))
	elif command == "BLINKTIME":
		commandSent = processBlinkCommand(int(commandSelected[ATTRIBUTE1]))
	else:
		device.write(uartCommands.get(command))
		commandSent = uartCommands.get(command)
	#except:
		#cprint("Syntax error, for more info type 'help'","red",attrs=["bold"])
		#commandSent = None

	if commandSent == "Success":
		pass
	elif commandSent != None:
		device.reset_input_buffer()

		slaveAnswer = device.read(len(commandSent))

		if slaveAnswer == commandSent:
			print("Slave answered " + str(slaveAnswer) + "thus, all is working properly!")
		else:
			print("Slave answer do not match send command")
			print(slaveAnswer)
			print(commandSent)
	else:
		print("Error sending command, try again")


	"""
		TO DO: VERIFICAR LA RESPUESTA DEL ESCLAVO
		validateSlaveAnswer()
	"""


def processLoadCommand(startAddress):

	if startAddress in bitmapAddress:

		addressPart1 = startAddress
		addressPart2 = addressPart1 + 64
		addressValueToBytesPart1 = addressPart1.to_bytes(2, byteorder='big')
		addressValueToBytesPart2 = addressPart2.to_bytes(2, byteorder='big')
		preLoadCommandFirstPart = list(uartCommands.get("LOAD"))
		preLoadCommandSecondPart = list(uartCommands.get("LOAD"))

		preLoadCommandFirstPart.append(addressValueToBytesPart1[0])
		preLoadCommandFirstPart.append(addressValueToBytesPart1[1])
		preLoadCommandSecondPart.append(addressValueToBytesPart2[0])
		preLoadCommandSecondPart.append(addressValueToBytesPart2[1])


		selectedImagePath = selectImage()
		bitmapPart1,bitmapPart2 = generateBitmap(selectedImagePath)


		for i in range(BYTES):
			preLoadCommandFirstPart.append(bitmapPart1[i])
			preLoadCommandSecondPart.append(bitmapPart2[i])

		loadCommandFirstPart = bytearray(preLoadCommandFirstPart)
		loadCommandSecondPart = bytearray(preLoadCommandSecondPart)

		device.reset_input_buffer()

		device.write(loadCommandFirstPart)
		slaveAnswerFirstPart = device.read(len(loadCommandFirstPart))
		
		device.write(loadCommandSecondPart)
		slaveAnswerSecondPart = device.read(len(loadCommandFirstPart))

		if (slaveAnswerFirstPart == loadCommandFirstPart) and (slaveAnswerSecondPart == loadCommandSecondPart):

			print("Slave answered correctly,thus all is working properly!")
			return "Success"
		else:
			print("Slave answer do not match send command")
			return None

	else:
		cprint("Bitmap address unavailable","red",attrs=["bold"])
		return None


def selectImage():
	imagesPath = os.getcwd()
	imagesPath = imagesPath.replace("modules","images") 
	imagesOnPath = os.listdir(imagesPath)
	imagenes = []

	for fichero in imagesOnPath:
		if (os.path.isfile(os.path.join(imagesPath, fichero))) and ((fichero.endswith('.png')) or (fichero.endswith('.jpeg'))):
			imagenes.append(fichero)
		
	cprint("Available Images: ","green")		
	for image in imagenes:
		string = str(imagenes.index(image))+ ". " + image		
		cprint(string,'green')  

	selectedImage = int(input("Select image (index)\n>"))
	imagePath = imagenes[selectedImage]

	return imagesPath + "/" + imagePath

def processChangeColorCommand(bitmap,Color):

	try:
		preColorCommand = list(uartCommands.get("COLOR"))
		preColorCommand.append(int(bitmap[-1:])+2)
		preColorCommand.append(0x00)
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
	
		preColorCommand.append(int(color.get(Color)))
		colorCommand = bytearray(preColorCommand)
		device.write(colorCommand)
		return colorCommand
	except:
		cprint("Syntax error, for more info type 'help'","red",attrs=["bold"])
		return None

def processBrightCommand(brightValue):
	brightValue = int((brightValue*2000)/100.0)
	brightValueToBytes = brightValue.to_bytes(2, byteorder='big')

	preBrightCommand = list(uartCommands.get("BRIGHT"))
	preBrightCommand.append(brightValueToBytes[0]);preBrightCommand.append(brightValueToBytes[1])
	brightCommand = bytearray(preBrightCommand)

	device.write(brightCommand)

	return brightCommand

def processBlinkCommand(blinkValue):
	blinkValueToBytes = blinkValue.to_bytes(2, byteorder='big')

	preBlinkCommand = list(uartCommands.get("BLINKTIME"))
	preBlinkCommand.append(blinkValueToBytes[0]);preBlinkCommand.append(blinkValueToBytes[1])
	blinkCommand = bytearray(preBlinkCommand)

	print(blinkCommand)

	device.write(blinkCommand)
	return blinkCommand


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

	commandSelected = input(">_").upper()
	commandSelected = commandSelected.split(' ')
	
	if commandSelected[BASECOMMAND] == "EXIT":
		break	
	switchMenuCommand(commandSelected[BASECOMMAND])

device.close()