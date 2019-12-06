import sqlite3 as db
con=db.connect("Item Database.db")
cur=con.cursor()
cur.execute("create table item (Itemno integer, name text, price float, quantity integer)")
print("Table created successfully")
cur.close()
con.commit()
