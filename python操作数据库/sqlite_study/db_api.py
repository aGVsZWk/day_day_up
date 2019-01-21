# encoding=utf-8;
from db_set import *
sql_string_dict = {
    "create":"CREATE TABLE genral_tab (card_id INTEGER , name text, address text)",
    "insert":[
        "INSERT INTO genral_tab (card_id,name,address) VALUES(1,'LiMing','East Zone')",
        "INSERT INTO genral_tab (card_id,name,address) VALUES(2,'WangMing','West Zone')",
        "INSERT INTO genral_tab (card_id,name,address) VALUES(3,'ZhaoMing','South Zone')",
        "INSERT INTO genral_tab (card_id,name,address) VALUES(4,'DingMing','North Zone')",
        ],
    "select":"SELECT * FROM genral_tab",
    "update":"UPDATE genral_tab SET name='QianMing' WHERE card_id=4",
    "delete":"DELETE FROM genral_tab WHERE card_id=3"

}

con = connect(db_name)
cur = con.cursor()

print("Create Table:\n")
cur.execute(sql_string_dict['create'])

print("Insert Data:\n")
print('(1,"LiMing","East Zone")')
print('(2,"WangMing","West Zone")')
print('(3,"ZhaoMing","South Zone")')
print('(4,"DingMing","North Zone")')
for sql in sql_string_dict['insert']:
    cur.execute(sql)
print()

print("All Records:")
cur.execute(sql_string_dict['select'])
for row in cur:
    print(row)
print()

print("After Updated")
cur.execute(sql_string_dict['select'])
for row in cur:
    print(row)
print()

print("After delete")
cur.execute(sql_string_dict['delete'])
cur.execute(sql_string_dict['select'])
for row in cur:
    print(row)

con.commit()
con.close()