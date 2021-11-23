from tkinter import *

root = Tk()
root.geometry("1000x800")
frame=Frame(root)
frame.pack()

listaBotones=[]
imagenBomba=PhotoImage(file="circulo1.png")

def generarBotones():
	global listaBotones
	for c in range(81):
		listaBotones.append(Button(frame,image=imagenBomba,command=lambda c=c:print(c), bg="grey"))
		if c >= 0 and c < 32:
			listaBotones[c].grid(column=1, row=c+1)
		if c >= 32 and c < 64:
			listaBotones[c].grid(column=2, row=c-31)
		if c >= 64 and c < 96:
			listaBotones[c].grid(column=3, row=c-63)
		if c >= 96 and c < 128:
			listaBotones[c].grid(column=4, row=c-96)
		if c >= 128 and c < 160:
			listaBotones[c].grid(column=5, row=c-127)
		if c >= 160 and c < 192:
			listaBotones[c].grid(column=6, row=c-159)
		if c >= 192 and c < 224:
			listaBotones[c].grid(column=7, row=c-191)
		if c >= 224 and c < 256:
			listaBotones[c].grid(column=8, row=c-223)
		if c >= 256 and c < 288:
			listaBotones[c].grid(column=9, row=c-255)
generarBotones()


chec= Checkbutton(root)
chec.pack()

root.mainloop()