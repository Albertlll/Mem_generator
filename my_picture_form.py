import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic


class MyPictureForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 300, 800, 200)
        
