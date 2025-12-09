from PyQt6.QtCore import Qt, QUrl
from PyQt6.QtGui import QFont
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWidgets import QFrame, QLabel, QVBoxLayout

import ui.server as server


class BoxWidget(QFrame):
    def __init__(self, title, value="0"):
        super().__init__()
        self.setStyleSheet("""
            QFrame {
                background-color: rgba(40, 40, 40, 170);
                border-radius: 15px;
                padding: 15px;
                border: 1px solid rgba(150,150,150,60);
            }
            QLabel {
                color: white;
            }
        """)
        layout = QVBoxLayout()
        title_label = QLabel(title)
        title_label.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        value_label = QLabel(value)
        value_label.setFont(QFont("Arial", 28, QFont.Weight.Bold))
        value_label.setAlignment(Qt.AlignmentFlag.AlignRight)

        layout.addWidget(title_label)
        layout.addWidget(value_label)
        self.value_label = value_label
        self.setLayout(layout)

    def setValue(self, v):
        self.value_label.setText(str(v))

    # function that sets the value of the info widget


class MapWidget(QFrame):
    def __init__(self):
        super().__init__()
        self.resize(900, 600)

        self.web = QWebEngineView(self)
        self.web.resize(900, 600)

        # URL del file HTML servito dal server
        url = QUrl(f"http://localhost:{server.PORT}/ui/map.html")
        self.web.load(url)

        # Stato della pagina
        self.page_is_ready = False
        self.pending_position = None

    def setPosition(self, lat, lon):
        try:
            lat = float(lat)
            lon = float(lon)
        except ValueError:
            print("ERRORE: Latitudine o longitudine non numerica")
            return
        self.web.page().runJavaScript(f"setPosition({lat}, {lon});")
