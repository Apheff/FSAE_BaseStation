from PyQt6.QtWidgets import QSpinBox, QWidget, QLabel, QComboBox, QPushButton

class SerialWindow(QWidget):
    def __init__(self, radio):
        ''' Window to configure the serial port and baudrate '''
        super().__init__()
        
        self.setWindowTitle("Serial Configuration")
        self.radio = radio
        
        # Widgets creation
        self.serialLabel = QLabel(self)
        self.serialLabel.setText("Select the COM port:")
        self.serialLabel.move(50, 20)
        
        
        # Dropdown menu with the available serial ports
        self.postList = QComboBox(self)
        self.postList.move(50, 50)
        self.postList.setFixedSize(200, 50)
        self.postList.addItems(self.radio.list_available_ports())
        self.postList.setCurrentIndex(0)
        
        # button to connect to the selected port
        self.connectButton = QPushButton('Connect', self)
        self.connectButton.move(300, 50)
        self.connectButton.setFixedSize(200, 50)
        
        # Spinbox to select the baudrate (should be 115200 by default)
        self.freqBox = QSpinBox(self)
        self.freqBox.move(50, 120)
        self.freqBox.setFixedSize(200, 50)
        self.freqBox.setRange(0, 115200)
        self.freqBox.setValue(115200)
        self.freqBox.valueChanged.connect(self.radio.setBaudrate)
        self.freqBox.setSuffix(" Baudrate")      # setting the suffix to " Baudrate"
        
        # Connect button to the function that gets the selected port
        self.connectButton.clicked.connect(self.get_selected_port)
        
        # end of __init__ function
        
    
    def get_selected_port(self):
        ''' Gets the selected port from the dropdown menu and initializes the radio '''
        self.radio.setCOM(self.postList.currentText().split(" : ")[0])

        print(self.postList.currentText().split(" : ")[0] + " selected")
        
        if(self.radio.init()):
            self.radio.running = True
            print("Serial port opened successfully")
            self.close() 
        else:
            print("Failed to open serial port")
        #  end of get_selected_port function 