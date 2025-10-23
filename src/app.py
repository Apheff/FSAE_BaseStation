import sys
from utils.radio import Radio
from ui.window import Window
from PyQt6.QtWidgets import QApplication,  QWidget, QLabel, QLineEdit, QPushButton,  QVBoxLayout
from PyQt6.QtCore import Qt, QThread
from PyQt6.QtGui import QIcon


class MainThread(QThread):
    def __init__(self):
        QThread.__init__(self)
        self.window = Window(800, 600)
        self.radio = Radio()
        self.radio.init("/dev/ttyACM0")
        self.start()
    # thread initialization
    
    def run(self):
        while True:
            self.window.update_inputText(str(self.radio.receive_message()))
    # main loop of the thread
    
    
    def kill(self):
        sys.exit(self.exec())
    # function to kill the thread

# application start
app = QApplication(sys.argv)
main = MainThread()
sys.exit(app.exec())