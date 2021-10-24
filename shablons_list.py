import sys
from PyQt5.QtWidgets import QApplication, QWidget,QScrollArea, QScrollBar
from PyQt5 import uic


class ShablonsList(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('shablon_list.ui', self)
        # for i in range(10):
    # def

