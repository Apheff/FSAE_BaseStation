import sys
from PyQt6.QtWidgets import QApplication
from ui.window import Window, SerialWindow
from utils.radio import RadioWorker

app = QApplication(sys.argv)

# GUI
mainWindow = Window()
mainWindow.show()

# Thread radio
radio = RadioWorker()
serialWindow = SerialWindow(radio)
serialWindow.show()
radio.data_received.connect(mainWindow.update_velocity)
radio.start()

sys.exit(app.exec())