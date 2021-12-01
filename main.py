from modules.classSerial import scanPorts
from modules.classSerial import *
from modules.classTkinter import *
from modules.classTime import *


serialConnection = None
runningProgram = True

def stopProgram():
    global runningProgram ; runningProgram = False

    if serialConnection:
        uartInterface.close()
        exit()

    graphicUserInterface.destroyWindow()

uartInterface = serialInterface(None,None)

graphicUserInterface = GraphicUITrafficLight()
graphicUserInterface.exitProtocol(stopProgram)

while runningProgram:
    t.sleep(0.001)
    graphicUserInterface.refreshScreen()
    graphicUserInterface.SysDate.set(currentDate())

    if serialConnection:
        print("Serial connection stablished")

