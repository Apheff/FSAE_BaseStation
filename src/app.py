import sys
from utils.radio import Radio
from ui.window import Window, SerialWindow
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QThread


class MainThread(QThread):
    def __init__(self):
        QThread.__init__(self)
        self.serialWindow = SerialWindow()
        Radio.setBaudrate(9600)
        self.mainWindow = Window()
        self.serialWindow.show()
        self.start()
    # thread initialization
    
    def run(self):
        while True:
            self.mainWindow.show()
            if(Radio.isActive()):
                self.mainWindow.update_inputText(Radio.receive_message())
    # main loop of the thread
    
    
    def kill(self):
        sys.exit(self.exec())
    # function to kill the thread

# application start
app = QApplication(sys.argv)
main = MainThread()
sys.exit(app.exec())