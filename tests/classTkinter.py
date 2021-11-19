from tkinter import *
from tkinter import ttk

class GraphicUITrafficLight:

    def __init__(self):

        self.root = Tk()
        self.root.config(background="#000000")
        self.root.title("Traffic Lights")
        self.root.geometry("800x400")
        
        self.VersionNumber = StringVar(value="0.0.0")
        self.SysDate = StringVar(value="10 Agosto 2021 11:11 hrs")
        self.SupervisorKey = StringVar()
        self.ServiceKey = StringVar()
        self.SysKey	= StringVar()
        self.LightTrafficNumber = IntVar(value=0)
        self.LightModeHour = StringVar()
        self.NightBrightLevel = IntVar()
        self.LightTrafficId = StringVar()
        self.TxLightTrafficConfig =StringVar()

        self.welcomeScreen = Frame(self.root, height = 400, width= 800, bg="red")
        self.welcomeScreen.pack()
        Button(self.welcomeScreen,text="INICIO", command= self.gotoMainScreen).pack(padx=10,pady=50)
        Label(self.welcomeScreen,text="LOGOTIPO CLIENTE").pack(pady=20)
        Label(self.welcomeScreen,text="NOMBRE CLIENTE").pack(pady=20)
        Label(self.welcomeScreen,text="VERSION FIRMWARE CONTROL").pack(pady=20);Label(self.welcomeScreen,text=self.VersionNumber.get()).pack(pady=20)
        Label(self.welcomeScreen,text="VERSION FIRMWARE PANTALLA").pack(pady=20)

        self.mainScreen = Frame(self.root, height = 400, width= 800, bg="lightblue")
        Label(self.mainScreen,text=self.SysDate.get()).pack()
        Button(self.mainScreen,text="CONFIGURAR SEMAFOROS", command= self.gotosetupLightTrafficScreen).pack(padx=40,pady=20)
        Button(self.mainScreen,text="CONFIGURAR SISTEMA", command= self.gotoconfigScreen).pack(padx=40,pady=20)
        Button(self.mainScreen,text="CONFIGURACION DE FASES", command= self.gotophasesConfig).pack(padx=40,pady=20)
        Button(self.mainScreen,text="MONITOREAR SISTEMA", command= self.gotooperScreen).pack(padx=40,pady=20)

        self.configScreen = Frame(self.root, height = 400, width= 800, bg="yellow")
        Button(self.configScreen,text="<---", command= self.gotoMainScreen).pack(padx=40,pady=35,side=LEFT)
        Button(self.configScreen,text="GUARDAR", command= self.save).pack(padx=40,pady=35,side=LEFT)
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

        self.setupLightTrafficScreen = Frame(self.root, height = 400, width= 800, bg="pink")
        self.trafficIdSel= ttk.Combobox(self.setupLightTrafficScreen)
        self.trafficIdSel.pack()
        self.trafficIdSel["values"] = ("Semaforo 1","Semaforo 2","Semaforo 3","Semaforo 4","Semaforo 5")
        Button(self.setupLightTrafficScreen,text="ENVIAR CONFIGURACION A SEMAFORO", command= self.sendConfig).pack(padx=40,pady=35)
        Button(self.setupLightTrafficScreen,text="<---", command= self.gotoMainScreen).pack(padx=40,pady=35)

        self.phasesConfigScreen = Frame(self.root, height = 400, width= 800, bg="purple")
        Button(self.phasesConfigScreen, text="GUARDAR CONFIGURACION DE FASES", command= self.savePhases)
        Button(self.phasesConfigScreen,text="<---", command= self.gotoMainScreen).pack(padx=40,pady=35)

        self.operScreen = Frame(self.root, height = 400, width= 800, bg="lightgreen")
        Button(self.operScreen,text="PAGINA PRINCIPAL", command= self.gotoMainScreen).pack(padx=40,pady=35)

    def gotoMainScreen(self):
        self.welcomeScreen.pack_forget()
        self.configScreen.pack_forget()
        self.setupLightTrafficScreen.pack_forget()
        self.phasesConfigScreen.pack_forget()
        self.operScreen.pack_forget()
        self.mainScreen.pack()

    def gotosetupLightTrafficScreen(self):
	    self.mainScreen.pack_forget()
	    self.setupLightTrafficScreen.pack()

    def gotoconfigScreen(self):
	    self.mainScreen.pack_forget()
	    self.configScreen.pack()

    def gotophasesConfig(self):
	    self.mainScreen.pack_forget()
	    self.phasesConfigScreen.pack()

    def gotooperScreen(self):
	    self.mainScreen.pack_forget()
	    self.operScreen.pack()

    def save(self):
	    print("Guardado!")
    
    def sendConfig(self):
	    print("Configuracion enviada a semaforo!")

    def savePhases(self):
	    print("Fases guardadas")

    def refreshScreen(self):
        self.root.update_idletasks()
        self.root.update()

    def destroyWindow(self):
        self.root.quit()
        self.root.destroy()

    def exitProtocol(self,protocolFunction):
        self.root.protocol("WM_DELETE_WINDOW",protocolFunction)
        


if __name__ == "__main__":
    exampleGUI = GraphicUITrafficLight()
    exampleGUI.root.mainloop()
