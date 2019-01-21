from sqlite3 import connect,Row
import binascii

db_name = 'test.db'

def encrypt(mydata):
    crc = str(binascii.crc32(mydata.encode()))
    while len(crc) < 10:
        crc = '0' + crc
    return mydata + crc

def check(mydata):
    if len(mydata) < 11:
        return None
    crc_res = str(binascii.crc32(mydata[:-10].encode()))
    while len(crc_res) < 10:
        crc_res = '0' + crc_res
    if crc_res == mydata[-10:]:
        return mydata[:-10]

con = connect(db_name)
con.create_function('checkk',1,check)
cur = con.cursor()
sql_script = """
DROP TABLE if EXISTS testa;
CREATE TABLE IF NOT EXISTS testa(id INTEGER ,name text);
INSERT INTO testa (id, name) values (3, "%s");
INSERT INTO testa (id, name) values (4, "%s");
"""
names = ['Lily', 'Green']
names = tuple(encrypt(i) for i in names)
sql_script = sql_script % names
print(sql_script)
cur.executescript(sql_script)
cur.execute('SELECT id, checkk(name) FROM testa')
for item in cur:
    print(item)
cur.execute('UPDATE testa SET name=? WHERE id=?',('hahahah1324512342', 4,))
cur.execute('SELECT id, checkk(name) from testa')
for item in cur:
    print(item)
con.commit()
con.close()

