from tkinter import *
from tkinter import ttk

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

    def __init__(self,root,cmdSavePhases,cmdGotoMainScreen,cmdLoadFile) -> None:
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

        Button(self.logicPhasesFrame, text="SAVE FILE", command= cmdSavePhases,width=20,height=5).pack(side=BOTTOM,fill=BOTH,padx=10,pady=10,expand=1)
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

class OperationScreen():

    def __init__(self,root,cmdGotoMainScreen,cmdStartSecuence) -> None:
        
        self.operScreen = Frame(root, height = 400, width= 800, bg="lightgreen")
        Button(self.operScreen,text="PAGINA PRINCIPAL", command= cmdGotoMainScreen).pack(padx=40,pady=35)
        Button(self.operScreen,text="begin secuence",command=cmdStartSecuence).pack(padx=40,pady=40)

    def show(self):
        self.operScreen.pack()

    def hide(self):
        self.operScreen.pack_forget()
