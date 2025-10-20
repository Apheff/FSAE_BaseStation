import sys
from PyQt6.QtWidgets import QApplication,  QWidget, QLabel, QPushButton, QPlainTextEdit
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
import utils.radio as Radio

class MainWindow(QWidget):
    def __init__(self, width, height):
        super().__init__()
        self.setWindowTitle("FSAE Base Station")
        
        if sys.platform != "win32":
            self.setWindowIcon(QIcon('../assets/logo.png'))
        else:
            self.setWindowIcon(QIcon('..\\assets\\logo.png'))
            
        self.setFixedSize(width, height)
        self.textbox = QPlainTextEdit(self)
        self.textbox.setReadOnly(True)
        self.textbox.setFixedSize(600, 400)
        self.textbox.addPlaintext(Radio.)
        self.textbox.move(100, 100)
        self.show()
    # creation of the window
    
    def on_click(self):
        self.label = QLabel('Bravo!', self)
        self.label.move(350, 300)
        self.label.show()
    # butto click event 
        
        
app = QApplication(sys.argv)
window = MainWindow(800, 600)
sys.exit(app.exec())