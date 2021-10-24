import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QListWidgetItem, QWidget
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PIL import Image, ImageDraw

IMAGE_ON_APP_SIZES = (500, 500)


class TextOnMem:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.text = "I hate Yandex"
        self.color = (0, 0, 0)
        self.font = ""

    def setx(self, x):
        self.x = x

    def getx(self):
        return self.x

    def sety(self, y):
        self.y = y

    def gety(self):
        return self.y

    def settext(self, text):
        self.text = text

    def setfont(self, font):
        self.font = font

    def getcolor(self):
        return self.color

    def __str__(self):
        return self.text


class MyPicture(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('generator_ui.ui', self)
        self.pushButton.clicked.connect(self.add_text)
        self.load_btn.clicked.connect(self.load_image)
        self.listWidget.itemDoubleClicked.connect(self.open_parametrs)
        self.texts = []
    
    def add_text(self):
        item = TextOnMem()
        self.listWidget.addItem(str(TextOnMem()))
        self.texts.append(item)
        self.reload_texts()

    def load_image(self):
        fname = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')[0]
        self.pil_file = Image.open(fname)
        self.pil_file.thumbnail(IMAGE_ON_APP_SIZES)

        self.reload_texts()
        self.pushButton.setEnabled(True)
        self.load_btn.setEnabled(False)

    def reload_texts(self):
        draw_pil_file = ImageDraw.Draw(self.pil_file)
        for i in range(len(self.texts)):
            txt = self.texts[i]
            draw_pil_file.text((txt.x, txt.y), str(txt), fill=txt.color)
        # self.image.resize(*pil_file.size)
        self.pil_file.save("redacting.png")

        self.pixmap = QPixmap("redacting.png")
        self.image.setPixmap(self.pixmap)

    def open_parametrs(self):
        self.parametrs = TextParametrs()
        self.parametrs.show()
        self.setEnabled(True)


class TextParametrs(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('text_parametrs_ui.ui', self)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MainForm()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
