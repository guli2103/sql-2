import sqlite3 as sql

boglanish = sql.connect("fayl1.db")

malumot = boglanish.cursor()

malumot.execute('''
CREATE TABLE IF NOT EXISTS Poytaxti(
    Toshkent TEXT
    Vashington TEXT
    Moskva TEXT
    Pekin TEXT
)''')

malumot.execute('''
CREATE TABLE IF NOT EXISTS Aholisi(
    ozbekiston aholisi INTEGER
    aqsh aholisi INTEGER
    rossiya aholisi INTEGER
    xitoy aholisi INTEGER
)
''')