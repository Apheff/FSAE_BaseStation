import sys
from PyQt6.QtWidgets import QLabel, QPushButton,  QWidget, QComboBox, QSlider
from PyQt6.QtGui import QIcon, QTextList
from PyQt6.QtCore import Qt
from utils.radio import RadioWorker

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("FSAE Base Station")
        
        if sys.platform != "win32":
            self.setWindowIcon(QIcon('../assets/logo.png'))
        else:
            self.setWindowIcon(QIcon('..\\assets\\logo.png'))
        
        # creation of the the text boxes
        self.inputText = QLabel(self)
        self.inputText.move(100, 100)
        self.inputText.setFixedSize(600, 300)
        self.inputText.setStyleSheet("""
            font-size: 72pt;
            color: white;
            font-weight: bold;
            qproperty-alignment: 'AlignCenter';
        """)
        
        self.slider = QSlider(self)
        self.slider.move(100, 450)
        self.slider.setFixedSize(600, 50)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.setOrientation(Qt.Orientation.Horizontal)
        self.setStyleSheet(f"""
            QSlider::groove:horizontal {{
                height: 8px;
                background: #333;
                border-radius: 4px;
            }}
            QSlider::sub-page:horizontal {{
                background: #555555;
                border-radius: 4px;
            }}
            QSlider::add-page:horizontal {{
                background: #222;
                border-radius: 4px;
            }}
            QSlider::handle:horizontal {{
                none;
            }}
        """)
    # creation of the window 

    def clean_inputText(self):
        self.slider.setValue(0)
        self.inputText.setText(f"0 km/h")
    # function that clears the serial input textbox
    
    def update_velocity(self, text):
        self.slider.setValue(int(text))
        self.inputText.setText(f"{text} km/h")
        self.updateColor(int(text))
    # fuction that updates the serial input textbox
    
    def updateColor(self, value):
            # Convert value (0-100) to color gradient from green to red
            r = int((value / 100) * 255)
            g = int(255 - (value / 100) * 255)
            color = f"rgb({r},{g},0)"  # changes from green -> yellow -> red
    
            self.setStyleSheet(f"""
                QSlider::groove:horizontal {{
                    height: 8px;
                    background: #333;
                    border-radius: 4px;
                }}
                QSlider::sub-page:horizontal {{
                    background: {color};
                    border-radius: 4px;
                }}
                QSlider::add-page:horizontal {{
                    background: #222;
                    border-radius: 4px;
                }}
                QSlider::handle:horizontal {{
                    none;
                }}
            """)
        
    
class SerialWindow(QWidget):
    def __init__(self, radio):
        super().__init__()
        
        self.setWindowTitle("Serial Configuration")
        
        self.radio = radio
        
        self.serialLabel = QLabel(self)
        self.serialLabel.setText("Select the COM port:")
        self.serialLabel.move(50, 20)
        
        self.postList = QComboBox(self)
        self.postList.move(50, 50)
        self.postList.setFixedSize(200, 50)
        self.postList.addItems(self.radio.list_available_ports())
        self.postList.setCurrentIndex(0)
        
        self.connectButton = QPushButton('Connect', self)
        self.connectButton.move(300, 50)
        self.connectButton.setFixedSize(200, 50)
    
        self.connectButton.clicked.connect(self.get_selected_port)
        
    
    def get_selected_port(self):
        self.radio.setCOM(self.postList.currentText().split(" : ")[0])
        
        print(self.postList.currentText().split(" : ")[0] + " selected")
        
        if(self.radio.init()):
            self.close() 
        else:
            print("Failed to open serial port")
        # function that gets the selected port from the dropdown menu