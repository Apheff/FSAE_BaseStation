import sys
from PyQt6.QtWidgets import QApplication, QLabel, QPushButton,  QWidget, QPlainTextEdit, QComboBox
from PyQt6.QtGui import QIcon, QTextList
from utils.radio import Radio

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("FSAE Base Station")
        
        if sys.platform != "win32":
            self.setWindowIcon(QIcon('../assets/logo.png'))
        else:
            self.setWindowIcon(QIcon('..\\assets\\logo.png'))
        
        # creation of the the text boxes
        self.inputText = QPlainTextEdit(self)
        self.inputText.setReadOnly(True)
        self.inputText.move(100, 100)
        self.inputText.setFixedSize(600, 300)
        
        self.cleanButton = QPushButton('Clear', self)
        self.cleanButton.move(100, 450)
        self.cleanButton.setFixedSize(600, 100)
        self.cleanButton.clicked.connect(self.clean_inputText)
    # creation of the window 

    def clean_inputText(self):
        self.inputText.clear()
    # function that clears the serial input textbox
    
    def update_inputText(self, text):
        self.inputText.appendPlainText(text)
    # fuction that updates the serial input textbox 
        
    
class SerialWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Serial Configuration")
        
        self.serialLabel = QLabel(self)
        self.serialLabel.setText("Select the COM port:")
        self.serialLabel.move(50, 20)
        
        self.postList = QComboBox(self)
        self.postList.move(50, 50)
        self.postList.setFixedSize(200, 50)
        self.postList.addItems(Radio.list_available_ports())
        self.postList.setCurrentIndex(0)
        
        self.connectButton = QPushButton('Connect', self)
        self.connectButton.move(300, 50)
        self.connectButton.setFixedSize(200, 50)
    
        self.connectButton.clicked.connect(self.get_selected_port)
        
    def get_selected_port(self):
        Radio.setCOM(self.postList.currentText().split(" : ")[0])
        print(self.postList.currentText().split(" : ")[0] + " selected")
        if(Radio.init()):
            self.hide()
        else:
            print("Failed to open serial port")
    # function that gets the selected port from the dropdown menu