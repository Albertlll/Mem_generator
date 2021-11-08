import os
import pprint
from PIL import Image, ImageDraw, ImageFont
import sqlite3

con = sqlite3.connect("БД\\shablons_DB.db")
cur = con.cursor()

for i in os.listdir("shablons_images"):
    if i[-4:] == ".jpg" or i[:-4] == "arm_to_face" or i[:-4] == "cool_spanch":
        continue
    file = open(f'shablons_images\\{i}\\texts_on_mem.txt', mode="w", encoding="utf-8")
    lst = ['2', '10', '10', 'Тут может быть', '0 0 0', 'Impact Regular.ttf', '20', '10', '30', 'ваш текст',
           '0 0 0', 'Impact Regular.ttf', '20']
    file.write("\n".join(lst))

# con.commit()
# print(open("shablons_images\\больно\\texts_on_mem.txt", 'r', encoding="utf-8"))
# print("shablons_images\\больно\\text_on_mem.txt")
# print(open("shablons_images/больно/texts_on_mem.txt"))
# print([i.strip() for i in open("shablons_images\\Баз Лайтер\\texts_on_mem.txt", encoding="utf-8").readlines()])


