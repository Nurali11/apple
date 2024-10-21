import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QFrame
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class DeviceFrame(QWidget):
    def __init__(self):
        super().__init__()

        # Устанавливаем параметры окна
        self.setWindowTitle("Устройство")
        self.setFixedSize(400, 500)

        # Создаем вертикальный layout
        main_layout = QVBoxLayout()

        # Создаем рамку для изображения и цены
        self.inner_frame = QFrame()
        self.inner_frame.setStyleSheet('border: none;')
        inner_layout = QVBoxLayout()

        # Загружаем изображение устройства
        image_path = "iphone15.png"  # Замените на путь к вашему изображению
        pixmap = QPixmap(image_path)

        # Создаем метку для изображения
        image_label = QLabel()
        image_label.setPixmap(pixmap)
        image_label.setAlignment(Qt.AlignCenter)

        # Создаем метку для цены
        price_label = QLabel("Price: $999")
        price_label.setStyleSheet('font-size: 40px')
        price_label.setAlignment(Qt.AlignCenter)

        # Добавляем элементы в внутренний layout
        inner_layout.addWidget(image_label)
        inner_layout.addWidget(price_label)
        self.inner_frame.setLayout(inner_layout)

        # Создаем внешнюю рамку
        self.outer_frame = QFrame()
        self.outer_frame.setFrameShape(QFrame.Box)
        self.outer_frame.setFixedSize(300, 400)
        self.outer_frame.setLineWidth(10)
        self.outer_frame.setStyleSheet('border-radius: 15px; border: 3px solid black;')

        # Добавляем внутренний фрейм во внешний
        outer_layout = QVBoxLayout()
        outer_layout.addWidget(self.inner_frame)
        self.outer_frame.setLayout(outer_layout)

        # Добавляем внешний фрейм в основной layout окна
        main_layout.addWidget(self.outer_frame)
        self.setLayout(main_layout)

        # Подключаем события для увеличения рамки
        self.outer_frame.setMouseTracking(True)
        self.outer_frame.enterEvent = self.mouseEnter
        self.outer_frame.leaveEvent = self.mouseLeave

    def mouseEnter(self, event):
        self.outer_frame.setFixedSize(310, 410)  # Увеличиваем размер рамки

    def mouseLeave(self, event):
        self.outer_frame.setFixedSize(300, 400)  # Возвращаемся к исходному размеру

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DeviceFrame()
    window.show()
    sys.exit(app.exec_())
