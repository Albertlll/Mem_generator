import sys
from PyQt5.QtGui import QIcon
from PyQt5 import uic
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QListWidgetItem, QWidget, QColorDialog,\
    QListWidget, QPushButton, QSpinBox, QLineEdit
from PyQt5 import uic
from PyQt5.QtGui import QPixmap, QColor
from PIL import Image, ImageDraw, ImageFont
import shablon_picture
import main_window
import recent_pic
from recent_list_ui import Ui_Form
from ql_que import get_all_recent


class RecentList(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.result = get_all_recent()
        for i in self.result:
            item = QListWidgetItem()
            item.setIcon(QIcon(i[0]))
            item.setText(str(i[2]))
            self.list.addItem(item)
        self.list.itemDoubleClicked.connect(self.open_shablon)

    def open_shablon(self):
        real_result = self.result[self.sender().currentRow()]
        text = real_result[1]
        im = real_result[0]
        name = real_result[2]
        shab_txt_file = [open(text, 'rt', encoding='utf-8').readlines()[0]]
        for i in open(text, 'rt', encoding='utf-8').readlines()[1:]:
            shab_txt_file.append(i.strip())
        self.hide()
        self.shablon = recent_pic.RecentPicture(im, shab_txt_file)
        self.shablon.show()

    def closeEvent(self, event):
        self.main_form = main_window.MainForm()
        self.main_form.show()
