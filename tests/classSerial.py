""" <TEST> CREATING A CLASS THAT INCORPORATES THE UART CONNECTION """

import serial

class InterfazOnTerminal:

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
    
    def close(self):
        self.serialDevice.close()

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
