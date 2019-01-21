from pymysql import connect
db_name = {
    'host':'localhost',
    'port':3306,
    'user':'root',
    'database':'mysql_study',
    'charset':'utf8'
}
con = connect(**db_name)
cur = con.cursor()
row = (5, 'QingFeng', 'West Zone')
cur.execute('INSERT INTO genral_tab (card_id, name, address) VALUES (%s,%s,%s)',row)

cur.execute('SELECT * FROM genral_tab')
for row in cur:
    print(row)

print("修改数据")
cur.execute('UPDATE genral_tab SET address=%s WHERE card_id=%s',('East Zone',5))
# cur.execute('SELECT * FROM genral_tab WHERE card_id=5')
cur.execute('SELECT * FROM genral_tab WHERE card_id=%(card_id)s',{'card_id':5})
for row in cur:
    print(row)

print("删除数据")
cur.execute('DELETE FROM genral_tab WHERE card_id=5;')
cur.execute('SELECT * FROM genral_tab')
for row in cur:
    print(row)
con.close()