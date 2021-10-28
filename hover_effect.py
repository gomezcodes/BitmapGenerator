from tkinter import *

w=Tk()
w.geometry("300x500")
w.configure(bg="#141414")

def bttn(x,y,text,bcolor,fcolor):

	def on_enter(e):
		mybutton["background"]=bcolor
		mybutton["foreground"]=fcolor

	def on_leave(e):
		mybutton["background"]=fcolor
		mybutton["foreground"]=bcolor


	mybutton = Button(w,width=250,height=2,text=text,
					  fg=bcolor,
					  bg=fcolor,
					  bd=0,
					  border=0,
					  borderwidth=0,
					  overrelief="flat",
					  highlightthickness=0,
					  activeforeground=fcolor,
					  activebackground=bcolor,)

	mybutton.bind("<Enter>", on_enter)
	mybutton.bind("<Leave>", on_leave)

	mybutton.pack()

bttn(0,0,"J O A Q U I N","#FFCC66","#141414")
bttn(0,37,"P O S M O","#25DAE9","#141414")
bttn(0,74,"G I S E L I T A","#F86263","#141414")
bttn(0,110,"O L I V E R","#FFA157","#141414")




w.mainloop()