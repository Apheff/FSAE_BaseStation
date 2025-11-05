import serial as pyserial
import serial.tools.list_ports as ports
from PyQt6.QtCore import QThread, pyqtSignal
import serial
import time
import random #la importo per la "prova dell'hashmap"
    
class RadioWorker(QThread):
 



    data_received = pyqtSignal(int)

    def __init__(self, baudrate=9600):
        super().__init__()
        self.port = None
        self.baudrate = baudrate
        self.running = False
        self.serial = None

    def run(self):
        try:
            self.serial = serial.Serial(self.port, self.baudrate, timeout=0.1)
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
        input_message = Radio.clean_string(str(self.serial.readline()))
        
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
            
        except self.serial.SerialException as e:
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
    
    
#--------------------AGGIUNGO HASHMAP------------------#
    def __init__(self):
        super().__init__()
        self.dati = {

            "velocity":0.0,
            "gear":0,
            "brake":0.0,
            "throttle":0.0,
            "pression oil":0.0,
            "engine rpm":0.0,
            "oil temperature":0.0,
            "engine temperature":0.0,
            "pression wheel":0.0,
            "steering":0

            }

        def telemetry_information(dati, self):
            #simulazione
            self.dati["velocity"] = round(random.uniform(0,150),1)
            self.dati["gear"] = random.randint(0,6)
            self.dati["brake"] = round(random.uniform(0,1),2)
            self.dati["throttle"] = round(random.uniform(0,1),2)
            self.dati["pression oil"] = round(random.uniform(0,100),1)
            self.dati["engine rpm"] = random.randint(1000,12000)
            self.dati["oil temperature"] = round(random.uniform(60,110),1)
            self.dati["engine temperature"] = round(random.uniform(60,120),1)
            self.dati["pression wheel"] = round(random.uniform(0,100),1)
            self.dati["steering"] = random.randint(-100,100)
            return self.dati


        def show_telemetry(dati, self):
            print("======ENGINE DATES======")
            for chiave, valore in self.dati.items():
                print(f"{chiave.capitalize()}: {valore}")
            print("========================\n")

        while True:
            essential_inf = telemetry_information(self.dati)
            show_telemetry(self.dati)
            time.sleep(1)
            return dati 


#---------------FINE IMPLEMENTAZIONE----------------#


