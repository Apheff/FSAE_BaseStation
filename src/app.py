import sys

from PyQt6.QtWidgets import QApplication

import ui.server
from ui.serial_window import SerialWindow
from ui.main_window import MainWindow
from utils.radio import RadioWorker

app = QApplication(sys.argv)
screen = app.primaryScreen()

# Get screen size with error handling
if not screen:
    print("Error: No primary screen detected.")
    sys.exit(1)

size = screen.size()
width = size.width()
height = size.height()

# GUI
mainWindow = MainWindow()
mainWindow.showFullScreen()
mainWindow.show()

# Thread server
server_thread = ui.server.ServerThread()
server_thread.start()

# Thread radio
radio = RadioWorker()
serialWindow = SerialWindow(radio)
serialWindow.show()

radio.data_received.connect(mainWindow.update_card)


# Start the application
sys.exit(app.exec())
