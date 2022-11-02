import sqlite3 as sql

boglanish = sql.connect("fayl3.db")

malumot = boglanish.cursor()

malumot.execute('''
CREATE TABLE IF NOT EXISTS Gullar(
    lola TEXT
    atirgul TEXT
    moychechak TEXT
    binafsha TEXT
)''')

malumot.execute('''
CREATE TABLE IF NOT EXISTS Rangi(
    rozviy TEXT
    qizil TEXT
    oq TEXT
    binafsh TEXT
)''')

malumot.execute('''
CREATE TABLE IF NOT EXISTS Soni(
    lolaning soni INTEGER
    atirgulning soni INTEGER
    moychechakning soni INTEGER
    binafshaning soni INTEGER
)''')