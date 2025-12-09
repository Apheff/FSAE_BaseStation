from PyQt6.QtWidgets import QGridLayout, QWidget

from .customwidgets import BoxWidget, MapWidget


class Window(QWidget):
    def __init__(self, width, height):
        """Main Window of the application"""
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
            "P": MapWidget(),
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
        """Function that updates the value of a specific card"""
        if key not in self.cards.keys():
            # if the received key is not in the dictionary we just return
            # hopefully this should not happen
            return

        # debug print
        print("Received:", key, value)

        if (key == "P"):
            if(len(value.split("-")) == 2):
                lat = float(value.split("-")[0])
                lon = float(value.split("-")[1])
                self.cards[key].setPosition(lat, lon)
        else:
            self.cards[key].setValue(value)

    # end of update_card function
