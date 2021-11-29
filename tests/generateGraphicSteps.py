from tkinter import *

def on_mousewheel(event):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units") #event.num  para linux
    print(event.delta)

secuencues = {
    "STEP 1" : ["BITMAP1", False, 10],
    "STEP 2" : ["BITMAP1", True, 8],
    "STEP 3" : ["BITMAP1", True, 8],
    "STEP 4" : ["BITMAP1", True, 8],
    "STEP 5" : ["BITMAP1", True, 8],
}

graphicSteps = []

def generateGraphics():
    yAxisStart = 50
    yAxisEnd = 150
    yAxisText = 90
    numberOfSteps = len(secuencues)

    for stepID in range(numberOfSteps):
        step = canvas.create_rectangle(50,yAxisStart,150,yAxisEnd,fill="lightblue",
                                        activefill="dark slate gray")
        canvas.create_text(250,yAxisText,fill="darkblue",font="Roboto 12 italic bold",text=list(secuencues.keys())[stepID], activefill="dark slate gray")
        graphicSteps.append(step)
        yAxisStart += 150
        yAxisEnd += 150
        yAxisText  += 150
    
    yAxisStart = 150
    yAxisEnd = 200
    
    for _ in range(numberOfSteps-1):
        step = canvas.create_line(100,yAxisStart,100,yAxisEnd,arrow=LAST,width = 3, fill="red")
        yAxisStart += 150
        yAxisEnd += 150

    returnLine = numberOfSteps*150
    canvas.create_line(100,returnLine,100,returnLine+50,200,returnLine+50,200,100,150,100,arrow=LAST,width = 3, fill="red")
    
    canvas.config(scrollregion=(0,0,1000,1000))
    """ hbar.pack(side=BOTTOM,fill=X) """
    vbar.pack(side=RIGHT,fill=Y)

    


root = Tk()
root.title("Generate Graphic Steps")
root.config(bg="#19266d")
root.geometry("700x700") 

frame=Frame(root,width=300,height=300)
frame.pack(padx = 10, pady = 10,side=LEFT)

canvas = Canvas(frame, width=400, height=700, bg="#007acc")
canvas.pack(padx = 3, pady = 3,side=LEFT)

""" hbar=Scrollbar(frame,orient=HORIZONTAL)
hbar.config(command=canvas.xview) """

vbar=Scrollbar(frame,orient=VERTICAL)
vbar.config(command=canvas.yview)

canvas.config(yscrollcommand=vbar.set)

canvas.bind("<MouseWheel>", on_mousewheel)

Button(root,text="LOAD",command=generateGraphics).pack(side=RIGHT)


root.mainloop()