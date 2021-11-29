from modules.tkWindows import *

class GraphicUITrafficLight:

    def __init__(self):

        self.root = Tk()
        self.root.config(background="#000000")
        self.root.title("Traffic Lights")
        self.root.geometry("800x400")

        self.SysDate = StringVar(value="10 Agosto 2021 11:11 hrs")
        self.SupervisorKey = StringVar()
        self.ServiceKey = StringVar()
        self.SysKey	= StringVar()
        self.LightTrafficNumber = IntVar(value=0)
        self.LightModeHour = StringVar()
        self.NightBrightLevel = IntVar()
        self.LightTrafficId = StringVar()
        self.TxLightTrafficConfig =StringVar()
        self.versionNumber = StringVar(value="0.0.1")

        self.WelcomeScreen = WelcomeScreen(self.root,self.gotoMainScreen,self.versionNumber)
        self.MainScreen = MainScreen(self.root,self.gotosetupLightTrafficScreen,
                                    self.gotoconfigScreen,
                                    self.gotophasesConfig,
                                    self.gotooperScreen,
                                    self.SysDate.get())
        self.SettingsScreen = SettingsScreen(self.root,self.gotoMainScreen,self.save)
        self.TLSettingScreen = LTSettingsScreen(self.root,self.sendConfig,self.gotoMainScreen)
        self.PhasesSettingScreen =  PhasesSettingScreen(self.root,self.savePhases,self.gotoMainScreen)
        self.OperationScreen = OperationScreen(self.root,self.gotoMainScreen)


    def gotoMainScreen(self):
        self.WelcomeScreen.hide()
        #self.welcomeScreen.pack_forget()
        self.SettingsScreen.hide()
        self.TLSettingScreen.hide()
        self.PhasesSettingScreen.hide()
        self.OperationScreen.hide()
        self.MainScreen.show()

    def gotosetupLightTrafficScreen(self):
	    self.MainScreen.hide()
	    self.TLSettingScreen.show()

    def gotoconfigScreen(self):
	    self.MainScreen.hide()
	    self.SettingsScreen.show()

    def gotophasesConfig(self):
	    self.MainScreen.hide()
	    self.PhasesSettingScreen.show()

    def gotooperScreen(self):
	    self.MainScreen.hide()
	    self.OperationScreen.show()

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
