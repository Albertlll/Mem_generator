from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class ScrollLabel(QScrollArea):
    def __init__(self, *args, **kwargs):
        QScrollArea.__init__(self, *args, **kwargs)
        self.setWidgetResizable(True)
        content = QWidget(self)
        self.setWidget(content)
        lay = QVBoxLayout(content)
        self.label = QLabel(content)
        self.label.setWordWrap(True)
        lay.addWidget(self.label)

    # the setText method

    def setText(self, text):
        self.label.setText(text)


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python ")
        self.setGeometry(100, 100, 600, 400)
        self.UiComponents()
        self.show()

    def UiComponents(self):
        text = "ааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааа"

        label = ScrollLabel(self)
        label.setText(text)
        label.setGeometry(100, 100, 200, 80)


App = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(App.exec())