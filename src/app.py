import sys
import utils.radio as Radio
import ui.MainWindow as Window
from PyQt6.QtWidgets import QApplication,  QWidget, QLabel, QLineEdit, QPushButton,  QVBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon

app = QApplication(sys.argv)
window = Window(800, 600)
sys.exit(app.exec())