import sqlite3


def add_row_to_recent(num):
    con = sqlite3.connect("БД\\shablons_DB.db")
    cur = con.cursor()
    cur.execute(f"""INSERT INTO recent('Картинка', 'Текста', 'Имя') 
                            VALUES ('Недавние\\{str(num)}\\{str(num)}.png',
                            'Недавние\\{str(num)}\\texts_on_mem.txt',
                            '{str(num)}')""")
    con.commit()


def get_answer_on_font(find_ask):
    con = sqlite3.connect("БД\\fonts_DB.sqlite")
    cur = con.cursor()
    return cur.execute(f"""SELECT * FROM fonts
                                WHERE Имя like '%{find_ask}%'""").fetchall()


def get_shablons(find_ask):
    con = sqlite3.connect("БД\\shablons_DB.db")
    cur = con.cursor()
    return cur.execute(f"""SELECT * FROM shablons
                            WHERE Имя like '%{find_ask}%'""").fetchall()


def get_all_recent():
    con = sqlite3.connect("БД\\shablons_DB.db")
    cur = con.cursor()
    return cur.execute(f"""SELECT * FROM recent""")
