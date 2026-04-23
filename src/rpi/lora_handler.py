# import serial
import time
from periphery import Serial
from data_elements import CDataElements
import threading


# serial bus (uart2): /dev/ttyS2
class CLoraHandler:

    def __init__(self, data):
        self.bus = Serial("/dev/ttyS2", baudrate=9600, parity="none", stopbits=1, databits=8)
        self.data = data

    def send_data(self):
        """lora send data

        Returns:
            TypeError: when invalid datatype tried to send
            ValueError: when invalid data in bytes
        """
        try:
            length = self.bus.write([self.data])
            # return length

        except TypeError:
            return "datatype is inavlid"

        except ValueError:
            return "data invalid in bytes"

    def receive_data(self):
        """lora receive data

        Returns:
            data: received data
            Error: if error during reading data (uart lora)
        """
        try:
            data = self.bus.read(2)
            self.data = CDataElements(data[1], data[2])
            return data

        except Exception:
            return "bad request, no data recevied to to any error"


if __name__ == '__main__':
    # pass
    x = CLoraHandler(0x50)
    while True:
        data = x.receive_data()
        print(data[0])
        # dist = bytes(data)
        # print(dist)
        # time.sleep(0.01)