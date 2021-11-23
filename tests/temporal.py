import os
#from modules.bitmapGenerator import generateBitmap
#from tkinter import *

"""___________________________________________________________________________________________"""
"""___________________________________________________________________________________________"""

import platform
import serial

SYSTEMOS = platform.system()

if SYSTEMOS == "Windows":
	import serial.tools.list_ports_windows
else:
	import serial.tools.list_ports_linux

def scanPorts():
    """ portIDSelected = None
    portSelectedDescription = None """
    availablePorts = []

    if SYSTEMOS == "Windows":
        ports = serial.tools.list_ports_windows.comports()
    else:
	    ports = serial.tools.list_ports_linux.comports()

    if len(ports) != 0:

        for port in ports:
            portAttributes= [port.device,port.description]
            availablePorts.append(portAttributes)

        return availablePorts

    return None

print(scanPorts())

"""___________________________________________________________________________________________"""

"""___________________________________________________________________________________________"""
""" ejemplo_dir = os.getcwd()

contenido = os.listdir(ejemplo_dir)

imagenes = []

for fichero in contenido:
    if os.path.isfile(os.path.join(ejemplo_dir, fichero)) and fichero.endswith('.png'):
        imagenes.append(fichero)

print(imagenes) """
"""___________________________________________________________________________________________"""

"""___________________________________________________________________________________________"""


""" commands = {
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

a= b'\x5A\x08\x05\x80\x00\x01\x00\x00'
b= b'\xFF\xff'
c = a + b

print(c)
print(list(commands.keys()))
if a in list(commands.values()):
    print("yes")
else:
    print("no")
print(len(commands.get("BLINKOFF")))

  """
"""___________________________________________________________________________________________"""

"""___________________________________________________________________________________________"""

""" def queseyo():
    lista=[]
    for i in range(10):
        lista.append(i)
    return lista[0:5], lista[5:10]
parte1,parte2 = queseyo()
print(parte1)
print(parte2) """

"""___________________________________________________________________________________________"""

"""___________________________________________________________________________________________"""

""" listaA=[0x50,0x51,0x52]

listaB=listaA
listaB.append(0x00);listaB.append(0x01)

print(listaB) """

"""___________________________________________________________________________________________"""

"""___________________________________________________________________________________________"""

""" brightValue = 100
brightValue = int((brightValue*2000)/100.0)
tobytes = brightValue.to_bytes(2, byteorder='big')
BRIGHt = list(b'\x5A\x08\x05\x80\x00\x08')

BRIGHt.append(tobytes[0])
BRIGHt.append(tobytes[1])

if 90 in BRIGHt:
    print(BRIGHt)
print(len(BRIGHt)) """

"""___________________________________________________________________________________________"""

"""___________________________________________________________________________________________"""
#a,b = generateBitmap('d:\VSCode\Folders\TrafficLights\GUI\BitmapGenerator\circulo.png')
""" 
a= [0,1]
b= [(0,1),(2,3)]

if type(a[0]) == int:
    print(a)

if type(b[0]) == tuple:
    print(b)
 """
"""___________________________________________________________________________________________"""

"""___________________________________________________________________________________________"""


"""hexadecimalI = int(input("numero:"),16)
hexadecimalII = hexadecimalI
hexadecimalII += 64

addressValueToBytes = hexadecimalI.to_bytes(2, byteorder='big')
print(addressValueToBytes[1],addressValueToBytes[0])
print(hexadecimalI,hexadecimalII,type(hexadecimalI))
"""
""" print(type(None)) """

"""___________________________________________________________________________________________"""

"""___________________________________________________________________________________________"""

""" bitmap = "BITMAP1"
x = (int(bitmap[-1:])+2)

print(x)

btmaddr = 1024
bitmapAddress = [0X0000,0X0400,0X0180,0X0580,0X0200,0X0600,0X0380,0X0780]

if btmaddr in bitmapAddress:
    print("it is    !!")
else:
    print("it's not  :c!")
 """
"""___________________________________________________________________________________________"""

"""___________________________________________________________________________________________"""



"""___________________________________________________________________________________________"""

"""___________________________________________________________________________________________"""

# from tkinter import *
# from tkinter import font

# root = Tk()
# root.geometry("500x500")

# def font_chooser(e):
#     our_font.config(
#         family=my_listbox.get(my_listbox.curselection()))
#     print(my_listbox.get(my_listbox.curselection()))

# our_font = font.Font(family="helvetica",size=32)

# myframe = Frame(root,width=480,height=275)
# myframe.pack()

# myframe.grid_propagate(False)
# myframe.columnconfigure(0,weight=10)


# mytext= Text(myframe,font=our_font)
# mytext.grid(row=0,column=0)
# mytext.grid_rowconfigure(0,weight=1)
# mytext.grid_columnconfigure(0,weight = 1)

# my_listbox = Listbox(root,selectmode=SINGLE, width = 80)
# my_listbox.pack()

# for f in font.families():
#     my_listbox.insert("end",f)

# my_listbox.bind("<ButtonRelease-1>",font_chooser)

# root.mainloop()

"""___________________________________________________________________________________________"""

"""___________________________________________________________________________________________"""



# # Import the required libraries
# from tkinter import *


# # Create an instance of tkinter frame
# win = Tk()

# # Set the size of the tkinter window
# win.geometry("700x350")

# # Define a Canvas widget
# canvas = Canvas(win, width=600, height=400, bg="white")
# canvas.pack(pady=20)

# # Add Images to Canvas widget

# img = canvas.create_rectangle(50,50,100,100)

# # Define a function to allow the image to move within the canvas
# def move(e):

#     canvas.move(img,e.x, e.y)

# canvas.tag_bind(img,"<B1-Motion>", move)  

# # Bind the move function
# #canvas.bind("<B1-Motion>", move)

# win.mainloop()

"""___________________________________________________________________________________________"""

"""___________________________________________________________________________________________"""



""" from tkinter import * 
root = Tk()
canvas = Canvas(root, width=400, height=200)
canvas.pack()
canvas.create_oval(10, 10, 110, 60, fill="grey")
canvas.create_text(60, 35, text="Oval")
canvas.create_rectangle(10, 100, 110, 150, outline="blue")
canvas.create_text(60, 125, text="Rectangle")
canvas.create_line(60, 60, 60, 100, width=3)


class MouseMover():
  def __init__(self):
    self.item = 0; self.previous = (0, 0)
  def select(self, event):
    widget = event.widget                       # Get handle to canvas 
    # Convert screen coordinates to canvas coordinates
    xc = widget.canvasx(event.x); yc = widget.canvasx(event.y)
    self.item = widget.find_closest(xc, yc)[0]        # ID for closest
    self.previous = (xc, yc)
    print((xc, yc, self.item))
  def drag(self, event):
    widget = event.widget
    xc = widget.canvasx(event.x); yc = widget.canvasx(event.y)
    canvas.move(self.item, xc-self.previous[0], yc-self.previous[1])
    self.previous = (xc, yc)


# Get an instance of the MouseMover object
mm = MouseMover()

# Bind mouse events to methods (could also be in the constructor)
canvas.bind("<Button-1>", mm.select)
canvas.bind("<B1-Motion>", mm.drag)

root.mainloop() """


""" imagesPath = os.getcwd()
imagesPath = imagesPath.replace("/modules","/images")

print(imagesPath) """