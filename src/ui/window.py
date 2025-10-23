import sys
from PyQt6.QtWidgets import QApplication, QPushButton,  QWidget, QLabel, QPlainTextEdit
from PyQt6.QtGui import QIcon
import keyboard

class Window(QWidget):
    def __init__(self, width, height):
        super().__init__()
        self.setWindowTitle("FSAE Base Station")
        
        if sys.platform != "win32":
            self.setWindowIcon(QIcon('../assets/logo.png'))
        else:
            self.setWindowIcon(QIcon('..\\assets\\logo.png'))
            
        self.setFixedSize(width, height)
        
        # creation of the the text boxes
        self.inputText = QPlainTextEdit(self)
        self.inputText.setReadOnly(True)
        self.inputText.move(100, 100)
        self.inputText.setFixedSize(600, 300)
        
        self.cleanButton = QPushButton('Clear', self)
        self.cleanButton.move(100, 450)
        self.cleanButton.setFixedSize(600, 100)
        self.cleanButton.clicked.connect(self.clean_inputText)
        self.show()
    # creation of the window 

    def clean_inputText(self):
        self.inputText.clear()
    # function that clears the serial input textbox
    
    def update_inputText(self, text):
        self.inputText.appendPlainText(text)
    # fuction that updates the serial input textbox 
    
    
    
