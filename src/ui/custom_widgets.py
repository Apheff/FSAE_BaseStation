from PyQt6.QtCore import Qt, QUrl, QRectF
from PyQt6.QtGui import QFont, QPainter, QPixmap, QPen, QColor
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QProgressBar
import math
import ui.server as server


class BoxWidget(QWidget):
    def __init__(self, title, value="0"):
        super().__init__()
        self.setStyleSheet("""
            QWidget {
                background-color: rgba(40, 40, 40, 170);
                border-radius: 24px;
                padding: 24px;
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


        layout.addWidget(title_label, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(value_label, alignment=Qt.AlignmentFlag.AlignCenter)
        self.value_label = value_label
        self.setLayout(layout)

    def setValue(self, v):
        self.value_label.setText(str(v))

    # function that sets the value of the info widget


class MapWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.web = QWebEngineView(self)
        self.web.resize(self.width(), self.height())

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


class HistogramWidget(QWidget):
    def __init__(self, title="Title", max_value=100, color="#4CAF50"):
        super().__init__()

        self.max_value = max_value
        self.color = color

        # Main layout
        layout = QVBoxLayout(self)

        # Vertical progress bar
        self.bar = QProgressBar()
        self.bar.setRange(0, self.max_value)
        self.bar.setValue(0)
        self.bar.setTextVisible(False)
        self.bar.setOrientation(Qt.Orientation.Vertical)
        self.bar.setFixedSize(50, 350)

        # Title label
        self.label = QLabel(title)
        self.label.setStyleSheet("color: white; font-weight: bold;")

        layout.addWidget(self.bar, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label, alignment=Qt.AlignmentFlag.AlignCenter)

        # Apply initial styles
        self.updateStyle()

        self.setStyleSheet("background-color: #2b2b2b; border-radius: 15px;")
        self.setMinimumSize(200, 400)

    # Method to change value
    def setValue(self, value):
        self.bar.setValue(value)

    # Method to change color dynamically
    def setColor(self, color):
        self.color = color
        self.updateStyle()

    # Internal method to update stylesheet
    def updateStyle(self):
        self.bar.setStyleSheet(f"""
            QProgressBar {{
                border: 2px solid #444;
                border-radius: 8px;
                background-color: #222;
            }}
            QProgressBar::chunk {{
                background-color: {self.color};
                border-radius: 6px;
            }}
        """)

class ImageWidget(QWidget):
    def __init__(self, fileName, scaleW=100, scaleH=100):
        super().__init__()

        layout = QVBoxLayout(self)

        self.label = QLabel()
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Load image immediately
        pixmap = QPixmap(fileName)
        self.label.setPixmap(
            pixmap.scaled(
                scaleW, scaleH,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )
        )

        layout.addWidget(self.label)

class TextWidget(QWidget):
    def __init__(self, title, value="0"):
        super().__init__()
        self.setStyleSheet("""
            QLabel {
                color: white;
            }
        """)
        layout = QVBoxLayout()
        title_label = QLabel(title)
        title_label.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        value_label = QLabel(value)
        value_label.setFont(QFont("Arial", 28, QFont.Weight.Bold))

        layout.addWidget(title_label)
        layout.addWidget(value_label)
        self.value_label = value_label
        self.setLayout(layout)

    def setValue(self, v):
        self.value_label.setText(str(v))


class GaugeWidget(QWidget):
    def __init__(self, min_value=0, max_value=100, title="Gauge"):
        super().__init__()

        self.min_value = min_value
        self.max_value = max_value
        self.value = 0

        title_label = QLabel(title)
        title_label.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        title_label.setAlignment(Qt.AlignmentFlag.AlignTop)

        layout = QVBoxLayout(self)
        layout.addWidget(title_label)
        
        self.setMinimumSize(350, 350)

    def setValue(self, value):
        value = int(value)
        self.value = max(self.min_value, min(value, self.max_value))
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        width = self.width()
        height = self.height()
        radius = min(width, height) / 2 - 20

        center_x = width / 2
        center_y = height * 0.9

        # Draw arc (background)
        pen = QPen(QColor("#444"), 15)
        painter.setPen(pen)

        rect = QRectF(center_x - radius, center_y - radius,
                      radius * 2, radius * 2)

        start_angle = 180 * 16
        span_angle = -180 * 16
        painter.drawArc(rect, start_angle, span_angle)

        # Calculate needle angle
        value_ratio = (self.value - self.min_value) / (self.max_value - self.min_value)
        angle = 180 - (value_ratio * 180)

        # Draw needle
        painter.setPen(QPen(QColor("red"), 4))

        needle_length = radius - 10
        rad = math.radians(angle)

        x = center_x + needle_length * math.cos(rad)
        y = center_y - needle_length * math.sin(rad)

        painter.drawLine(int(center_x), int(center_y), int(x), int(y))

        # Draw center circle
        painter.setBrush(QColor("red"))
        painter.drawEllipse(int(center_x - 6), int(center_y - 6), 12, 12)

        # Draw value text
        painter.setPen(QColor("white"))
        painter.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        painter.drawText(0, int(height * 0.3), width, 30,
                         Qt.AlignmentFlag.AlignCenter,
                         str(self.value))
