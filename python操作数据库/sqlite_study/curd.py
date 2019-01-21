from sqlite3 import connect
db_name = "test.db"
con = connect(db_name)
cur = con.cursor()
# cur.execute('CREATE TABLE star(id INTEGER,name TEXT, age INTEGER, address TEXT)')
rows = [(1,"王俊凯",16,"重庆"),(2,"王源",15,"重庆"),(3,"易烊千玺",15,"怀化")]
# for item in rows:
#     cur.execute('INSERT INTO star (id,name,age,address) VALUES (?,?,?,?)',item)
# cur.execute('SELECT * FROM star')
# for row in cur:
#     print(row)
#
# cur.execute('UPDATE star SET age=? WHERE id=?',(16,3))
#
# cur.execute('SELECT * FROM star')
# for row in cur:
#     print(row)
#
# cur.execute('DELETE FROM star where id=?',(3,))
# cur.execute('SELECT * FROM star')
# for row in cur:
#     print(row)


# cur.executemany('INSERT INTO star (id,name,age,address) VALUES (?,?,?,?)',rows)

cur.execute('SELECT * FROM star')

# r = cur.fetchone()
# print(r)
# r = cur.fetchmany(3)
# print(r)
r = cur.fetchmany()
print(r)
# r = cur.fetchall()
# print(r)

con.commit()
con.close()