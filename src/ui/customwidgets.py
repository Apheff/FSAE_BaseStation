from PyQt6.QtWidgets import QFrame, QVBoxLayout, QLabel
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

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

