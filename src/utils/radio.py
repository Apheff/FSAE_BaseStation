import time

import serial as pyserial
import serial.tools.list_ports as ports
from PyQt6.QtCore import QThread, pyqtSignal
from serial import SerialException


class RadioWorker(QThread):
    data_received = pyqtSignal(str, str)

    def __init__(self, baudrate=115200):
        """initialization of the RadioWorker thread"""
        super().__init__()
        self.port = None
        self.baudrate = baudrate
        self.running = False
        self.serial = None

        # Dictionary to store telemetry data (and pass it to the main window set function via signal)
        self.info = {
            "ST": "",
            "TP": "",
            "BS": "",
            "M": "",
            "CS": "",
            "OT": "",
            "WT": "",
            "RPM": "",
            "OP": "",
            "SS": "",
        }
        self.start()
        # end of __init__ function

    def run(self):
        """Main thread loop to read data from the serial port"""
        try:
            self.serial = pyserial.Serial(self.port, self.baudrate, timeout=0.1)
        except Exception as e:
            print(f"Serial error: {e}")
            return

        while self.running:
            try:
                if self.serial:
                    msg = self.serial.readline().decode("utf-8").strip()

                    # Parsing the message (the format here is <key1>:<value1>,<key2>:<value2>,...)
                    for part in msg.split(","):
                        # splitting key and value
                        if ":" in part:
                            key, value = part.split(":", 1)

                            # updating the info dictionary
                            self.info[key] = value

                    for key, value in self.info.items():
                        self.data_received.emit(key, value)
                time.sleep(0.05)  # Small delay to prevent CPU overload
            except Exception as e:
                print(f"/!\\ Error in RadioWorker: {e}")
                break

    # end of run function

    def wait_for_message(self, message):
        """waiting for a specific massage sent by the radio module"""
        if not self.serial:
            return

        input_message = ""

        while message not in input_message:
            input_message = str(self.serial.readline())

        return input_message

    # end of wait_for_message function

    def list_available_ports(self):
        """Lists all the available serial ports"""
        s = []
        for _ in ports.comports():
            if "n/a" not in _.description.lower():
                s.append(f"{_.device} : {_.description}")
        return s

    # end of list_available_ports function

    def init(self):
        """Connect with comprehensive error handling"""
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

    # end of init function

    """
    --------------------------------
    |                              |
    |      Get and Set Methods     |
    |                              |
    --------------------------------
    """

    def isActive(self):
        """Checks if the serial connection is active"""
        return self.serial

    def setBaudrate(self, baudrate):
        """Sets the baudrate for the serial connection"""
        self.baudrate = baudrate

    def getBaudrate(self):
        """Gets the baudrate for the serial connection"""
        return self.baudrate

    def setCOM(self, port):
        """Sets the COM port for the serial connection"""
        self.port = port

    def getCOM(self):
        """Gets the COM port for the serial connection"""
        return self.port
