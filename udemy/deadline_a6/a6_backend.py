import sqlite3 as sql


def connect():
    con=sql.connect("database6.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS datab (id INTEGER PRIMARY KEY, title TEXT, level INTEGER, subject TEXT, date REAL)")
    con.commit()
    con.close
    #
def insert(title,level,subject,date):
    con=sql.connect("database6.db")
    cur=con.cursor()
    cur.execute("INSERT INTO datab VALUES(NULL,?,?,?,?)",(title,level,subject,date))
    con.commit()
    con.close()
    #
def view():
    con=sql.connect("database6.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM datab")
    rows=cur.fetchall()
    con.close()
    return rows
    #
def search(title="",level="",subject="",date=""):
    con=sql.connect("database6.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM datab WHERE title=? OR level=? OR subject=? OR date=?",(title,level,subject,date))
    rows=cur.fetchall()
    con.close()
    return rows
    #
def delete(id):
    con=sql.connect("database6.db")
    cur=con.cursor()
    cur.execute("DELETE FROM datab WHERE id=?",(id,))
    con.commit()
    con.close()
    #
def update(id,title,level,subject,date):
    con=sql.connect("database6.db")
    cur=con.cursor()
    cur.execute("UPDATE datab SET title=?, level=?, subject=?, date=? WHERE id=?",(title,level,subject,date,id))
    con.commit()
    con.close()
    #

connect()
#if __name__=='__main__':
    #insert('algebre',3,'math',12.3)
    #insert('do rac',2,'maison',13.3)
    #insert('physie',1,'math',1.4)
    #insert('arbreTDTP',5,'math',19.3)
    #update(1,'detail',4,'physic',10.9)
    #print(view())
