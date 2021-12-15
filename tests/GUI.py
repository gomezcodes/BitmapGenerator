""" from tkinter import *

def button_hover(event):
	my_button["activeback"]="Azure"
	status_label.config(text="I'm hovering over the button ")
	my_button.flash()

def button_hover_leave(event):
	my_button["bg"]="silver"
	status_label.config(text="")


root = Tk()
root.title("Testing functions")
root.geometry("1000x700")
root.configure(bg="#141414")

my_button = Button(root, text="Click me", font=("helvetica",28))
my_button.pack(pady=10)

status_label=Label(root,text="",bd=1,relief=SUNKEN, anchor=E)
status_label.pack(fill = X, side=BOTTOM, ipady=2)

my_button.bind("<Enter>",button_hover)
my_button.bind("<Leave>",button_hover_leave)


root.mainloop() """

""" from tkinter import *
from tkinter import ttk
root = Tk()

h = ttk.Scrollbar(root, orient=HORIZONTAL)
v = ttk.Scrollbar(root, orient=VERTICAL)
canvas = Canvas(root, scrollregion=(0, 0, 1000, 1000), yscrollcommand=v.set, xscrollcommand=h.set)
h['command'] = canvas.xview
v['command'] = canvas.yview

canvas.grid(column=0, row=0, sticky=(N,W,E,S))
h.grid(column=0, row=1, sticky=(W,E))
v.grid(column=1, row=0, sticky=(N,S))
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

lastx, lasty = 0, 0

def xy(event):
	global lastx, lasty
	print(f"event: {event}")
	lastx, lasty = canvas.canvasx(event.x), canvas.canvasy(event.y)
	print(f"[{lastx,lasty}]")

def setColor(newcolor):
    global color
    color = newcolor
    canvas.dtag('all', 'paletteSelected')
    canvas.itemconfigure('palette', outline='white')
    canvas.addtag('paletteSelected', 'withtag', 'palette%s' % color)
    canvas.itemconfigure('paletteSelected', outline='#999999')

def addLine(event):
	global lastx, lasty
	x, y = canvas.canvasx(event.x), canvas.canvasy(event.y)
	print(x,y)
	canvas.create_line((lastx, lasty, x, y), fill=color, width=5, tags='currentline')
	lastx, lasty = x, y

def doneStroke(event):
    canvas.itemconfigure('currentline', width=1)        
        
canvas.bind("<Button-1>", xy)
canvas.bind("<B1-Motion>", addLine)
canvas.bind("<B1-ButtonRelease>", doneStroke)

id = canvas.create_rectangle((10, 10, 30, 30), fill="red", tags=('palette', 'palettered'))
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("red"))
id = canvas.create_rectangle((10, 35, 30, 55), fill="blue", tags=('palette', 'paletteblue'))
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("blue"))
id = canvas.create_rectangle((10, 60, 30, 80), fill="black", tags=('palette', 'paletteblack', 'paletteSelected'))
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("black"))

setColor('black')
canvas.itemconfigure('palette', width=5)
root.mainloop() """

""" import tkinter as tk
from tkinter import ttk


def return_pressed(event):
    print('Return key pressed.')


def log(event):
    print(event)


root = tk.Tk()

btn = ttk.Button(root, text='Save')
btn.bind('<Return>', return_pressed)
btn.bind('<Return>', log, add='+')


btn.focus()
btn.pack(expand=True)

root.mainloop() """

import tkinter as tk
from tkinter import ttk
import re


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Tkinter Validation Demo')

        self.create_widgets()

    def create_widgets(self):
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)
        self.columnconfigure(2, weight=1)

        # label
        ttk.Label(text='Email:').grid(row=0, column=0, padx=5, pady=5)

        # email entry
        vcmd = (self.register(self.validate), '%P')
        ivcmd = (self.register(self.on_invalid),)

        self.email_entry = ttk.Entry(self, width=50)
        self.email_entry.config(validate='focusout', validatecommand=vcmd, invalidcommand=ivcmd)
        self.email_entry.grid(row=0, column=1, columnspan=2, padx=5)

        self.label_error = ttk.Label(self, foreground='red')
        self.label_error.grid(row=1, column=1, sticky=tk.W, padx=5)

        # button
        self.send_button = ttk.Button(text='Send').grid(row=0, column=4, padx=5)

    def show_message(self, error='', color='black'):
        self.label_error['text'] = error
        self.email_entry['foreground'] = color

    def validate(self, value):
        """
        Validat the email entry
        :param value:
        :return:
        """
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.fullmatch(pattern, value) is None:
            return False

        self.show_message()
        return True

    def on_invalid(self):
        """
        Show the error message if the data is not valid
        :return:
        """
        self.show_message('Please enter a valid email', 'red')


if __name__ == '__main__':
    app = App()
    app.mainloop()