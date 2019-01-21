# from sqlite3 import connect, Row
# db_name = "test.db"
# con = connect(db_name)
# con.row_factory = Row
# cur = con.cursor()
# cur.execute('SELECT * from star')
# row = cur.fetchone()
# print(type(row))
# # print("以列名访问:", row['name'])
# print("以索引号访问", row[1]) # 第几列
# print("以迭代的方式访问:")
# for item in row:
#     print(item)
# print("len():",len(row))
#
# cur.close()
# con.commit()
# con.close()

from sqlite3 import Row, connect
db_name = 'test.db'
con = connect(db_name)
con.row_factory = Row
cur = con.cursor()
cur.execute('SELECT * FROM star')
# 设置row_factory之后, 再遍历就出对象了
# for row in cur:
#     print(row)
# 换用fetch方法
# row = cur.fetchone()
row = cur.fetchall()
# print(type(row))
# print("以列名访问: ", row['name'])
print("以索引号访问: ", row[1]['name'])
print("以迭代的方式访问")
for item in row:
    print(item)
print("len():", len(row))
cur.close()
con.commit()
con.close()

