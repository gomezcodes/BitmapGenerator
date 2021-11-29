from modules.classSerial import scanPorts
from modules.classSerial import *
from modules.classTkinter import *


serialConnection = None
runningProgram = True

def stopProgram():
    global runningProgram ; runningProgram = False

    if serialConnection:
        #interfazTL.close()
        exit()

    graphicUserInterface.destroyWindow()

""" print(scanPorts())
serialPort = input("Select Device if available:")
serialBaudrate = input("Baudrate:") """


""" try:
    interfazTL = serialInterface(serialPort,serialBaudrate)
    serialConnection = True
except:
    runningProgram = False """

graphicUserInterface = GraphicUITrafficLight()

graphicUserInterface.exitProtocol(stopProgram)

while runningProgram:
    graphicUserInterface.refreshScreen()

    if serialConnection:
        
        """ chooseBitmap = input("mandar")

        if chooseBitmap in list(interfazTL.commands.keys()):
            interfazTL.write(interfazTL.commands.get(chooseBitmap))
            graphicUserInterface.root.title("Hola")
            print("done") """
