import serial as pyserial

class Radio:
    def __init__(self, COM, BAUDRATE = 9600):
        self.serial = pyserial.Serial(COM, BAUDRATE)
    # serial connection initialization
    
    def receive_message(self):
        ''' Receives the data from the serial port '''
        return print(self.serial.readline())
    
    def wait_for_message(self, message):
        ''' Aspetta un determinato messaggio da Arduino '''
        input_message = ""
    
        while message not in input_message:
            input_message = str(self.serial.readline())
        
        return input_message
    
    
    def clean_string(msg):
        # TO-DO: implement the function to clean the receiving string from the radio
        return msg
