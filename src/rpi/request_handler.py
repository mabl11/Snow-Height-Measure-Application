from lora_handler import CLoraHandler
from timer import CTimer


class CRequestHandler:

    def __init__(self):
        self.Lora = CLoraHandler(0x50)
        self.timer = None

    def get_timed_snow_depth(self, time_cycle=0):
        """receives the snow depth data

        Args:
            time_cycle: int only, repetition interval in seconds, default = 0

        Returns:
            data: snow depth from sensor (float)
        """
        self.Lora.data = 0x01
        if self.timer is not None:
            self.timer.stop()
        self.timer = CTimer(int(time_cycle), self.Lora.send_data)
        self.timer.start()

        data = self.__receive_data()
        return data

    def new_reference(self):
        """create a new reference 

        Returns:
            data: new reference (float)
        """
        if self.timer is not None:
            self.timer.stop()

        self.Lora.data = 0x10
        self.Lora.send_data()
        data = self.__receive_data()
        return data
    
    def get_reference(self):
        """get the current reference

        Returns:
            ref: reference data (float)
        """
        if self.timer is not None:
            self.timer.stop()
        
        self.Lora.data = 0x11
        self.Lora.send_data()
        ref = self.__receive_data()
        return ref

    def delete_reference(self):
        """delete the current reference (set to 0)

        Returns:
            old_ref: data of old_ref which no longer exists
        """
        if self.timer is not None:
            self.timer.stop()

        self.Lora.data = 0x12
        self.Lora.send_data()
        old_ref = self.__receive_data()
        return old_ref

    def __receive_data(self):
        """receive data from lora handler

        Returns:
            data: received data from lora handler
        """
        data = self.Lora.receive_data()
        return data

         
if __name__ == '__main__':
    pass