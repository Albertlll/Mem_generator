import sys
import sqlite3
from pprint import pprint
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QListWidgetItem, QWidget, QColorDialog,\
    QListWidget, QPushButton, QSpinBox, QLineEdit
from PyQt5 import uic
import math
from PyQt5.QtGui import QPixmap, QColor, QIcon
from PIL import Image, ImageDraw, ImageFont
from font_list import FontsList
from text_on_mem import TextOnMem
from constants import *
from mem_gen_tests import TextParametrs
from PyQt5.QtCore import Qt


class ShablonPicture(QWidget):
    def __init__(self, im, shablon_texts):
        super().__init__()
        uic.loadUi('UI\\generator_ui.ui', self)

        self.shablon_texts = shablon_texts
        self.image.setPixmap(QPixmap(im))
        self.load_btn.setEnabled(False)
        self.add_text_btn.setEnabled(True)
        self.export_btn.setEnabled(True)
        self.export_btn.clicked.connect(self.export)
        self.add_text_btn.clicked.connect(self.add_text)
        self.listWidget.itemDoubleClicked.connect(self.open_parametrs)
        self.texts = []
        self.fname = im
        self.pil_file = Image.open(im)
        self.pil_file.thumbnail(IMAGE_ON_APP_SIZES)
        self.add_begin_text()
        self.reload_texts()

    def keyPressEvent(self, event):
        if int(event.modifiers()) == Qt.ControlModifier:
            if event.key() == Qt.Key_E:
                if self.export_btn.isEnabled():
                    self.export()
            if event.key() == Qt.Key_A:
                if self.add_text_btn.isEnabled():
                    self.add_text()


    def export(self):
        name = QFileDialog.getSaveFileName(self, 'Save File', '', "Картинка (*.jpg);;Картинка (*.png)")[0]
        if not name:
            return None
        save_file = open(name, 'wb')
        im_file = open("redacting.png", "rb")
        save_file.write(im_file.read())
        save_file.close()

    def add_begin_text(self):
        n_of_texts = int(self.shablon_texts[0])
        ind_in_shab_list = 0
        for i in range(n_of_texts):
            x = int(self.shablon_texts[ind_in_shab_list + 1])
            y = int(self.shablon_texts[ind_in_shab_list + 2])
            text = self.shablon_texts[ind_in_shab_list + 3]
            clr = tuple([int(i) for i in self.shablon_texts[ind_in_shab_list + 4].split()])
            fnt = self.shablon_texts[ind_in_shab_list + 5]
            fnt_size = int(self.shablon_texts[ind_in_shab_list + 6])

            item = TextOnMem(x, y, text, clr, fnt, fnt_size)
            self.listWidget.addItem(str(item))
            self.texts.append(item)
            ind_in_shab_list += 6

    def add_text(self):
        item = TextOnMem()
        self.listWidget.addItem(str(TextOnMem()))
        self.texts.append(item)
        self.reload_texts()

    def reload_texts(self):
        self.pil_file = Image.open(self.fname)
        self.pil_file.thumbnail(IMAGE_ON_APP_SIZES)
        draw_pil_file = ImageDraw.Draw(self.pil_file)
        for i in range(len(self.texts)):
            txt = self.texts[i]
            font = ImageFont.truetype(txt.font, txt.font_size)
            draw_pil_file.text((txt.x, txt.y), str(txt), fill=txt.color, font=font)
        # self.image.resize(*pil_file.size)
        self.pil_file.save("redacting.png")

        self.pixmap = QPixmap("redacting.png")
        self.image.setPixmap(self.pixmap)

    def open_parametrs(self):
        self.parametrs = TextParametrs(self.sender().currentRow(), self.texts, self)
        self.parametrs.show()
        self.setEnabled(True)

