import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
from shablons_list import ShablonsList
from mem_gen_tests import MyPicture


class MainForm(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main_ui.ui', self)
        self.pushButton_2.clicked.connect(self.open_shablons_form)
        self.pushButton.clicked.connect(self.open_my_picture_form)

    def open_shablons_form(self):
        self.hide()
        self.shablon_list = ShablonsList()
        self.shablon_list.show()

    def open_my_picture_form(self):
        self.hide()
        self.my_picture_form = MyPicture()
        self.my_picture_form.show()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MainForm()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
