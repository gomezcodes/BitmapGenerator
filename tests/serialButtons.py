import serial.tools.list_ports_linux
import functools
from tkinter import *

def selectDevice(index):
        portID= ports[index].product
        print(str(portID) + "selected")
        Label(root,text=(str(portID) + " selected")).pack()
        for a in range(len(ports)):
            portsList[a].pack_forget()

portsList = []
num = 0
ports = serial.tools.list_ports_linux.comports()

root = Tk()
root.title("Gui Tests")
root.config(bg="black")
root.geometry("700x700") 
#root.attributes("-fullscreen", True) #Abre la ventana en pantalla completa
#root.resizable(True,False)

for p in ports:
                ## Button objects, Displays serial ports as buttons
    portsList.append(Button(root, font= ("Tahoma",14), text=(p.product), width=30,command= functools.partial(selectDevice, index = ports.index(p))))
    portsList[num].pack()
    num += 1

root. mainloop()