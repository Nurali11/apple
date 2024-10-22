from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QFrame, QHBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from iphone import Iphone_Window
from ipad import Ipad_Window
from mac import Mac_Window
from watch import Watch_Window
from aksesuar import Aksesuar_Window  


class Frame_Window(QFrame):
    def __init__(self, obj, rasmi, nomi, window_class):
        self.obj = obj
        super().__init__()
        self.setFrameShape(QFrame.Box)
        self.setLineWidth(2)
        self.setStyleSheet('border-radius: 10px; border: 2px solid gray;')
        self.window_class = window_class

        self.v_lay = QVBoxLayout(self)

        self.icon_label = QLabel()
        logo = QPixmap(rasmi)
        logo = logo.scaled(150, 150, Qt.KeepAspectRatio)
        self.icon_label.setPixmap(logo)
        self.icon_label.setAlignment(Qt.AlignCenter)

        self.name_label = QLabel(nomi)
        self.name_label.setAlignment(Qt.AlignCenter)
        self.name_label.setStyleSheet('font-size: 30px; font-weight: bold;')

        self.v_lay.addWidget(self.icon_label)
        self.v_lay.addWidget(self.name_label)

    def enterEvent(self, event):
        self.setStyleSheet('border: 3px solid green; border-radius: 10px;')
        self.setFixedSize(self.width() + 10, self.height() + 10) 
        super().enterEvent(event)

    def leaveEvent(self, event):
        self.setStyleSheet('border: 3px solid black; border-radius: 10px; border: 2px solid gray;')        
        self.setFixedSize(self.width() - 10, self.height() - 10) 
        super().leaveEvent(event)

    def mousePressEvent(self, event):
        self.device_window = self.window_class(self.obj)
        self.obj.hide()
        self.device_window.show()
        super().mousePressEvent(event)


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Apple Store")
        self.setFixedSize(1900, 980)

        self.v_main_layout = QVBoxLayout(self)

        self.lbl = QLabel('Welcome to Apple store!')
        self.lbl.setStyleSheet('font-size: 70px; font-weight: bold')
        self.lbl.setAlignment(Qt.AlignHCenter)

        self.logo = QLabel()
        apple_logo = QPixmap("apple.png")
        apple_logo = apple_logo.scaled(300, 300, Qt.KeepAspectRatio)
        self.logo.setPixmap(apple_logo)
        self.logo.setAlignment(Qt.AlignHCenter | Qt.AlignTop)

        self.lbl2 = QLabel('Nima sotib olmoqchisiz?')
        self.lbl2.setStyleSheet('font-size: 50px; font-weight: solid')
        self.lbl2.setAlignment(Qt.AlignHCenter)

        self.v_main_layout.addWidget(self.lbl)
        self.v_main_layout.addWidget(self.logo)
        self.v_main_layout.addWidget(self.lbl2)

        self.h_lay = QHBoxLayout()

        qurilma = [
            ("iPhone", "iphone_logo.png", Iphone_Window),
            ("iPad", "ipad_logo.png", Ipad_Window),
            ("MacBook", "mac_icon.png", Mac_Window),
            ("Apple Watch", "watch_icon.png", Watch_Window),
            ("Accessories", "accessories.png", Aksesuar_Window)
        ]

        for nomi, rasmi, window_class in qurilma:
            frame = Frame_Window(self, rasmi, nomi, window_class)
            self.h_lay.addWidget(frame)

        self.v_main_layout.addLayout(self.h_lay)


app = QApplication([])
window = MyWindow()
window.show()
app.exec_()
