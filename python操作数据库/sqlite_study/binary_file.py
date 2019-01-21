from sqlite3 import connect
db_name = 'test.db'
con = connect(db_name)
cur = con.cursor()
sql_script =  """
DROP TABLE IF EXISTS testa;
CREATE TABLE IF NOT EXISTS testa(id INTEGER ,data BlOB);
"""
cur.executescript(sql_script)
f = open('wall.jpg','rb')
cur.execute('INSERT INTO testa (id, data) VALUES (3,?)',(f.read(),))
f.close()
cur.execute('SELECT * FROM testa WHERE id=3')
record = cur.fetchone()
f = open('tt.jpg','wb')
f.write(record[1])
f.close()
con.commit()
con.close()