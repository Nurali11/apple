from PyQt5.QtWidgets import *

class Ipad_Window(QWidget):
    def __init__(self, obj):
        self.obj = obj
        super().__init__()
        self.btn = QPushButton('Bosma', self)
        self.btn.clicked.connect(self.Bosildi)
    def Bosildi(self):
        self.hide()
        self.obj.show()