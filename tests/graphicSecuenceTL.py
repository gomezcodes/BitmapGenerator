import time
from tkinter import *
import serial
import threading
from BitmapGenerator.modules.classMillis import *

try:
    serialDevice = serial.Serial("COM10",19200)
    print("CONECTED")
except:
    print("NO CONECTED")

secuencueIsActive = False
rootDestroy= False
currentTime = millis()
delay = 0
currentStep = 0

uartCommands = {
	"BLINKOFF" 	: b'\x5A\x08\x05\x80\x00\x01\x00\x00',
	"BLINKON" 	: b'\x5A\x08\x05\x80\x00\x01\x00\x01',
	"BITMAP1" 	: b'\x5A\x08\x05\x80\x00\x00\x00\x00',
	"BITMAP2" 	: b'\x5A\x08\x05\x80\x00\x00\x00\x01',
	"BITMAP3" 	: b'\x5A\x08\x05\x80\x00\x00\x00\x02',
	"BITMAP4" 	: b'\x5A\x08\x05\x80\x00\x00\x00\x03',
}

#[Bitmap, Blink, TimeonStep]
secuencues = [
    ["BITMAP1", False, 10],
    ["BITMAP1", True, 8],
    ["BITMAP2", False, 5],
];BITMAP = 0; BLINKSTATE = 1; TIMEONSTEP = 2


def secuencer(bitmap,blinkState):
    if blinkState:  
        serialDevice.write(uartCommands.get("BLINKON"))
    else:
        serialDevice.write(uartCommands.get("BLINKOFF"))

    time.sleep(0.2)
    serialDevice.write(uartCommands.get(bitmap))


def sayHi():
    Label(root,text="hi").pack(side=TOP)

def stop():
    global secuencueIsActive
    secuencueIsActive = False

def start():
    global secuencueIsActive
    secuencueIsActive = True

def protocolFunction():
    global rootDestroy; rootDestroy = True
    root.quit()
    root.destroy()
    
    

def secuence():
    global secuencueIsActive, rootDestroy, currentTime, delay, currentStep
    while (True):
        time.sleep(0.005)
        if secuencueIsActive:
            if nonBlockingDelay(currentTime,delay) :
                if  currentStep < len(secuencues) :
                    secuencer(secuencues[currentStep][BITMAP],
                              secuencues[currentStep][BLINKSTATE])
                    delay = secuencues[currentStep][TIMEONSTEP]
                    currentTime = millis()
                    for step in range(len(secuencues)):
                        if step == currentStep:
                            canvas.itemconfig(step+1,fill="green")
                        else:
                            canvas.itemconfig(step+1,fill="lightblue")
                    currentStep += 1
                    
                    
                else: 
                    currentStep = 0
        if rootDestroy:
            return 0



secuenceThread = threading.Thread(target=secuence)
secuenceThread.start()

root = Tk()
root.title("Gui Tests")
root.config(bg="black")
root.geometry("700x700") 
root.protocol("WM_DELETE_WINDOW",protocolFunction)
#root.attributes("-fullscreen", True) #Abre la ventana en pantalla completa
#root.resizable(True,False)


canvas = Canvas(root, width=400, height=700, bg="white")
canvas.pack(padx = 5, pady = 5,side=LEFT)

step1 = canvas.create_rectangle(50,50,150,150,fill="lightblue",activefill="dark slate gray",tags="step1")
step2 =canvas.create_rectangle(50,200,150,300,fill="lightblue",activefill="dark slate gray")
step3 = canvas.create_rectangle(50,350,150,450,fill="lightblue",activefill="dark slate gray")
print(step1,step2,step3)
canvas.create_line(100,150,100,200,arrow=LAST,width = 3, fill="red")

canvas.create_line(100,300,100,350,arrow=LAST,width = 3, fill="red")

canvas.create_line(100,450,100,550,200,550,200,100,150,100,arrow=LAST,width = 3, fill="red")

canvas.create_line(100,0,100,600,dash=(3,5))

canvas.create_text(250,90,fill="darkblue",font="Roboto 12 italic bold",text="Step 1", activefill="dark slate gray")
canvas.create_text(250,240,fill="darkblue",font="Roboto 12 italic bold",text="Step 2", activefill="dark slate gray")
canvas.create_text(250,390,fill="darkblue",font="Roboto 12 italic bold",text="Step 3", activefill="dark slate gray")

Button(root,text="Start",command=start).pack(side=RIGHT)
Button(root,text="Stop",command=stop).pack(side=RIGHT)


Button(root,text="Say hi",command=sayHi).pack(side=RIGHT)


root. mainloop()

time.sleep(0.1)
print(secuenceThread.is_alive())

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