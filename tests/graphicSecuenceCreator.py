from tkinter import *
from tkinter.ttk import Combobox
from tkinter.messagebox import showerror

rectangleTarget = "STEP"
lineTarget= "LINE"
targetNum = 0
yAxisStart = 50
yAxisEnd = 150
stepsList = []



secuencues = {}


graphicSteps = []

def saveSecuence():
    print(secuencues)
    
    if stepnameVar.get() == "":
        showerror("ERROR","Fill Blank Spaces")

def botonpresionado(event,eso):
    print(eso)

def updateValues():

    if len(secuencues) != 0:
        secuencues.update({stepnameVar.get():[bitmapVar.get(),timeStepVar.get(),blinkstateVar.get()]})
        print(secuencues)
    



def addStep():
    global rectangleTarget,lineTarget,targetNum,yAxisStart,yAxisEnd

    

    targetNum += 1

    rectangleTarget += str(targetNum)
    
    lineTarget += str(targetNum)
    canvas.create_rectangle(50,yAxisStart,150,yAxisEnd,fill="lightblue",activefill="dark slate gray",tags=rectangleTarget)

    returnLine = targetNum*150

    if targetNum != 1:
        canvas.create_line(100,yAxisStart-50,100,yAxisEnd-100,arrow=LAST,width = 3, fill="red",tags=lineTarget)
        canvas.delete("RETURNLINE")
        canvas.create_line(100,returnLine,100,returnLine+50,200,returnLine+50,200,100,150,100,arrow=LAST,width = 3, fill="red",tags="RETURNLINE")
    else:
        canvas.create_line(100,returnLine,100,returnLine+50,200,returnLine+50,200,100,150,100,arrow=LAST,width = 3, fill="red",tags="RETURNLINE")

    message["text"] = f"Created {rectangleTarget}"
    stepsList.append(rectangleTarget)
    stepname.set(rectangleTarget)
    stepname["values"] = stepsList
    secuencues.update({stepnameVar.get():[bitmapVar.get(),timeStepVar.get(),blinkstateVar.get()]})

    ese=len(stepsList)
    canvas.tag_bind(rectangleTarget,"<Button-1>",lambda event: botonpresionado(event,ese))

    lineTarget = "LINE"
    rectangleTarget = "STEP"
    
    yAxisStart += 150
    yAxisEnd += 150
    if len(secuencues) != 0:
        saveButton["state"] = "normal"




def deleteStep():
    global rectangleTarget,lineTarget,targetNum,yAxisStart,yAxisEnd

    if targetNum > 0:
        returnLine  = (targetNum-1)*150
        print(targetNum)
        targetDelete = rectangleTarget + str(targetNum)
        line = lineTarget + str(targetNum)
        stepsList.remove(targetDelete)

        stepname["values"] = stepsList

        targetNum -= 1
        message["text"] = f"Eliminated {targetDelete}"
        canvas.delete(targetDelete)
        canvas.delete(line)
        canvas.delete("RETURNLINE")
        print(canvas.find_all())
        if len(canvas.find_all()) != 0:
            canvas.create_line(100,returnLine,100,returnLine+50,200,returnLine+50,200,100,150,100,arrow=LAST,width = 3, fill="red",tags="RETURNLINE")
        yAxisStart -= 150
        yAxisEnd -= 150
        secuencues.popitem()

        if len(secuencues) == 0:
            saveButton["state"] = "disabled"


root = Tk()
root.title("Generate Graphic Steps")
root.config(bg="#19266d")
root.geometry("700x700") 

stepnameVar = StringVar()
bitmapVar = StringVar(value="Bitmap 1")
timeStepVar = DoubleVar(value="1.0")
blinkstateVar = StringVar(value="No")
cualquieraVar = BooleanVar(value=True)

message=Label(root,text="THIS IS FOR MESSAGES")
message.pack(side=BOTTOM,expand=1,fill=BOTH)

frame=Frame(root,width=300,height=300)
frame.pack(padx = 10, pady = 10,side=LEFT)

canvas = Canvas(frame, width=400, height=700, bg="#007acc")
canvas.pack(padx = 3, pady = 3,side=LEFT)

vbar=Scrollbar(frame,orient=VERTICAL)
vbar.config(command=canvas.yview)
canvas.config(yscrollcommand=vbar.set)

Label(root,text="Step List",font="Forte 15").pack()
stepname = Combobox(root,textvariable=stepnameVar)
stepname["values"] = stepsList
stepname.pack()

Label(root,text="Bitmap List",font="Forte 15").pack()
bitmap = Combobox(root,textvariable=bitmapVar)
bitmap["values"] = ["Bitmap 1","Bitmap 2","Bitmap 3","Bitmap 4"]
bitmap.pack()

Label(root,text="Time on Step (seconds)",font="Forte 15").pack()
timeStep = Entry(root,textvariable=timeStepVar)
timeStep.pack()

Label(root,text="Blink (Y/N)",font="Forte 15").pack()
blinkState = Combobox(root,textvariable=blinkstateVar)
blinkState["values"] = ["Yes","No"]
blinkState.pack()

blinkState = Checkbutton(root,variable=cualquieraVar)
blinkState.pack()


saveButton = Button(root,text="Save Step",command=updateValues,state="disabled")
saveButton.pack()
Button(root,text="ADD",command=addStep).pack()
Button(root,text="Generate",command=saveSecuence).pack()
Button(root,text="Delete",command=deleteStep).pack()
 
root.mainloop()



""" from tkinter import *

def callback(sv):
    print (sv.get())

root = Tk()
sv = StringVar()
sv.trace("w", lambda name, index, mode, sv=sv: callback(sv))
e = Entry(root, textvariable=sv)
e.pack()
root.mainloop()   """

""" from tkinter import *

root = Tk()
sv = StringVar()

def callback():
    print(sv.get())
    return True

e = Entry(root, textvariable=sv, validate="focus", validatecommand=callback)
e.grid()
e = Entry(root)
e.grid()
root.mainloop() """

""" from tkinter import * 
from tkinter import ttk

class GUI():                              
    def __init__(self):  
        self.root = Tk()
        self.sv = StringVar() 
        self.prevlaue=''
        #entry
        self.entry = ttk.Entry(self.root, width=30, textvariable =self.sv)
        self.entry.grid(pady=20,padx=20) 
        self.entry.bind("<KeyRelease>", self.OnEntryClick) #keyup                  
        self.root.mainloop()       

    def OnEntryClick(self, event):
        value=self.sv.get().strip()
        changed = True if self.prevlaue != value else False
        print(value, 'Text has changed ? {}'.format(changed))
        self.prevlaue = value

#create the gui
GUI() """