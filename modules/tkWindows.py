from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
from tkinter.messagebox import showerror


class WelcomeScreen():

    def __init__(self,root, command,VersionNumber) -> None:

        self.welcomeScreen = Frame(root, height = 400, width= 800, bg="red")
        self.welcomeScreen.pack()
        Button(self.welcomeScreen,text="INICIO", command= command).pack(padx=10,pady=50)
        Label(self.welcomeScreen,text="LOGOTIPO CLIENTE").pack(pady=20)
        Label(self.welcomeScreen,text="NOMBRE CLIENTE").pack(pady=20)
        Label(self.welcomeScreen,text="VERSION FIRMWARE CONTROL").pack(pady=20);Label(self.welcomeScreen,text=VersionNumber.get()).pack(pady=20)
        Label(self.welcomeScreen,text="VERSION FIRMWARE PANTALLA").pack(pady=20)
    
    def show(self):
        self.welcomeScreen.pack()

    def hide(self):
        self.welcomeScreen.pack_forget()
    
class MainScreen():
    
    def __init__(self,root,command0,command1,command2,command3,SysDate) -> None:
        
        self.mainScreen = Frame(root, height = 400, width= 800, bg="lightblue")
        Label(self.mainScreen,textvariable=SysDate).pack()
        Button(self.mainScreen,text="CONFIGURAR SEMAFOROS", command= command0).pack(padx=40,pady=20)
        Button(self.mainScreen,text="CONFIGURAR SISTEMA", command= command1).pack(padx=40,pady=20)
        Button(self.mainScreen,text="CONFIGURACION DE FASES", command= command2).pack(padx=40,pady=20)
        Button(self.mainScreen,text="MONITOREAR SISTEMA", command= command3).pack(padx=40,pady=20)
    
    def show(self):
        self.mainScreen.pack()

    def hide(self):
        self.mainScreen.pack_forget()

class SettingsScreen():

    def __init__(self,root,cmdMainScreen,cmdSave,) -> None:
        
        self.configScreen = Frame(root, height = 400, width= 800, bg="yellow")
        Button(self.configScreen,text="<---", command= cmdMainScreen).pack(padx=40,pady=35,side=LEFT)
        Button(self.configScreen,text="GUARDAR", command= cmdSave).pack(padx=40,pady=35,side=LEFT)
        Label(self.configScreen,text="Hora y Fecha").pack()
        Entry(self.configScreen).pack()
        Label(self.configScreen,text="Contraseña Supervisor").pack()
        Entry(self.configScreen).pack()
        Label(self.configScreen,text="Contraseña Servicio").pack()
        Entry(self.configScreen).pack()
        Label(self.configScreen,text="Llave de Seguridad").pack()
        Entry(self.configScreen).pack()
        Label(self.configScreen,text="Numero de Semaforos").pack()
        Entry(self.configScreen).pack()
        Label(self.configScreen,text="Hora Activacion Modo Nocturno").pack()
        Entry(self.configScreen).pack()
        Label(self.configScreen,text="Nivel de Brillo en Modo Nocturno").pack()
        Entry(self.configScreen).pack()

    def show(self):
        self.configScreen.pack()

    def hide(self):
        self.configScreen.pack_forget()

class LTSettingsScreen():

    def __init__(self,root,cmdSendConfig,cmdMainScreen) -> None:

        self.setupLightTrafficScreen = Frame(root, height = 400, width= 800, bg="pink")
        self.trafficIdSel= ttk.Combobox(self.setupLightTrafficScreen)
        self.trafficIdSel.pack()
        self.trafficIdSel["values"] = ("Semaforo 1","Semaforo 2","Semaforo 3","Semaforo 4","Semaforo 5")
        Button(self.setupLightTrafficScreen,text="ENVIAR CONFIGURACION A SEMAFORO", command= cmdSendConfig).pack(padx=40,pady=35)
        Button(self.setupLightTrafficScreen,text="<---", command= cmdMainScreen).pack(padx=40,pady=35)

    def show(self):
        self.setupLightTrafficScreen.pack()

    def hide(self):
        self.setupLightTrafficScreen.pack_forget()

class PhasesSettingScreen():

    def __init__(self,root) -> None:

        self.rectangleTarget = "STEP"
        self.lineTarget= "LINE"
        self.targetNum = 0
        self.yAxisStart = 50
        self.yAxisEnd = 150
        self.stepsList = []
        self.stepnameVar = StringVar()
        self.bitmapVar = StringVar()
        self.timeStepVar = DoubleVar()
        self.blinkstateVar = BooleanVar()

        self.graphicPhasesFrame = Frame(root, bg="purple")
        self.logicPhasesFrame = Frame(root, bg="lightblue")

        self.canvasFrame = Frame(self.graphicPhasesFrame)
        self.canvasFrame.pack(expand=1)

        self.canvas = Canvas(self.canvasFrame, width=400, height=700, bg="#007acc")
        self.canvas.pack(padx = 0, pady = 0,expand=1,side=LEFT)
        self.vbar=Scrollbar(self.canvasFrame,orient=VERTICAL)
        self.vbar.config(command=self.canvas.yview)
        self.canvas.config(yscrollcommand=self.vbar.set)
        self.canvas.bind("<Button-4>", self.on_mousewheel)
        self.canvas.bind("<Button-5>", self.on_mousewheel)

        Label(self.logicPhasesFrame,text="Step List",font="Forte 15").pack()
        self.stepname = Combobox(self.logicPhasesFrame,textvariable=self.stepnameVar)
        self.stepname["values"] = self.stepsList
        self.stepname.pack()

        Label(self.logicPhasesFrame,text="Bitmap List",font="Forte 15").pack()
        self.bitmap = Combobox(self.logicPhasesFrame,textvariable=self.bitmapVar)
        self.bitmap["values"] = ["Bitmap 1","Bitmap 2","Bitmap 3","Bitmap 4"]
        self.bitmap.pack()

        Label(self.logicPhasesFrame,text="Time on Step (seconds)",font="Forte 15").pack()
        self.timeStep = Entry(self.logicPhasesFrame,textvariable=self.timeStepVar)
        self.timeStep.pack()

        Label(self.logicPhasesFrame,text="Blink (Y/N)",font="Forte 15").pack()
        self.blinkState = Checkbutton(self.logicPhasesFrame,variable=self.blinkstateVar,text="Blink")
        self.blinkState.pack()

        Button(self.logicPhasesFrame,text="Save",command=self.saveSecuence).pack()
        Button(self.logicPhasesFrame,text="ADD",command=self.addStep).pack()
        Button(self.logicPhasesFrame,text="Generate",command=lambda : print("Generate")).pack()
        Button(self.logicPhasesFrame,text="Delete",command=self.deleteStep).pack()
    
    def addStep(self):
        self.targetNum += 1
        self.rectangleTarget += str(self.targetNum)
        self.lineTarget += str(self.targetNum)
        self.canvas.create_rectangle(50,self.yAxisStart,150,self.yAxisEnd,fill="lightblue",activefill="dark slate gray",tags=self.rectangleTarget)
        
        returnLine = self.targetNum*150

        if self.targetNum != 1:
            self.canvas.create_line(100,self.yAxisStart-50,100,self.yAxisEnd-100,arrow=LAST,width = 3, fill="red",tags=self.lineTarget)
            self.canvas.delete("RETURNLINE")
            self.canvas.create_line(100,returnLine,100,returnLine+50,200,returnLine+50,200,100,150,100,arrow=LAST,width = 3, fill="red",tags="RETURNLINE")
        else:
            self.canvas.create_line(100,returnLine,100,returnLine+50,200,returnLine+50,200,100,150,100,arrow=LAST,width = 3, fill="red",tags="RETURNLINE")

        print(self.canvas.coords(self.rectangleTarget))
        
        self.stepsList.append(self.rectangleTarget)
        self.stepname["values"] = self.stepsList
        self.stepname.set(self.rectangleTarget)
        print(self.targetNum)

        self.lineTarget = "LINE"
        self.rectangleTarget = "STEP"
        
        self.yAxisStart += 150
        self.yAxisEnd += 150

    def deleteStep(self):    
        if self.targetNum > 0:
            returnLine  = (self.targetNum-1)*150
            print(self.targetNum)
            targetDelete = self.rectangleTarget + str(self.targetNum)
            line = self.lineTarget + str(self.targetNum)
            self.stepsList.remove(targetDelete)

            self.stepname["values"] = self.stepsList

            self.targetNum -= 1
            print(f"Eliminated {targetDelete}")
            self.canvas.delete(targetDelete)
            self.canvas.delete(line)
            self.canvas.delete("RETURNLINE")
            print(self.canvas.find_all())
            if len(self.canvas.find_all()) != 0:
                self.canvas.create_line(100,returnLine,100,returnLine+50,200,returnLine+50,200,100,150,100,arrow=LAST,width = 3, fill="red",tags="RETURNLINE")
            self.yAxisStart -= 150
            self.yAxisEnd -= 150

    def saveSecuence(self):
        print(f"{self.stepnameVar.get()} {self.bitmapVar.get()} {self.timeStepVar.get()} {self.blinkstateVar.get()}")
        
        if self.stepnameVar.get() == "":
            showerror("ERROR","Fill Blank Spaces")

    def on_mousewheel(self,event):
        if event.num == 4:
            self.canvas.yview_scroll(int(-1*(event.num/4)),"units")

        if event.num == 5:
            self.canvas.yview_scroll(int(event.num/5),"units") 

    def show(self):
        self.graphicPhasesFrame.pack(side=LEFT,fill=BOTH,expand=1)
        self.logicPhasesFrame.pack(side=LEFT,fill=BOTH,expand=1)

    def hide(self):
        self.graphicPhasesFrame.pack_forget()
        self.logicPhasesFrame.pack_forget()

class OperationScreen():

    def __init__(self,root,cmdGotoMainScreen,cmdLoadFile,cmdStartSecuence) -> None:
        self.graphicSteps = [] 
        self.secuences = {}

        self.graphicPhasesFrame = Frame(root, bg="purple")
        self.logicPhasesFrame = Frame(root, bg="lightblue")

        self.canvasFrame = Frame(self.graphicPhasesFrame)
        self.canvasFrame.pack(expand=1)
        
        self.canvas = Canvas(self.canvasFrame, width=400, height=700, bg="#007acc")
        self.canvas.pack(padx = 0, pady = 0,expand=1,side=LEFT)
        self.vbar=Scrollbar(self.canvasFrame,orient=VERTICAL)
        self.vbar.config(command=self.canvas.yview)
        self.canvas.config(yscrollcommand=self.vbar.set)
        self.canvas.bind("<Button-4>", self.on_mousewheel)
        self.canvas.bind("<Button-5>", self.on_mousewheel)

        self.trafficIdSel= ttk.Combobox(self.logicPhasesFrame)
        self.trafficIdSel["values"] = ["Semaforo 1","Semaforo 2","Semaforo 3","Semaforo 4","Semaforo 5"]

        Label(self.logicPhasesFrame,text="This is a ComboBox",font="Helvetica 15").pack()
        self.trafficIdSel.pack(side=TOP,fill=BOTH,padx=10,pady=10,expand=0)

        Label(self.logicPhasesFrame,text="This is a CheckButton",font="Helvetica 15").pack()
        Checkbutton(self.logicPhasesFrame,text="HOLA",width=20,height=1).pack(side=TOP,fill=BOTH,padx=10,pady=10,expand=1)

        Label(self.logicPhasesFrame,text="These are Buttons",font="Helvetica 15").pack()

        #Button(self.logicPhasesFrame, text="SAVE FILE", command= cmdSavePhases,width=20,height=5).pack(side=BOTTOM,fill=BOTH,padx=10,pady=10,expand=1)
        Button(self.logicPhasesFrame,text="begin secuence",command=cmdStartSecuence,width=20,height=5).pack(side=BOTTOM,fill=BOTH,padx=10,pady=10,expand=1)
        Button(self.logicPhasesFrame,text="<- RETURN", command= cmdGotoMainScreen,width=20,height=5).pack(side=BOTTOM,fill=BOTH,padx=10,pady=10,expand=1)
        Button(self.logicPhasesFrame,text="OPEN FILE",command=cmdLoadFile,width=20,height=5).pack(side=BOTTOM,fill=BOTH,padx=10,pady=10,expand=1)
        self.loadPhasesFileButton = Button(self.logicPhasesFrame,text="CARGAR FASES",state="disabled",command=self.generateGraphics,width=20,height=5)
        self.loadPhasesFileButton.pack(side=BOTTOM,fill=BOTH,padx=10,pady=10,expand=1)
        
    def generateGraphics(self):
        yAxisStart = 50
        yAxisEnd = 150
        yAxisText = 90

        for stepID in self.secuences["steps"]:
            step = self.canvas.create_rectangle(50,yAxisStart,150,yAxisEnd,fill="lightblue",
                                            activefill="dark slate gray")
            self.canvas.create_text(250,yAxisText,fill="darkblue",font="Roboto 12 italic bold",text=stepID["stepName"], activefill="dark slate gray")
            self.graphicSteps.append(step)
            yAxisStart += 150
            yAxisEnd += 150
            yAxisText  += 150
        
        yAxisStart = 150
        yAxisEnd = 200
        
        for _ in self.secuences["steps"]:
            step = self.canvas.create_line(100,yAxisStart,100,yAxisEnd,arrow=LAST,width = 3, fill="red")
            yAxisStart += 150
            yAxisEnd += 150

        returnLine = len(self.graphicSteps)*150
        self.canvas.create_line(100,returnLine,100,returnLine+50,200,returnLine+50,200,100,150,100,arrow=LAST,width = 3, fill="red")
        
        self.canvas.config(scrollregion=(0,0,1000,1000))
        """ hbar.pack(side=BOTTOM,fill=X) """
        self.vbar.pack(side=RIGHT,fill=Y)
    
    def on_mousewheel(self,event):
        if event.num == 4:
            self.canvas.yview_scroll(int(-1*(event.num/4)),"units")

        if event.num == 5:
            self.canvas.yview_scroll(int(event.num/5),"units")

    def show(self):
        self.graphicPhasesFrame.pack(side=LEFT,fill=BOTH,expand=1)
        self.logicPhasesFrame.pack(side=LEFT,fill=BOTH,expand=1)

    def hide(self):
        self.graphicPhasesFrame.pack_forget()
        self.logicPhasesFrame.pack_forget()

    
