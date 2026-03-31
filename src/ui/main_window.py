from PyQt6.QtWidgets import QHBoxLayout, QSlider, QWidget, QVBoxLayout
from PyQt6.QtCore import Qt
from .custom_widgets import BoxWidget, GaugeWidget, HistogramWidget, MapWidget, ImageWidget, TextWidget


class MainWindow(QWidget):
    def __init__(self):
        """Main Window of the application"""
        super().__init__()
        self.setWindowTitle("FSAE Base Station")

        # creation of the the text boxes using a dictionary
        # Important telemetry cards
        self.cards = {
            "B": HistogramWidget("Brake", color= "#00FF00"),
            "T": HistogramWidget("Throttle", color= "#FFFFFF"),
            "C": HistogramWidget("Clutch", color= "#FF0000"),
            "S": GaugeWidget(0, 180, "Steering"),
            "G": BoxWidget("Gear"),
            "OT": TextWidget("Oil Temp"),
            "WT": TextWidget("Water Temp"),
            "R": GaugeWidget(0, 8000, "RPM"),
            "OP": TextWidget("Oil Pressure"),
            "L": MapWidget(),
        }

        main_layout = QVBoxLayout()
        main_layout.setSpacing(10)

        # ---- LOGO ----
        logo_row = QHBoxLayout()
        logo_row.addStretch()  # add stretch to center the logo


        logo_row.addWidget(ImageWidget("assets/logo.png", scaleW=200, scaleH=100))
        main_layout.addLayout(logo_row)

        # ---- ROW 1 ----
        row1 = QHBoxLayout()

        row1.addWidget(self.cards["B"], stretch=1)  # smaller
        row1.addWidget(self.cards["T"], stretch=1)  # smaller
        row1.addWidget(self.cards["C"], stretch=1)  # smaller
        row1.addWidget(self.cards["R"], stretch=2, alignment=Qt.AlignmentFlag.AlignCenter)  # bigger
        row1.addWidget(self.cards["S"], stretch=2, alignment=Qt.AlignmentFlag.AlignCenter)  # bigger

        main_layout.addLayout(row1)

        # ---- ROW 2 ----
        row2 = QHBoxLayout()

        row2.addWidget(self.cards["L"], stretch=3)  # biggest
        row2.addWidget(self.cards["G"], stretch=2)  # bigger

        col1 = QVBoxLayout()
        col1.addWidget(ImageWidget("ui/water-temperature.svg"), stretch=1)
        col1.addWidget(ImageWidget("ui/engine-oil.svg"), stretch=1)
        row2.addLayout(col1, stretch=2)

        col2 = QVBoxLayout()
        col2.addWidget(self.cards["WT"], stretch=1)  # smaller
        col2.addWidget(self.cards["OT"], stretch=1)  # smaller
        col2.addWidget(self.cards["OP"], stretch=1)  # smaller
        row2.addLayout(col2, stretch=2)

        main_layout.addLayout(row2)

        self.setLayout(main_layout)

    # end of __init__ function

    def update_card(self, key, value):
        """Function that updates the value of a specific card"""
        if key not in self.cards.keys():
            # if the received key is not in the dictionary we just return
            # hopefully this should not happen
            return
        

        if(not value.isnumeric() and key not in ["L", "G"]):  # if the value is not numeric and the card is not the map or the gear box, we just
            return
        elif(value.isnumeric()):
            value = int(value)

        # debug print
        print("Received:", key, value)

        if (key == "L"):
            if(len(value.split("-")) == 2):
                lat = value.split("-")[0]
                lon = value.split("-")[1]
                self.cards[key].setPosition(lat, lon)
        else:
            self.cards[key].setValue(value)

    # end of update_card function
