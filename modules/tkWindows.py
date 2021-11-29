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
        Label(self.mainScreen,text=SysDate).pack()
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

    def __init__(self,root,cmdSavePhases,cmdGotoMainScreen) -> None:
        
        self.phasesConfigScreen = Frame(root, height = 400, width= 800, bg="purple")
        Button(self.phasesConfigScreen, text="GUARDAR CONFIGURACION DE FASES", command= cmdSavePhases)
        Button(self.phasesConfigScreen,text="<---", command= cmdGotoMainScreen).pack(padx=40,pady=35)

    def show(self):
        self.phasesConfigScreen.pack()

    def hide(self):
        self.phasesConfigScreen.pack_forget()

class OperationScreen():

    def __init__(self,root,cmdGotoMainScreen) -> None:
        
        self.operScreen = Frame(root, height = 400, width= 800, bg="lightgreen")
        Button(self.operScreen,text="PAGINA PRINCIPAL", command= cmdGotoMainScreen).pack(padx=40,pady=35)

    def show(self):
        self.operScreen.pack()

    def hide(self):
        self.operScreen.pack_forget()
