import sqlite3 as sql

boglanish = sql.connect("fayll.db")

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



