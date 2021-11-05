import sys
import sqlite3
from pprint import pprint
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QListWidgetItem, QWidget, QColorDialog,\
    QListWidget, QPushButton, QSpinBox, QLineEdit
from PyQt5 import uic
import math
from PyQt5.QtGui import QPixmap, QColor, QIcon
from PIL import Image, ImageDraw, ImageFont


class FontsList(QWidget):
    def __init__(self, txt_param_self):
        super().__init__()
        uic.loadUi('UI\\font_list_ui.ui', self)
        self.txt_param_self = txt_param_self
        self.find_ask = ""
        self.search()
        self.search_edit.textChanged.connect(self.search)

    def search(self):
        self.list.clear()
        con = sqlite3.connect("БД\\fonts_DB.sqlite")
        cur = con.cursor()
        self.find_ask = self.search_edit.text()

        self.result = cur.execute(f"""SELECT * FROM fonts
                            WHERE Имя like '%{self.find_ask}%'""").fetchall()
        for i in self.result:
            item = QListWidgetItem()
            item.setIcon(QIcon(i[1]))
            item.setText(i[2])
            self.list.addItem(item)

        self.list.itemDoubleClicked.connect(self.save_font)

    def save_font(self):
        real_result = self.result[self.sender().currentRow()][0]
        self.txt_param_self.sndr.font = real_result
        self.txt_param_self.save()
