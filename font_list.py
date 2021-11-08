import sqlite3
from PyQt5.QtWidgets import QListWidgetItem, QWidget
from PyQt5 import uic
from PyQt5.QtGui import QIcon
import os.path
from constants import *
from ql_que import get_answer_on_font
from font_list_ui import Ui_Form


class FontsList(QWidget, Ui_Form):
    def __init__(self, txt_param_self):
        super().__init__()
        self.setupUi(self)
        self.txt_param_self = txt_param_self
        self.find_ask = ""
        self.search()
        self.search_edit.textChanged.connect(self.search)

    def search(self):
        self.list.clear()
        self.find_ask = self.search_edit.text()
        self.result = get_answer_on_font(self.find_ask)
        for i in self.result:
            if not os.path.exists(i[1]):
                continue
            item = QListWidgetItem()
            item.setIcon(QIcon(i[INDEX_OF_ICON]))
            item.setText(i[INDEX_OF_TEXT])
            self.list.addItem(item)

        self.list.itemDoubleClicked.connect(self.save_font)

    def save_font(self):
        real_result = self.result[self.sender().currentRow()][0]
        self.txt_param_self.sndr.font = real_result
        self.txt_param_self.save()
        self.hide()
