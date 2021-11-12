import sys
from PyQt5.QtGui import QIcon
from PyQt5 import uic
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QListWidgetItem, QWidget, QColorDialog,\
    QListWidget, QPushButton, QSpinBox, QLineEdit
from PyQt5 import uic
from PyQt5.QtGui import QPixmap, QColor
from PIL import Image, ImageDraw, ImageFont
import os
from constants import *
from text_on_mem import *
import shablon_picture
import main_window
import text_parameters
from shablon_list_ui import Ui_Form
from ql_que import get_shablons


class ShablonsList(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.first = True
        self.find_ask = ""
        self.search()
        self.search_edit.textChanged.connect(self.search)

    def search(self):
        self.list.clear()
        self.find_ask = self.search_edit.text()
        self.result = get_shablons(self.find_ask)
        for i in self.result:
            item = QListWidgetItem()
            if not os.path.exists(i[0]):
                continue
            item.setIcon(QIcon(i[0]))
            item.setText(i[1])
            self.list.addItem(item)

        if self.first:
            self.list.itemDoubleClicked.connect(self.open_shablon)
            self.first = False

    def open_shablon(self):
        self.hide()
        real_result = self.result[self.sender().currentRow()]
        text = real_result[2]
        im = real_result[0]
        name = real_result[1]
        print(text)
        shab_txt_file = [i.strip() for i in open(text, 'r', encoding="utf-8").readlines()]
        # for i in shab_txt_file:
        #     print(i)
        self.shablon = shablon_picture.ShablonPicture(im, shab_txt_file)
        self.shablon.show()
        self.setEnabled(True)

    def closeEvent(self, event):
        self.main_form = main_window.MainForm()
        self.main_form.show()
