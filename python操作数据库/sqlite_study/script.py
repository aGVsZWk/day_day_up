from sqlite3 import connect
db_name = 'testb.db'
con = connect(db_name)
cur = con.cursor()
sql_str = """
CREATE TABLE test (id INTEGER ,name test);
INSERT INTO test (id, name) VALUES (1, 'Lily');
INSERT INTO test (id, name) VALUES (2, 'Green')
"""
cur.executescript(sql_str)
cur.execute('SELECT * FROM test')
for item in cur:
    print(item)
cur.close()
con.commit()
con.close()