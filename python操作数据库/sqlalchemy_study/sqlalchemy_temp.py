import pymysql
pymysql.install_as_MySQLdb()
# 默认情况下, sqlalchemy使用mysqldb连接数据库, python2中会安装mysqldb的包, python3中不会安装, 可安装pymysql, 里面切成mysqldb()


from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey
DB_CONNECT_STRING = "mysql://root:mysql@127.0.0.1:3306/sqlalchemy_study"
engine = create_engine(DB_CONNECT_STRING, echo=True)
# engine = create_engine(DB_CONNECT_STRING, echo=True) # echo=True, 打印调试信息
metadata = MetaData(engine) # 创建 MetaData 时绑定了引擎


# print(metadata)
# user_table = Table('user', metadata,
#                        Column('id', Integer, primary_key=Table),
#                        Column('name', String(50)),
#                        Column('fullname', String(100))
#                     )
#
# address_table = Table('address', metadata,
#                       Column('id', Integer, primary_key=Table),
#                       Column('user_id', None, ForeignKey('user.id')),
#                       Column('email', String(128), nullable=False)
#                       )
#


# metadata.create_all()   # 会自动检查表是否存在
# 若创建metadata时不传入engine, 此处应该写成metadata.create_all(engine)


# 除了metadata.create_all()外, Table自己也有create方法:
# Table对象.create(bind=引擎, checkfirst=False)

# user_table.create(checkfirst=False)     # bind参数一般指引擎,绑定Metadata对象可忽略 checkfirst为True时, 如果表存在, 不报错, 什么也不做; 为False时会引发异常
# address_table.create(checkfirst=False)








# 导入表, 表已经存在, 不再创建表了, 使用参数autoload=True
user_table = Table('user', metadata, autoload=True)
# print('user' in metadata.tables)    # 查看是否导入成功, True
# print('address' in metadata.tables) # False
# print([c.name for c in user_table.columns]) # 查看列的名字


# 反射功能, 如果被反射的表外键引用了另一个表, 那么被引用的表也会一并被反射. 比如只反射address表, user表也一并被反射了
address_table = Table('address', metadata, autoload=True)
# print('user' in metadata.tables)    # True











# 插入数据
# 插入数据之前, 必须要有表对象, 不管是新创建的还是通过反射导入的
# ins = user_table.insert()   # 返回Insert对象所对应的sql语句
# print(ins)
# ins = ins.values(id="1",name='zhangsan',fullname='nigulasiZhangSan')



# 执行插入数据
# conn = engine.connect()
# result = conn.execute(ins)


# 执行多条语句
# 把参数通过execute()方法传进去
ins = user_table.insert()
conn = engine.connect()
# conn.execute(ins, name="zhangsan", fullname="nigulasi zhaosi")
# 一次插入多条记录, 传入一个字典列表(每个字典的键必须一致)给execute()即可
# conn.execute(address_table.insert(),[
#     {'user_id':1, "email": "sprinfall@gmail.com"},
#     {'user_id':1, "email": "sprinfall@hotmail.com"},
#     ])



# 查询数据
cur = conn.execute('select * from address;')
res = cur.fetchall()
print(res)