import serial as pyserial
import serial.tools.list_ports as ports

class Radio:
    def __init__(self):
        self.serial = None
    # serial connection initialization
    
    
    def receive_message(self):
        ''' Receives the data from the serial port '''
        return Radio.clean_string(str(self.serial.readline()))
    
    
    def wait_for_message(self, message):
        ''' Aspetta un determinato messaggio da Arduino '''
        input_message = ""
    
        while message not in input_message:
            input_message = str(self.serial.readline())
        
        return input_message
    
    
    def list_available_ports():
        ''' Lists all the available serial ports '''
        s = []
        for _ in ports.comports():
            if ("n/a" not in _.description.lower()):
                s += _
        return s
        

    def init(self, COM, BAUDRATE = 9600):
        ''' Initializes the serial connection '''
        self.serial = pyserial.Serial(COM, BAUDRATE)
        return self.serial.is_open


    def clean_string(msg):
        # TO-DO: implement the function to clean the receiving string from the radio
        out = msg[2:][:-5]
        return out
