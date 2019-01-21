from sqlite3 import connect, Row
import binascii

db_name = "test.db"

class AbsSum:
    def __init__(self):
        self.s = 0

    def step(self, v):
        self.s += abs(v)

    def finalize(self):
        return self.s

con = connect(db_name)
con.create_aggregate('abssum', 1, AbsSum)
cur = con.cursor()
sql_script = """
DROP TABLE IF EXISTS testa;
CREATE TABLE IF NOT EXISTS testa(id INTEGER , name TEXT, score INTEGER);
INSERT INTO testa (id, name, score) VALUES (3, 'Lily',8);
INSERT INTO testa (id, name, score) VALUES (4, 'John',-7);
"""

cur.executescript(sql_script)
cur.execute('SELECT abssum(score) FROM testa')
for item in cur:
    print(item)
con.commit()
con.close()