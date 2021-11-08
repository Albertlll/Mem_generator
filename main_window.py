from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
import shablons_list
import own_picture
import recent_list
from main_ui import Ui_MainWindow


class MainForm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.open_shablon_list_btn.clicked.connect(self.open_shablons_form)
        self.open_own_picture_btn.clicked.connect(self.open_my_picture_form)
        self.open_recent_list_btn.clicked.connect(self.open_recent_form)

    def open_shablons_form(self):
        self.hide()
        self.shablon_list = shablons_list.ShablonsList()
        self.shablon_list.show()

    def open_my_picture_form(self):
        self.hide()
        self.my_picture_form = own_picture.MyPicture()
        self.my_picture_form.show()

    def open_recent_form(self):
        self.hide()
        self.recent_list = recent_list.RecentList()
        self.recent_list.show()
