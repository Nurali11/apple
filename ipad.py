from PyQt5.QtWidgets import *
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt

class ipad_Frame(QFrame):
    def __init__(self, image_path, model_name, price):
        super().__init__()
        self.setStyleSheet('border: 3px solid black; border-radius: 20px;')
        self.setFixedSize(300, 400)

        frame_layout = QVBoxLayout()

        image_label = QLabel()
        pixmap = QPixmap(image_path)
        image_label.setPixmap(pixmap.scaled(280, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        image_label.setAlignment(Qt.AlignCenter)

        model_label = QLabel(model_name)
        model_label.setAlignment(Qt.AlignCenter)
        model_label.setStyleSheet('font-size: 18px; font-weight: bold;')

        price_label = QLabel(price)
        price_label.setAlignment(Qt.AlignCenter)
        price_label.setStyleSheet('font-size: 16px; color: gray;')

        frame_layout.addWidget(image_label)
        frame_layout.addWidget(model_label)
        frame_layout.addWidget(price_label)

        self.setLayout(frame_layout)

    def enterEvent(self, event):
        self.setStyleSheet('border: 3px solid green; border-radius: 20px;')
        self.setFixedSize(self.width() + 10, self.height() + 10) 
        super().enterEvent(event)

    def leaveEvent(self, event):
        self.setStyleSheet('border: 3px solid black; border-radius: 20px;')
        self.setFixedSize(self.width() - 10, self.height() - 10) 
        super().leaveEvent(event)

    def mousePressEvent(self, event):
        self.device_window = DeviceDetailWindow(self)
        self.device_window.show()
        super().mousePressEvent(event)


class DeviceDetailWindow(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.setWindowTitle("Device Details")
        self.setFixedSize(400, 300)


class Ipad_Window(QWidget):
    def __init__(self, obj):
        self.obj = obj
        super().__init__()
        self.setWindowTitle("ipad Models")
        self.setFixedSize(1900, 980)

        self.v_main_layout = QVBoxLayout()

        # Top layout for the exit button
        self.top_layout = QHBoxLayout()
        self.exit_button = QPushButton()
        exit_icon = QIcon("exit.png")  # Use your exit icon
        self.exit_button.setIcon(exit_icon)
        self.exit_button.setFixedSize(60, 60)  # Set the button size to 40x40
        self.exit_button.setIconSize(self.exit_button.size())  # Set icon size to match button size
        self.exit_button.clicked.connect(self.exit)  # Connect to close method

        # Align the button to the top right corner
        self.top_layout.addStretch()
        self.top_layout.addWidget(self.exit_button)
        self.v_main_layout.addLayout(self.top_layout)

        self.h_lay_top = QHBoxLayout()
        self.h_lay_bottom = QHBoxLayout()

        ipad_models = [
            ("ipad1.png", "Ipad Pro", "$999"),
            ("ipad2.png", "Ipad Air", "$599"),
            ("ipad3.png", "Ipad", "$399"),
            ("ipad4.png", "Ipad Mini", "$750")
        ]

        for i, (image_path, model_name, price) in enumerate(ipad_models):
            frame = ipad_Frame(image_path, model_name, price)

            if i < 5:
                self.h_lay_top.addWidget(frame)
            else:
                self.h_lay_bottom.addWidget(frame)

        self.v_main_layout.addLayout(self.h_lay_top)
        self.v_main_layout.addLayout(self.h_lay_bottom)

        self.setLayout(self.v_main_layout)
    
    def exit(self):
        self.hide()
        self.obj.show()