from modules.tkWindows import *
import modules.classFileChooser as classFileChooser


class GraphicUITrafficLight:

    def __init__(self):

        self.stpsFileData = {}
        self.stpsFilePath = ""
        self.secuenceState = False
        self.root = Tk()
        self.root.config(background="#000000")
        self.root.title("Traffic Lights")
        self.root.geometry("1300x800")
        self.root.minsize(867,730)

        self.SysDate = StringVar(value="10 Agosto 2021 11:11 hrs")
        self.versionNumber = StringVar(value="0.0.1")
        self.graphicSteps= []

        self.WelcomeScreen = WelcomeScreen(self.root,self.gotoMainScreen,self.versionNumber)
        self.MainScreen = MainScreen(self.root,self.gotosetupLightTrafficScreen,
                                    self.gotoconfigScreen,
                                    self.gotophasesConfig,
                                    self.gotooperScreen,
                                    self.SysDate)
        self.SettingsScreen = SettingsScreen(self.root,self.gotoMainScreen,self.save)
        self.TLSettingScreen = LTSettingsScreen(self.root,self.sendConfig,self.gotoMainScreen)
        self.PhasesSettingScreen =  PhasesSettingScreen(self.root)
        self.OperationScreen = OperationScreen(self.root,self.gotoMainScreen,self.loadPhases,self.startSecuence)


    def gotoMainScreen(self):
        self.WelcomeScreen.hide()
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
        classFileChooser.saveFile({})
    
    def loadPhases(self):
        self.stpsFilePath,self.stpsFileData = classFileChooser.openFile()
        self.OperationScreen.secuences = self.stpsFileData

        if self.stpsFileData != None and self.stpsFilePath != None:
            self.OperationScreen.loadPhasesFileButton["state"] = "active"
    
    def startSecuence(self):
        self.secuenceState = True

    def refreshScreen(self,sysDate):
        self.root.update_idletasks()
        self.root.update()
        self.SysDate.set(sysDate)

    def destroyWindow(self):
        self.root.quit()
        self.root.destroy()

    def exitProtocol(self,protocolFunction):
        self.root.protocol("WM_DELETE_WINDOW",protocolFunction)
        


if __name__ == "__main__":
    exampleGUI = GraphicUITrafficLight()
    exampleGUI.root.mainloop()


""" self.SupervisorKey = StringVar()
self.ServiceKey = StringVar()
self.SysKey	= StringVar()
self.LightTrafficNumber = IntVar(value=0)
self.LightModeHour = StringVar()
self.NightBrightLevel = IntVar()
self.LightTrafficId = StringVar()
self.TxLightTrafficConfig =StringVar() """