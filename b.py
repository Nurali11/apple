import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QVBoxLayout, QWidget, QLabel, QPushButton, QHBoxLayout
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import QPropertyAnimation, QRect, Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Apple.com Clone")
        self.setGeometry(100, 100, 1280, 720)
        self.setStyleSheet("background-color: white;")

        # Навигационная панель
        self.create_navbar()

        # Центральный виджет с несколькими страницами
        self.stacked_widget = QStackedWidget(self)
        self.stacked_widget.setGeometry(0, 50, 1280, 670)

        # Создание страниц для продуктов
        self.create_product_pages()

        # Анимация для плавного перехода между страницами
        self.animation = QPropertyAnimation(self.stacked_widget, b"geometry")

    def create_navbar(self):
        """Создание навигационной панели с кнопками"""
        nav_layout = QHBoxLayout()
        self.nav_widget = QWidget(self)
        self.nav_widget.setGeometry(0, 0, 1280, 50)
        self.nav_widget.setStyleSheet("""
            background-color: #f8f8f8; 
            border-bottom: 2px solid #dcdcdc;
            font-family: Arial, sans-serif;
        """)
        self.nav_widget.setLayout(nav_layout)

        # Создаем кнопки навигации
        buttons = ["iPhone", "iPad", "Mac", "Apple Watch", "AirPods", "Apple TV"]
        for button_name in buttons:
            button = QPushButton(button_name, self)
            button.setFont(QFont("Arial", 12))
            button.setStyleSheet("""
                QPushButton { 
                    border: none; 
                    padding: 10px 20px; 
                    color: #333; 
                    transition: background-color 0.3s ease; 
                }
                QPushButton:hover { 
                    background-color: #e1e1e1;
                    border-radius: 5px;
                }
            """)
            button.clicked.connect(self.on_click)
            nav_layout.addWidget(button)

    def create_product_pages(self):
        """Создание страниц для различных моделей продуктов"""
        # iPhone models
        iphone_models = {
            "iPhone 14": ("iphone14.png", "Meet iPhone 14, with advanced camera features and a powerful A15 chip."),
            "iPhone 15": ("iphone15.png", "Meet iPhone 15, now with Dynamic Island and even better performance."),
            "iPhone 16 Pro Max": ("iphone16promax.png", "Introducing iPhone 16 Pro Max, the ultimate iPhone with a stunning display."),
        }

        # iPad models
        ipad_models = {
            "iPad Air": ("ipadair.png", "iPad Air is powerful, portable, and versatile."),
            "iPad Pro": ("ipadpro.png", "iPad Pro features the powerful M1 chip for incredible performance."),
        }

        # Mac models
        mac_models = {
            "MacBook Air": ("macbookair.png", "The MacBook Air with M2 chip is ultra-thin and lightweight."),
            "MacBook Pro": ("macbookpro.png", "MacBook Pro with M2 chip delivers phenomenal performance."),
        }

        # Creating pages for devices
        self.create_device_pages("iPhone", iphone_models)
        self.create_device_pages("iPad", ipad_models)
        self.create_device_pages("Mac", mac_models)

        # Add additional device pages here
        self.create_device_pages("Apple Watch", {"Apple Watch Series 8": ("watch.png", "Stay fit and healthy with Apple Watch Series 8.")})
        self.create_device_pages("AirPods", {"AirPods Pro": ("airpods.png", "Enjoy active noise cancellation with AirPods Pro.")})
        self.create_device_pages("Apple TV", {"Apple TV 4K": ("tv.png", "Experience stunning 4K video with Apple TV.")})

    def create_device_pages(self, title, models):
        """Создание страниц для каждого устройства"""
        for model_name, (image_path, description) in models.items():
            page = self.create_product_page(f"{title}: {model_name}", image_path, description)
            self.stacked_widget.addWidget(page)

    def create_product_page(self, title, image_path, description):
        """Создание страницы продукта с изображением и текстом"""
        page = QWidget()
        layout = QVBoxLayout()
        
        # Баннер продукта
        banner_layout = QVBoxLayout()
        title_label = QLabel(title)
        title_label.setFont(QFont("Arial", 28, QFont.Bold))
        title_label.setStyleSheet("color: #333; margin: 20px;")
        banner_layout.addWidget(title_label, alignment=Qt.AlignCenter)

        # Описание продукта
        description_label = QLabel(description)
        description_label.setFont(QFont("Arial", 16))
        description_label.setWordWrap(True)
        description_label.setStyleSheet("color: #666; margin: 0 50px;")
        banner_layout.addWidget(description_label, alignment=Qt.AlignCenter)

        # Изображение продукта
        image_label = QLabel()
        pixmap = QPixmap(image_path)
        image_label.setPixmap(pixmap.scaled(800, 400, Qt.KeepAspectRatio))  # Адаптивный размер изображения
        banner_layout.addWidget(image_label, alignment=Qt.AlignCenter)

        layout.addLayout(banner_layout)
        page.setLayout(layout)
        return page

    def on_click(self):
        """Плавный переход на другую страницу"""
        sender = self.sender()
        current_index = self.stacked_widget.currentIndex()
        # Получаем индекс кнопки навигации
        next_index = ["iPhone", "iPad", "Mac", "Apple Watch", "AirPods", "Apple TV"].index(sender.text())
        
        # Плавная анимация перехода
        self.animate_transition(current_index, next_index)

    def animate_transition(self, current_index, next_index):
        """Анимация смены страницы"""
        self.animation.setDuration(500)
        self.animation.setStartValue(QRect(1280, 50, 1280, 670))  # Анимация слева направо
        self.animation.setEndValue(QRect(0, 50, 1280, 670))
        self.stacked_widget.setCurrentIndex(next_index)
        self.animation.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
