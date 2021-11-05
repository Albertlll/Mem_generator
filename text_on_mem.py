from constants import *


class TextOnMem:
    def __init__(self, x=0, y=0, text="I hate Yandex", color=(0, 0, 0), font=BASE_FONT, font_size=BASE_FONT_SIZE):
        self.x = x
        self.y = y
        self.text = text
        self.color = color
        self.font = font
        self.font_size = font_size

    def __str__(self):
        return self.text
