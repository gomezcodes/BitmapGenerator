# from TLControlCenter import *

# GUI = AppTrafficLight()

# while True:
# 	try:
# 		GUI.root.update_idletasks() 
# 		GUI.root.update()
# 	except

import tkinter as tk
from tkinter import ttk
from urllib.request import urlopen
def download_file():
    info_label["text"] = "Descargando archivo..."
    # Deshabilitar el botón mientras se descarga el archivo.
    download_button["state"] = "disabled"
    url = "https://www.python.org/ftp/python/3.7.2/python-3.7.2.exe"
    filename = "python-3.7.2.exe"
    # Abrir la dirección de URL.
    with urlopen(url) as r:
        with open(filename, "wb") as f:
            # Leer el archivo remoto y escribir el fichero local.
            f.write(r.read())
    info_label["text"] = "¡El archivo se ha descargado!"
    # Restablecer el botón.
    download_button["state"] = "normal"
root = tk.Tk()
root.title("Descargar archivo con Tcl/Tk")
info_label = ttk.Label(text="Presione el botón para descargar el archivo.")
info_label.pack()
download_button = ttk.Button(text="Descargar archivo", command=download_file)
download_button.pack()
root.mainloop()