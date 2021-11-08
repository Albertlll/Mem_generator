import sys
from PyQt5.QtWidgets import QApplication, QFileDialog, QWidget, QColorDialog
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PIL import Image, ImageDraw, ImageFont
from font_list import FontsList
from text_on_mem import TextOnMem
from constants import *
from PyQt5.QtCore import Qt
import sqlite3
import shutil
import text_parameters
import os
from ql_que import add_row_to_recent
from generator_ui import Ui_Form


class BasePicture(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.add_text_btn.clicked.connect(self.add_text)
        self.load_btn.clicked.connect(self.load_image)
        self.listWidget.itemDoubleClicked.connect(self.open_parametrs)
        self.texts = []
        self.export_btn.clicked.connect(self.export)
        self.redacted = False

    def export(self):
        save_name = QFileDialog.getSaveFileName(self, 'Save File', '', "Картинка (*.jpg);;Картинка (*.png)")[0]
        if not save_name:
            return None
        # Запись как шаблона(для использования в недавних)
        number_txt_file_read = open("Недавние\\number.txt", mode="r")
        num = int(number_txt_file_read.readlines()[0].strip())
        number_txt_file_write = open("Недавние\\number.txt", mode="w")
        number_txt_file_write.write(str(num + 1))
        os.mkdir("Недавние" + "\\" + str(num))
        shutil.copyfile(self.fname, f"Недавние\\{str(num)}\\{str(num)}.png")

        texts_file = open("Недавние" + "\\" + str(num) + "\\" + "texts_on_mem.txt", mode="w", encoding="utf-8")

        num_of_texts = len(self.texts)
        texts_file.write(str(num_of_texts) + "\n")

        # Создание файла с параметрами текстов
        for i in range(num_of_texts):
            text_on_mem_now = self.texts[i]
            texts_file.write(str(text_on_mem_now.x) + "\n")
            texts_file.write(str(text_on_mem_now.y) + "\n")
            texts_file.write(str(text_on_mem_now.text) + "\n")
            texts_file.write(str(" ".join([str(i) for i in text_on_mem_now.color])) + "\n")
            texts_file.write(str(text_on_mem_now.font) + "\n")
            texts_file.write(str(text_on_mem_now.font_size) + "\n")

        texts_file.close()
        add_row_to_recent(num)
        save_file = open(save_name, 'wb')
        im_file = open("redacting.png", "rb")
        save_file.write(im_file.read())
        save_file.close()

    def add_text(self):
        self.redacted = True
        item = TextOnMem()
        self.listWidget.addItem(str(TextOnMem()))
        self.texts.append(item)
        self.reload_texts()

    def load_image(self):
        self.redacted = True
        self.fname = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '', 'JPG(*.jpg);;PNG(*.png)')[0]
        if not self.fname:
            return None
        self.pil_file = Image.open(self.fname)
        self.pil_file.thumbnail(IMAGE_ON_APP_SIZES)
        self.reload_texts()
        self.add_text_btn.setEnabled(True)
        self.export_btn.setEnabled(True)

        self.load_btn.setEnabled(False)

    def reload_texts(self):
        self.pil_file = Image.open(self.fname)
        self.pil_file.thumbnail(IMAGE_ON_APP_SIZES)
        draw_pil_file = ImageDraw.Draw(self.pil_file)
        for i in range(len(self.texts)):
            txt = self.texts[i]
            self.listWidget.item(i).setText(str(txt))
            font = ImageFont.truetype(txt.font, txt.font_size)
            draw_pil_file.text((txt.x, txt.y), str(txt), fill=txt.color, font=font)
        self.pil_file.save("redacting.png")
        self.pixmap = QPixmap("redacting.png")
        self.image.setPixmap(self.pixmap)

    def open_parametrs(self):
        self.parametrs = text_parameters.TextParametrs(self.sender().currentRow(), self.texts, self)
        self.parametrs.show()
        self.setEnabled(True)
