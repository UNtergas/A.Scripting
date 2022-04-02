import sqlite3 as sql

con=sql.connect("ex_data.db")
cur=con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS store(item TEXT, quantity INTERGER, price REAL)")
con.commit()
con.close()