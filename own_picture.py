import sys
from PyQt5.QtWidgets import QApplication, QFileDialog, QWidget, QColorDialog
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PIL import Image, ImageDraw, ImageFont
from font_list import FontsList
from text_on_mem import TextOnMem
from constants import *
from PyQt5.QtCore import Qt
import main_window
import text_parameters
import base_picture


class MyPicture(base_picture.BasePicture):
    def __init__(self):
        super().__init__()

    def keyPressEvent(self, event):
        if int(event.modifiers()) == Qt.ControlModifier:
            if event.key() == Qt.Key_E:
                if self.export_btn.isEnabled():
                    self.export()
            if event.key() == Qt.Key_A:
                if self.add_text_btn.isEnabled():
                    self.add_text()
            if event.key() == Qt.Key_L:
                if self.load_btn.isEnabled():
                    self.load_image()

    def closeEvent(self, event):
        self.main_form = main_window.MainForm()
        self.main_form.show()
        try:
            self.parametrs.close()
        except AttributeError:
            pass

