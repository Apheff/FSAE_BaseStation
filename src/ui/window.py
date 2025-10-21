import sys
from PyQt6.QtWidgets import QApplication,  QWidget, QLabel, QPlainTextEdit
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
        self.inputText = QPlainTextEdit(self)
        self.inputText.setReadOnly(True)
        self.inputText.setFixedSize(600, 300)
        self.inputText.move(100, 100)
        self.outputText = QPlainTextEdit(self)
        self.outputText.move(100, 450)
        self.outputText.setFixedSize(600, 100)
        self.show()
    # creation of the window 

    def update_inputText(self, text):
        self.inputText.appendPlainText(text)
    # fuction that updates the serial input textbox 
    
    def update_outputText(self):
        if(keyboard.is_pressed('enter')):
            text = self.outputText.toPlainText()
            self.outputText.clear()
            return text
    
    
    
