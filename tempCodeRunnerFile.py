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