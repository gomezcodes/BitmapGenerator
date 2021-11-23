""" <TEST> CREATING A CLASS THAT INCORPORATES THE UART CONNECTION """

import serial
import platform

SYSTEMOS = platform.system()

if SYSTEMOS == "Windows":
	import serial.tools.list_ports_windows
else:
	import serial.tools.list_ports_linux



class serialInterface:

    commands = {
    "1" : b'\x5A\x08\x05\x80\x00\x00\x00\x00',
    "2" : b'\x5A\x08\x05\x80\x00\x00\x00\x01',
    "3" : b'\x5A\x08\x05\x80\x00\x00\x00\x02',
    "4" : b'\x5A\x08\x05\x80\x00\x00\x00\x03',
    }

    def __init__(self,serialPort,baudrate) -> None:
        self.serialPort = serialPort
        self.baudRate = baudrate
        self.serialDevice = serial.Serial(self.serialPort,self.baudRate)

    def write(self,dataToSend):
        try:
            self.serialDevice.write(dataToSend)
            return True
        except:
            return False

    def read(self,expectedBytes):
        try:
            self.__receivedBytes = self.serialDevice.read(expectedBytes)
            return self.__receivedBytes
        except:
            return False

    def close(self):
        self.serialDevice.close()

def scanPorts():
    
    availablePorts = []

    if SYSTEMOS == "Windows":
        ports = serial.tools.list_ports_windows.comports()
    else:
	    ports = serial.tools.list_ports_linux.comports()

    if len(ports) != 0:

        for port in ports:
            portAttributes= [port.device,port.description]
            availablePorts.append(portAttributes)

        return availablePorts
    
    return None
