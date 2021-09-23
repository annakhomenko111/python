import sqlite3

base = sqlite3.connect('new.db')
cur = base.cursor()

base.execute('CREATE TABLE IF NOT EXISTS data (login PRIMARY KEY,password,address)')
base.commit()

cur.execute('INSERT INTO data VALUES (?, ?, ?)', ('Anna', '1234567', 'Kyiv'))
base.commit()
cur.execute('INSERT INTO data VALUES (?, ?, ?)', ('Mike', '1234567', 'New York'))
base.commit()
cur.execute('INSERT INTO data VALUES (?, ?, ?)', ('John', '1234567', 'Washington'))
base.commit()


# https://www.youtube.com/watch?v=siSRd4s7_ro