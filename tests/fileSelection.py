from tkinter import *
from tkinter import messagebox

from tkinter.filedialog import askopenfilename, asksaveasfile
from io import open

def openFile():
    filename = askopenfilename(defaultextension="stps") # show an "Open" dialog box and return the path to the selected file
    print(filename)


    if len(filename) != 0:
        try:
            archivo_texto = open(filename,"r")
            displaydata.config(text=archivo_texto.readlines())
            archivo_texto.seek(0)
            print(list(archivo_texto.readlines()[0]))
            archivo_texto.close()
        except FileNotFoundError:
            messagebox.showerror(message="Unable to open selected file", title="Error")

def saveFile():
    filename = asksaveasfile(defaultextension="stps") 
    filename.close()
    print(filename.name)
    filename.seek(0)
    filename.writelines(str(secuence))
    filename.close()
    Label(root,text=filename).pack()

secuence = [
    ["BITMAP1", False, 10],
    ["BITMAP1", True, 8],
    ["BITMAP2", False, 5],
]


root = Tk()
root.geometry("400x400")

data = StringVar()

Button(root,text="Open File",command=openFile).pack()
Button(root,text="Save File",command=saveFile).pack()

Entry(root,textvariable=data).pack()
displaydata = Label(root,text="")
displaydata.pack()

root.mainloop()

#Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing


