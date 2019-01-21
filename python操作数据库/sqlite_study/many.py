# from sqlite3 import connect, Row
# db_name = "test.db"
# con = connect(db_name)
# con.row_factory = Row
# cur = con.cursor()
# rows = [(1,'Lily',12,"Beijing"),(6,"John",12,"ChongQing")]
# cur.executemany('INSERT INTO star(id, name, age, address) VALUES (?,?,?,?)',rows)
# cur.execute('SELECT * FROM star')
#
# for row in cur:
#     for r in row:
#         print(r)
# con.commit()
# con.close()


from sqlite3 import connect, Row
db_name = 'test.db'
con = connect(db_name)
con.row_factory = Row
cur = con.cursor()
rows = [
    (14, 'Lily', 12, 'Beijing'),
    (6, 'John', 13, 'ChongQing')
    ]
cur.executemany('INSERT INTO star (id, name, age, address) VALUES (?, ?, ?, ?)', rows)
cur.execute('SELECT * FROM star')
for row in cur:
    for r in row:
        print(r)
con.commit()
con.close()




