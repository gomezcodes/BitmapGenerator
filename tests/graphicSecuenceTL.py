import time
from tkinter import *
import serial

try:
    serialDevice = serial.Serial("/dev/ttyUSB1",19200)
    print("CONECTED")
except:
    print("NO CONECTED")

def secuence():

    while True:
        serialDevice.write(b'\x5A\x08\x05\x80\x00\x00\x00\x00')
        canvas.itemconfig(step1,fill="green")
        root.update()
        time.sleep(5)
        canvas.itemconfig(step1,fill="lightblue")
        root.update()


        serialDevice.write(b'\x5A\x08\x05\x80\x00\x01\x00\x01')
        canvas.itemconfig(step2,fill="green")
        root.update()
        time.sleep(3)
        serialDevice.write(b'\x5A\x08\x05\x80\x00\x01\x00\x00')
        time.sleep(0.1)
        canvas.itemconfig(step2,fill="lightblue")
        root.update()


        serialDevice.write(b'\x5A\x08\x05\x80\x00\x00\x00\x02')
        #time.sleep(0.01)
        #serialDevice.write(b'\x5A\x08\x05\x80\x00\x01\x00\x01')
        canvas.itemconfig(step3,fill="green")
        root.update()
        time.sleep(2)
        canvas.itemconfig(step3,fill="lightblue")
        root.update()

        




root = Tk()
root.title("Gui Tests")
root.config(bg="black")
root.geometry("700x700") 
#root.attributes("-fullscreen", True) #Abre la ventana en pantalla completa
#root.resizable(True,False)


canvas = Canvas(root, width=400, height=700, bg="white")
canvas.pack(padx = 5, pady = 5,side=LEFT)

step1 = canvas.create_rectangle(50,50,150,150,fill="lightblue",activefill="dark slate gray",tags="step1")
canvas.create_line(100,150,100,200,arrow=LAST,width = 3, fill="red")

step2 =canvas.create_rectangle(50,200,150,300,fill="lightblue",activefill="dark slate gray")
canvas.create_line(100,300,100,350,arrow=LAST,width = 3, fill="red")
 
step3 = canvas.create_rectangle(50,350,150,450,fill="lightblue",activefill="dark slate gray")
canvas.create_line(100,450,100,550,200,550,200,100,150,100,arrow=LAST,width = 3, fill="red")

canvas.create_line(100,0,100,600,dash=(3,5))

canvas.create_text(250,90,fill="darkblue",font="Roboto 12 italic bold",text="Step 1", activefill="dark slate gray")
canvas.create_text(250,240,fill="darkblue",font="Roboto 12 italic bold",text="Step 2", activefill="dark slate gray")
canvas.create_text(250,390,fill="darkblue",font="Roboto 12 italic bold",text="Step 3", activefill="dark slate gray")

Button(root,text="Start",command=secuence).pack(side=RIGHT)


root. mainloop()

""" 
DISPLAYS A "RIGHT CLICK" MENU 

def onObjectClick(e):
    print("right clicjed!")
    try:
        m.tk_popup(e.x_root, e.y_root)
    finally:
        m.grab_release()

m = Menu(root, tearoff = 0)
m.add_command(label ="Cut",command=cut)
m.add_command(label ="Copy")
m.add_command(label ="Paste")
m.add_command(label ="Reload")
m.add_separator()
m.add_command(label ="Rename")

canvas.tag_bind(step1, '<ButtonPress-3>', onObjectClick)  """