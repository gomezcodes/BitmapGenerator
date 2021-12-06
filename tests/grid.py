from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("1300x800")
root.minsize(867,730)

frame1 = Frame(root,background="red")
frame2 = Frame(root,background="blue")

frame1.pack(side=LEFT,fill=BOTH,expand=1)
frame2.pack(side=LEFT,fill=BOTH,expand=1)

canvas = Canvas(frame1, width=400, height=700, bg="#007acc")
canvas.pack(padx = 0, pady = 0,expand=1)

trafficIdSel= ttk.Combobox(frame2)
trafficIdSel["values"] = ("Semaforo 1","Semaforo 2","Semaforo 3","Semaforo 4","Semaforo 5")

#Button(frame1,text="Algo").pack(fill=BOTH,expand=1)
Label(frame2,text="This is a ComboBox",font="Helvetica 15").pack()
trafficIdSel.pack(side=TOP,fill=BOTH,padx=10,pady=10,expand=0)

Label(frame2,text="This is a CheckButton",font="Helvetica 15").pack()
Checkbutton(frame2,text="HOLA",width=20,height=1).pack(side=TOP,fill=BOTH,padx=10,pady=10,expand=1)

Label(frame2,text="These are Buttons",font="Helvetica 15").pack()

#butfr=Frame(frame2,background="purple")
#butfr.pack(side=BOTTOM,fill=BOTH,expand=1) 

Button(frame2,text="Cargar",width=20,height=5).pack(side=BOTTOM,fill=BOTH,padx=10,pady=10,expand=1) #master:butfr
Button(frame2,text="Salvar",width=20,height=5).pack(side=BOTTOM,fill=BOTH,padx=10,pady=10,expand=1) #master:butfr
Button(frame2,text="Abrir",width=20,height=5).pack(side=BOTTOM,fill=BOTH,padx=10,pady=10,expand=1)
Button(frame2,text="Comenzar secuencia",width=20,height=5).pack(side=BOTTOM,fill=BOTH,padx=10,pady=10,expand=1)



root.mainloop()