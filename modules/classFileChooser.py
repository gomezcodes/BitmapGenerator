from tkinter.filedialog import askopenfilename, asksaveasfile
from io import open
import json

class FileChooser():

    def openFile(self):
        self.filePathOpen = askopenfilename(defaultextension="stps")
        
        if len(self.filePathOpen) != 0:
            with open(self.filePathOpen) as file:
                self.jsonDataDict = json.load(file)
        
        return self.filePathOpen,self.jsonDataDict

    def saveFile(self,jsonData):
        self.filePathSave = asksaveasfile(defaultextension="stps") 
        self.filePathSave.close()

        with open(self.filePathSave.name, 'w') as file:
            json.dump(jsonData, file, indent=4)

