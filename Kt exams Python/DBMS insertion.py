import sqlite3 as db
con=db.connect("Inter database.db")
cur=con.cursor()
cur.execute("insert into Item values(101,Geometry_Box,100,0,25")
cur.execute("insert into Item values(102,Soap,100,0,50")
cur.execute("insert into Item values(103,Perfume,100,0,25")
cur.execute("insert into Item values(104,Pen,50,0,200")
cur.execute("insert into Item values(105,Pencil,20,0,100")
cur.execute("select * from Item")
print(cur.fetchall())
cur.close()
con.commit()
