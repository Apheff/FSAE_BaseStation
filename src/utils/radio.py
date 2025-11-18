import serial as pyserial
import serial.tools.list_ports as ports
from PyQt6.QtCore import QThread, pyqtSignal
import time
from serial import SerialException
    
class RadioWorker(QThread):

    data_received = pyqtSignal(int)

    def __init__(self, baudrate=9600):
        super().__init__()
        self.port = None
        self.baudrate = baudrate
        self.running = False
        self.serial = None
        self.queue = []

    def run(self):
        try:
            self.serial = pyserial.Serial(self.port, self.baudrate, timeout=0.1)
        except Exception as e:
            print(f"Serial error: {e}")
            return

        while self.running:
            try:
                if self.serial.in_waiting:
                    msg = self.serial.readline().decode(errors="ignore").strip()
                    if msg.isdigit():
                        self.data_received.emit(int(msg))
                time.sleep(0.05)  # Small delay to prevent CPU overload
            except Exception as e:
                print(f"Error in RadioWorker: {e}")
                break
                
    
    def start(self):
        self.running = True
        super().start()

    def stop(self):
        self.running = False
        self.wait()

    def receive_message(self):
        ''' Receives the data from the serial port '''
        input_message = self.serial.readline()
        
        if input_message != "":
            self.queue.append(input_message)
            
    def read_message(self):
        ''' Reads the oldest message from the queue '''
        if len(self.queue) > 0:
            return self.queue.pop(0)
        else:
            return None
            
    def canRead(self):
        ''' Checks if there are messages in the queue '''
        return len(self.queue) > 0
    
    
    def wait_for_message(self, message):
        ''' Aspetta un determinato messaggio da Arduino '''
        input_message = ""
    
        while message not in input_message:
            input_message = str(self.serial.readline())
        
        return input_message

    
    def list_available_ports(self):
        ''' Lists all the available serial ports '''
        s = []
        for _ in ports.comports():
            if ("n/a" not in _.description.lower()):
                s.append(f"{_.device} : {_.description}")
        return s

    def init(self):
        ''' Connect with comprehensive error handling '''
        try:
            self.serial = pyserial.Serial(self.port, self.baudrate, timeout=10)
            self.start()
            return self.serial
            
        except SerialException as e:
            print(f"Serial port error: {e}")
        except PermissionError:
            print("Permission denied. Fix:")
            print("  Linux: sudo usermod -a -G dialout $USER")
            print("  Windows: Run as administrator")
        except FileNotFoundError:
            print("Port not found. Check:")
            print("  - Device connected and powered")
            print("  - Correct port name")
            print("  - Driver installed")
        
        return False

    def isActive(self):
        ''' Checks if the serial connection is active '''
        return self.serial

    def setBaudrate(self, baudrate):
        ''' Sets the baudrate for the serial connection '''
        self.baudrate = baudrate
    
    def getBaudrate(self):
        ''' Gets the baudrate for the serial connection '''
        return self.baudrate

    def setCOM(self, port):
        ''' Sets the COM port for the serial connection '''
        self.port = port
    
    def getCOM(self):
        ''' Gets the COM port for the serial connection '''
        return self.port
    
    @staticmethod
    def clean_string(msg):
        ''' Restituisce solo la parte utile di una stringaricevuta tramite connessione seriale '''
        out = msg[2:][:-5]
        return out
