import sqlite3 as sql

boglanish = sql.connect("fayl.db")

malumot = boglanish.cursor()

malumot.execute('''
CREATE TABLE IF NOT EXISTS Davaltalar(
    ozbekiston TEXT
    aqsh TEXT
    rossiya TEXT
    xitoy TEXT
)''')

malumot.execute('''
CREATE TABLE IF NOT EXISTS Prezidenti(
    Shavkat Miromonovich Mirziyoyev TEXT
    Joe Biden TEXT
    Vlademir Putin TEXT
    Shi Jinpin TEXT
)''')

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

malumot.execute('''
CREATE TABLE IF NOT EXISTS Maydoni(
    ozbekiston maydoni INTEGER
    aqsh maydoni INTEGER
    rossiya maydoni INTEGER
    xitoy maydoni INTEGER
)''')