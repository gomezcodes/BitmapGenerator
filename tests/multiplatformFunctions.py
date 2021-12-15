import platform
import serial.tools.list_ports_windows
import serial.tools.list_ports_linux

SYSTEMOS = platform.system()

def serial_list_ports():

    if SYSTEMOS == "Windows":
        return serial.tools.list_ports_windows.comports()
    else:
        return serial.tools.list_ports_linux.comports()





