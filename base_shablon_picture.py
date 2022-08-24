from PyQt5.QtGui import QPixmap, QColor, QIcon
from PIL import Image, ImageDraw, ImageFont
from font_list import FontsList
from text_on_mem import TextOnMem
from constants import *
from PyQt5.QtCore import Qt
import text_parameters
import base_picture
import shablons_list


class BaseShablonPicture(base_picture.BasePicture):
    def __init__(self, im, shablon_texts):
        super().__init__()
        self.shablon_texts = shablon_texts
        self.image.setPixmap(QPixmap(im))
        self.load_btn.setEnabled(False)
        self.add_text_btn.setEnabled(True)
        self.export_btn.setEnabled(True)
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
            if event.key() == Qt.Key_Delete:
                if self.add_text_btn.isEnabled():
                    self.del_text()

    def add_begin_text(self):
        n_of_texts = int(self.shablon_texts[0])
        ind_in_shab_list = 0
        # Распаковка значений из файла текстов
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
