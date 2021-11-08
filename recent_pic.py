from PyQt5.QtGui import QPixmap, QColor, QIcon
from PIL import Image, ImageDraw, ImageFont
from font_list import FontsList
from text_on_mem import TextOnMem
from constants import *
from PyQt5.QtCore import Qt
import text_parameters
import base_picture
import shablon_picture
import shablons_list
import main_window
import base_shablon_picture


class RecentPicture(base_shablon_picture.BaseShablonPicture):
    def __init__(self, im, shablon_texts):
        super().__init__(im, shablon_texts)

    def closeEvent(self, event):
        self.main_form = main_window.MainForm()
        self.main_form.show()
