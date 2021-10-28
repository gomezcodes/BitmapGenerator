from tkinter import *

def button_hover(event):
	my_button["activeback"]="Azure"
	status_label.config(text="I'm hovering over the button ")

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


root.mainloop()