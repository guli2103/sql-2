import sqlite3 as sql

boglanish = sql.connect("fayl2.db")

malumot = boglanish.cursor()

malumot.execute('''
CREATE TABLE IF NOT EXISTS Maydoni(
    ozbekiston maydoni INTEGER
    aqsh maydoni INTEGER
    rossiya maydoni INTEGER
    xitoy maydoni INTEGER
)''')

malumot.execute('''
CREATE TABLE IF NOT EXISTS Tili(
    ozbek TEXT
    inglish TEXT
    rus TEXT
    tibet TEXT
)''')