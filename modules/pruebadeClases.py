from tkinter import *
from classFileChooser import *

jdata = {}

jdata['clients'] = []

jdata['clients'].append({
    'first_name': 'Sigrid',
    'last_name': 'Mannock',
    'age': 27,
    'amount': 7.17})

jdata['clients'].append({
    'first_name': 'Joaquin',
    'last_name': 'Hinners',
    'age': 21,
    'amount': [1.90, 5.50]})

def button_hover(event):
	my_button["activeback"]="Azure"
	status_label.config(text="I'm hovering over the button ")
	my_button.flash()

def button_hover_leave(event):
	my_button["bg"]="silver"
	status_label.config(text="")

def save():
    saveFile(jdata)


def load():
    path,data = openFile()

    print(path,data)    


root = Tk()
root.title("Testing functions")
root.geometry("1000x700")
root.configure(bg="#141414")

my_button = Button(root, text="Click me", font=("helvetica",28),command=load)
my_button.pack(pady=10)

my_button1 = Button(root, text="save", font=("helvetica",28),command=save)
my_button1.pack(pady=10)

status_label=Label(root,text="",bd=1,relief=SUNKEN, anchor=E)
status_label.pack(fill = X, side=BOTTOM, ipady=2)

my_button.bind("<Enter>",button_hover)
my_button.bind("<Leave>",button_hover_leave)


root.mainloop()
