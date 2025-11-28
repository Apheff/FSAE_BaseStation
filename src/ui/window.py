from PyQt6.QtWidgets import QWidget, QGridLayout
from .customwidgets import BoxWidget

class Window(QWidget):
    def __init__(self, width, height):
        ''' Main Window of the application '''
        super().__init__()
        self.setWindowTitle("FSAE Base Station")
        self.setFixedSize(width, height)
        
        # creation of the the text boxes using a dictionary
        # Important telemetry cards
        self.cards = {
            "ST": BoxWidget("Steering"),
            "TP": BoxWidget("Throttle"),   
            "BS": BoxWidget("Brake"),
            "M": BoxWidget("Marcia"),
            "CS": BoxWidget("Clutch system"),
            "OT": BoxWidget("Oil Temp"),
            "WT": BoxWidget("Water Temp"),
            "RPM": BoxWidget("RPM"),
            "OP": BoxWidget("Oil Pressure"),
            "SS": BoxWidget("Status"),
        }

        # Card Grid Layout
        grid = QGridLayout()
        grid.setSpacing(20)
        
        # arranging the text boxes in a grid [N x 3]
        row = 0
        col = 0
        for card in self.cards.values():
            grid.addWidget(card, row, col)
            col += 1
            if col > 2:
                row += 1
                col = 0
        self.setLayout(grid)
    # end of __init__ function

    
    def update_card(self, key, value):
        ''' Function that updates the value of a specific card '''
        if(key not in self.cards.keys()):
            # if the received key is not in the dictionary we just return
            # hopefully this should not happen
            return

        if(not value.isdigit()):
            # here we print and set a default value if the received value is not valid 
            print("/!\\ Value missing: keeping the previous one")
            return
        
        # debug print
        print("Received:", key, value)
        self.cards[key].setValue(str(value))
    # end of update_card function

    
