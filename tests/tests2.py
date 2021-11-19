from classSerial import *
from classTkinter import *

#DEBUG = FALSE

serialConnection = None
runningProgram = True

def stopProgram():
    global runningProgram ; runningProgram = False

    if serialConnection:
        interfazTL.close()
        exit()

    graphicUserInterface.destroyWindow()



try:
    interfazTL = InterfazOnTerminal("/dev/ttyUSB0",19200)
    serialConnection = True
except:
    pass

graphicUserInterface = GraphicUITrafficLight()
graphicUserInterface.exitProtocol(stopProgram)

while runningProgram:
    graphicUserInterface.refreshScreen()

    if serialConnection:
        
        chooseBitmap = input("mandar")

        if chooseBitmap in list(interfazTL.commands.keys()):
            interfazTL.write(interfazTL.commands.get(chooseBitmap))
            graphicUserInterface.root.title("Hola")
            print("done")
