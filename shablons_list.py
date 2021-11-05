import sys
from PyQt5.QtGui import QIcon
from PyQt5 import uic
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QListWidgetItem, QWidget, QColorDialog,\
    QListWidget, QPushButton, QSpinBox, QLineEdit
from PyQt5 import uic
from PyQt5.QtGui import QPixmap, QColor
from PIL import Image, ImageDraw, ImageFont
from constants import *
from text_on_mem import *
from shablon_picture import ShablonPicture
from mem_gen_tests import MyPicture


class ShablonsList(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI\\shablon_list.ui', self)
        self.find_ask = ""
        self.search()
        self.search_edit.textChanged.connect(self.search)

    def search(self):
        con = sqlite3.connect("БД\\shablons_DB.db")
        cur = con.cursor()
        self.list.clear()
        self.find_ask = self.search_edit.text()

        self.result = cur.execute(f"""SELECT * FROM shablons
                            WHERE Имя like '%{self.find_ask}%'""").fetchall()
        for i in self.result:
            item = QListWidgetItem()
            item.setIcon(QIcon(i[0]))
            item.setText(i[1])
            self.list.addItem(item)

        self.list.itemDoubleClicked.connect(self.open_shablon)

    def open_shablon(self):
        real_result = self.result[self.sender().currentRow()]
        text = real_result[2]
        im = real_result[0]
        name = real_result[1]
        print(text)
        shab_txt_file = [i.strip() for i in open(text, 'r', encoding="utf-8").readlines()]
        # for i in shab_txt_file:
        #     print(i)
        print(shab_txt_file)
        self.shablon = ShablonPicture(im, shab_txt_file)
        self.shablon.show()
        self.setEnabled(True)


# class ShablonPicture(QWidget):
#     # shablon_value - список с каринкой, словарем текстов
#     def __init__(self, im, shablon_texts):
#         super().__init__()
#         uic.loadUi('UI\\generator_ui.ui', self)
#         self.image.setPixmap(QPixmap(im))
#         self.load_btn.setEnabled(False)
#         self.pushButton.setEnabled(True)
#         self.pushButton.clicked.connect(self.add_text)
#         self.listWidget.itemDoubleClicked.connect(self.open_parametrs)
#         self.texts = []
#         self.fname = im
#         self.pil_file = Image.open(im)
#         self.pil_file.thumbnail(IMAGE_ON_APP_SIZES)
#         self.reload_texts()
#
#     def add_text(self):
#         item = TextOnMem()
#         self.listWidget.addItem(str(TextOnMem()))
#         self.texts.append(item)
#         self.reload_texts()
#
#     def reload_texts(self):
#         self.pil_file = Image.open(self.fname)
#         self.pil_file.thumbnail(IMAGE_ON_APP_SIZES)
#         draw_pil_file = ImageDraw.Draw(self.pil_file)
#         for i in range(len(self.texts)):
#             txt = self.texts[i]
#             font = ImageFont.truetype(txt.font, txt.font_size)
#             draw_pil_file.text((txt.x, txt.y), str(txt), fill=txt.color, font=font)
#         # self.image.resize(*pil_file.size)
#         self.pil_file.save("redacting.png")
#
#         self.pixmap = QPixmap("redacting.png")
#         self.image.setPixmap(self.pixmap)
#
#     def open_parametrs(self):
#         self.parametrs = TextParametrs(self.sender().currentRow(), self.texts, self)
#         self.parametrs.show()
#         self.setEnabled(True)


class TextParametrs(QWidget):
    def __init__(self, sender_txt, texts, self_of_form):
        super().__init__()
        self.self_of_form = self_of_form
        self.sndr = texts[sender_txt]
        self.color = self.sndr.color
        self.x = self.sndr.x
        self.y = self.sndr.y
        self.text = self.sndr.text
        self.font_size = self.sndr.font_size
        self.font = self.sndr.font

        uic.loadUi('UI\\text_parametrs_ui.ui', self)
        # Устанавливаем значения не по умолчанию, ведь он мог редактироваться ранее
        # print(f"background-color: rgba({', '.join(list(str(i) for i in self.color))});")
        self.change_color.setStyleSheet(f"background-color: rgb({', '.join(list(str(i) for i in self.color))});"
                                        f"border-radius: 10px;")
        self.change_x.setValue(int(self.x))
        self.change_y.setValue(int(self.y))
        self.font_size_box.setValue(int(self.font_size))
        self.lineEdit.setText("I hate Yandex")

        self.change_color.clicked.connect(self.choise_color)
        self.change_x.valueChanged.connect(self.save)
        self.change_y.valueChanged.connect(self.save)
        self.lineEdit.textChanged.connect(self.save)

        self.font_size_box.valueChanged.connect(self.save)

    def choise_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.color = color.getRgb()
            # print(help(self.change_color.setStyleSheet))
            self.change_color.setStyleSheet(
                f"background-color: rgba({', '.join(list(str(i) for i in self.color))});"
                f"border-radius: 10px;")
        self.save()

    def save(self):
        self.sndr.color = self.color
        self.sndr.text = self.lineEdit.text()
        self.sndr.x = self.change_x.value()
        self.sndr.y = self.change_y.value()
        self.sndr.font_size = self.font_size_box.value()
        ShablonPicture.reload_texts(self.self_of_form)

    def choice_own_font(self):
        self.own_font_fname = QFileDialog.getOpenFileName(self, 'Выбрать шрифт', '')[0]
        self.txt_param_slf.font = self.own_font_fname