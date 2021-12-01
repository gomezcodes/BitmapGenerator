from tkinter.filedialog import askopenfilename, asksaveasfile
from io import open
import json



def openFile():
    filePathOpen = askopenfilename(defaultextension="stps")
        
    if len(filePathOpen) != 0:
        with open(filePathOpen) as file:
            jsonDataDict = json.load(file)
            return filePathOpen,jsonDataDict

    return None, None

def saveFile(jsonData):
    filePathSave = asksaveasfile(defaultextension="stps") 

    if filePathSave != None:
        filePathSave.close()
        with open(filePathSave.name, 'w') as file:
            json.dump(jsonData, file, indent=4)

