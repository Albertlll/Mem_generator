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
# QSpinBox.changeEvent()
from constants import *


class MyPicture(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI\\generator_ui.ui', self)
        self.pushButton.clicked.connect(self.add_text)
        self.load_btn.clicked.connect(self.load_image)
        self.listWidget.itemDoubleClicked.connect(self.open_parametrs)
        self.texts = []
        self.pushButton_2.clicked.connect(self.export)

    def export(self):
        name = QFileDialog.getSaveFileName(self, 'Save File', '', "Картинка (*.jpg);;Картинка (*.png)")[0]
        if not name:
            return None
        save_file = open(name, 'wb')
        im_file = open("redacting.png", "rb")
        save_file.write(im_file.read())
        save_file.close()
    
    def add_text(self):
        item = TextOnMem()
        self.listWidget.addItem(str(TextOnMem()))
        self.texts.append(item)
        self.reload_texts()

    def load_image(self):
        self.fname = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '', 'JPG(*.jpg);;PNG(*.png)')[0]
        if not self.fname:
            return None
        self.pil_file = Image.open(self.fname)
        self.pil_file.thumbnail(IMAGE_ON_APP_SIZES)
        self.reload_texts()
        self.pushButton.setEnabled(True)
        self.load_btn.setEnabled(False)

    def reload_texts(self):
        self.pil_file = Image.open(self.fname)
        self.pil_file.thumbnail(IMAGE_ON_APP_SIZES)
        draw_pil_file = ImageDraw.Draw(self.pil_file)
        for i in range(len(self.texts)):
            txt = self.texts[i]
            self.listWidget.item(i).setText(str(txt))

            font = ImageFont.truetype(txt.font, txt.font_size)
            print(txt.color)
            draw_pil_file.text((txt.x, txt.y), str(txt), fill=txt.color, font=font)
        # self.image.resize(*pil_file.size)
        self.pil_file.save("redacting.png")
        self.pixmap = QPixmap("redacting.png")
        self.image.setPixmap(self.pixmap)

    def open_parametrs(self):
        self.parametrs = TextParametrs(self.sender().currentRow(), self.texts, self)
        self.parametrs.show()
        self.setEnabled(True)


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
        self.lineEdit.setText(self.text)

        self.change_color.clicked.connect(self.choice_color)
        self.change_x.valueChanged.connect(self.save)
        self.change_y.valueChanged.connect(self.save)
        self.lineEdit.textChanged.connect(self.save)

        self.select_own_font_btn.clicked.connect(self.choice_own_font)
        self.select_self_font_btn.clicked.connect(self.choice_not_own_font)

        self.font_size_box.valueChanged.connect(self.save)

    def choice_color(self):
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
        MyPicture.reload_texts(self.self_of_form)

    def choice_own_font(self):
        self.own_font_fname = QFileDialog.getOpenFileName(self, 'Выбрать шрифт', '')[0]
        self.sndr.font = self.own_font_fname
        self.save()

    def choice_not_own_font(self):
        self.parametrs = FontsList(self)
        self.parametrs.show()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyPicture()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
