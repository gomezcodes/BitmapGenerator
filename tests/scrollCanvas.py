from tkinter import *

def on_mousewheel(event):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    print(event.delta)

root=Tk()
frame=Frame(root,width=300,height=300)
frame.pack(expand=True, fill=BOTH) #.grid(row=0,column=0)

canvas=Canvas(frame,bg='#FFFFFF',width=300,height=300,scrollregion=(0,0,1000,1000))

hbar=Scrollbar(frame,orient=HORIZONTAL)
hbar.pack(side=BOTTOM,fill=X)
hbar.config(command=canvas.xview)

vbar=Scrollbar(frame,orient=VERTICAL)
vbar.pack(side=RIGHT,fill=Y)
vbar.config(command=canvas.yview)

canvas.config(width=300,height=300)
canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
canvas.pack(side=LEFT,expand=True,fill=BOTH)

canvas.bind("<MouseWheel>", on_mousewheel)

canvas.create_rectangle(50,50,110,100)

root.mainloop() 

""" # explore the mouse wheel with the Tkinter GUI toolkit
# Windows and Linux generate different events
# tested with Python25
import tkinter as tk
def mouse_wheel(event):
    global count
    # respond to Linux or Windows wheel event
    print(event.num)
    if event.num == 5 or event.delta == -120:
        count -= 1
    if event.num == 4 or event.delta == 120:
        count += 1
    label['text'] = count
count = 0
root = tk.Tk()
root.title('turn mouse wheel')
root['bg'] = 'darkgreen'
# with Windows OS
root.bind("<MouseWheel>", mouse_wheel)
# with Linux OS
root.bind("<Button-4>", mouse_wheel)
root.bind("<Button-5>", mouse_wheel)
label = tk.Label(root, font=('courier', 18, 'bold'), width=10)
label.pack(padx=40, pady=40)
root.mainloop() """