import sqlite3 as sql

def createtable():
    con=sql.connect("udemy//ex_data.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store(item TEXT, quantity INTERGER, price REAL)")
    con.commit()
    con.close()
    #
def insert(item,quantity,price):
    con=sql.connect("udemy//ex_data.db")
    cur=con.cursor()
    cur.execute("INSERT INTO store VALUES(?,?,?)",(item,quantity,price))
    con.commit()
    con.close()
    #
def viewtable():
    con=sql.connect("udemy//ex_data.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    con.close()
    return rows
    #
def deleteitem(item):
    con=sql.connect("udemy//ex_data.db")
    cur=con.cursor()
    cur.execute("DELETE FROM store WHERE item=?",(item,))
    con.commit()
    con.close()
    #
def update(quantity,price,item):
    con=sql.connect("udemy//ex_data.db")
    cur=con.cursor()
    cur.execute("UPDATE store SET quantity=?,price=? WHERE item=?",(quantity,price,item))
    con.commit()
    con.close()
    #
createtable()
#insert("wine ",5,10.5)
#insert("coffee",5,6)
#insert("water",20,6)
#deleteitem("water")
#update(8,12,"water")
print(viewtable())