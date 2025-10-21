import sys
from utils.radio import Radio
from ui.window import Window
from PyQt6.QtWidgets import QApplication,  QWidget, QLabel, QLineEdit, QPushButton,  QVBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
import serial.tools.list_ports as ports



app = QApplication(sys.argv)
for _ in ports.comports():
    if ("n/a" not in _.description.lower()):
        print(_)
window = Window(800, 600)
radio = Radio("/dev/ttyACM0", 9600)

while True:
    radio.receive_message
sys.exit(app.exec())