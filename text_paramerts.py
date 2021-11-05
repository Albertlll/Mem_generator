# from imports import *
#
#
# class TextParametrs(QWidget):
#     def __init__(self, sender_txt, texts, self_of_form):
#         super().__init__()
#         self.self_of_form = self_of_form
#         self.sndr = texts[sender_txt]
#         self.color = self.sndr.color
#         self.x = self.sndr.x
#         self.y = self.sndr.y
#         self.text = self.sndr.text
#         self.font_size = self.sndr.font_size
#         self.font = self.sndr.font
#
#         uic.loadUi('UI\\text_parametrs_ui.ui', self)
#         # Устанавливаем значения не по умолчанию, ведь он мог редактироваться ранее
#         # print(f"background-color: rgba({', '.join(list(str(i) for i in self.color))});")
#         self.change_color.setStyleSheet(f"background-color: rgb({', '.join(list(str(i) for i in self.color))});"
#                                         f"border-radius: 10px;")
#         self.change_x.setValue(int(self.x))
#         self.change_y.setValue(int(self.y))
#         self.font_size_box.setValue(int(self.font_size))
#         self.lineEdit.setText(self.text)
#
#         self.change_color.clicked.connect(self.choice_color)
#         self.change_x.valueChanged.connect(self.save)
#         self.change_y.valueChanged.connect(self.save)
#         self.lineEdit.textChanged.connect(self.save)
#
#         self.select_own_font_btn.clicked.connect(self.choice_own_font)
#         self.select_self_font_btn.clicked.connect(self.choice_not_own_font)
#
#         self.font_size_box.valueChanged.connect(self.save)
#
#     def choice_color(self):
#         color = QColorDialog.getColor()
#         if color.isValid():
#             self.color = color.getRgb()
#             # print(help(self.change_color.setStyleSheet))
#             self.change_color.setStyleSheet(
#                 f"background-color: rgba({', '.join(list(str(i) for i in self.color))});"
#                 f"border-radius: 10px;")
#         self.save()
#
#     def save(self):
#         self.sndr.color = self.color
#         self.sndr.text = self.lineEdit.text()
#         self.sndr.x = self.change_x.value()
#         self.sndr.y = self.change_y.value()
#         self.sndr.font_size = self.font_size_box.value()
#         MyPicture.reload_texts(self.self_of_form)
#
#     def choice_own_font(self):
#         self.own_font_fname = QFileDialog.getOpenFileName(self, 'Выбрать шрифт', '')[0]
#         self.sndr.font = self.own_font_fname
#         self.save()
#
#     def choice_not_own_font(self):
#         self.parametrs = FontsList(self)
#         self.parametrs.show()
