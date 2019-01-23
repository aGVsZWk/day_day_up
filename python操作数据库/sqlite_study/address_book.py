import sqlite3

import os


class MySqliteDb(object):
    """sqlite3 Db Class"""
    def __init__(self,dbname='address.db'):
        self.dbname = dbname
        self.con = None
        self.curs = None

    def getCursor(self):
        self.con = sqlite3.connect(self.dbname)
        if self.con:
            self.curs = self.con.cursor()

    def closeDb(self):
        if self.curs:
            self.curs.close()
        if self.con:
            self.con.commit()
            self.con.close()

    def __enter__(self):
        self.getCursor()
        return self.curs

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val:
            print('Exception has generate: ', exc_val)
            print('sqlite3 execute error!')
        self.closeDb()

def initDb():
    sql_script = """
    CREATE TABLE contact(
      id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
      name VARCHAR(20) not null,
      home_tel VARCHAR(20),
      office_tel VARCHAR(20),
      mobile_phone VARCHAR(20),
      memo text
    );
    CREATE TABLE mygroup(
      id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
      name VARCHAR(20) NOT NULL,
      memo TEXT
    );
    CREATE TABLE con_gro(
      cid INTEGER NOT NULL,
      gid INTEGER NOT NULL,
      FOREIGN KEY(cid) REFERENCES contact(id),
      FOREIGN KEY(gid) REFERENCES mygroup(id)
    );
    """

    if not os.path.exists('address.db'):
        with MySqliteDb() as db:
            db.executescript(sql_script)


class Contact:
    def __init__(self, name='', home_tel='', office_tel='', mobile_phone='', memo=''):
        self.id = -1
        self.name = name
        self.home_tel = home_tel
        self.office_tel = office_tel
        self.mobile_phone = mobile_phone
        self.memo = memo
        self.keys = ('home_tel','office_tel','mobile_phone','memo')
        self.__change()

    def save(self):
        if self.id == -1:
            params_dicts = {k:getattr(self,k) for k in self.keys if getattr(self,k)}
            keys =tuple(k for k in self.keys if k in params_dicts)
            quotes =','.join(('?' for i in range(len(params_dicts))))
            param_tuple = [self.name,]
            for key in keys:
                param_tuple.append(params_dicts[key])
            param_tuple = tuple(param_tuple)
            sql = 'INSERT INTO contact (name,%s) VALUES (?,%s)'%(','.join(keys),quotes)
            if self.name:
                try:
                    with MySqliteDb() as db:
                        db.execute(sql,param_tuple)
                        res = db.execute('SELECT id FROM contact WHERE name=?',(self.name,))
                        res = res.fetchone()
                        self.id = res[0]
                except:
                    print("保存失败, 请检查服务器! ")
            else:
                print('姓名不能为空')
                return False
        else:
            return self.update()

    def update(self):
        sql = 'UPDATE contact SET %s=? WHERE id=?'
        chgs = {k:getattr(self,k) for k in self.keys \
                if getattr(self,k) and getattr(self,k) != self.vals.get(k)}
        if not chgs:
            return
        try:
            with MySqliteDb() as db:
                for k,v in chgs.items:
                    db.execute(sql % k,(v,self.id))
            self.__change()
            return True
        except:
            print("更新失败! ")
            return False

    def load(self, id):
        try:
            with MySqliteDb() as db:
                res = db.execute('SELECT * FROM contact WHERE id=?',(id,))
                res = res.fetchone()
                self.name = res[1]
                self.id = id
                for i,v in enumerate(res[2:]):
                    setattr(self,self.keys[i-2],v)
            self.__change()
            return True
        except:
            print("加载数据失败! ")

    def load_from_name(self):
        if self.name:
            try:
                with MySqliteDb() as db:
                    res = db.execute('SELECT * FROM contact WHERE name=?',(self.name,))
                    res = res.fetchone()
                    self.id = res[0]
                    for i, v in enumerate(res[2:]):
                        setattr(self, self.keys[i-2], v)
                self.__change()
                return True
            except:
                print("数据载入失败! ")

    def get_by_name(self, name):
        try:
            with MySqliteDb() as db:
                res = db.execute('SELECT * FROM contact WHERE name=?',(name,))
                res = res.fetchall()
            return res
        except:
            print("数据查询失败! ")

    def delete(self):
        try:
            with MySqliteDb() as db:
                db.execute('DELETE FROM contact WHERE id=?', (self.id,))
                db.execute('DELETE FROM contact WHERE cid=?', (self.id))
            return True
        except:
            print("数据查询失败")

    def all(self):
        try:
            with MySqliteDb() as db:
                res = db.execute('SELECT * FROM contact')
                res = res.fetchall()
            return res
        except:
            print("数据查询失败")

    def add_to_group(self,gid):
        try:
            with MySqliteDb() as db:
                db.execute('INSERT INTO con_gro (cid, gid) VALUES(?,?)',(self.id, gid))
            return True
        except:
            print("数据查询失败! ")

    def __change(self):
        self.vals = {k:getattr(self,k) for k in self.keys}

class Group:
    def __init__(self, name='', memo=''):
        self.id = -1
        self.name = name
        self.memo = memo
        self.contacts = []

    def save(self):
        if self.name and self.id == -1:
            try:
                with MySqliteDb() as db:
                    db.execute('INSERT INTO mygroup (name, memo) VALUES (?,?)',(self.name, self.memo))

                    res = db.execute('SELECT id from mygroup where name=?',(self.name,))
                    self.id = res.fetchone()[0]
                return True
            except:
                print("数据查询失败")
        if self.name and self.id != -1:
            return self.update()

    def update(self):
        try:
            with MySqliteDb() as db:
                db.exectue('UPDATE mygroup SET name=?, memo=? WHERE id=?',(self.name, self.memo, self.id))
                return True
        except:
            print("数据更新失败! ")

    def load(self, id):
        try:
            with MySqliteDb() as db:
                db.exectue('SELECT * FROM mygroup where id = ?',(id,))
                res = db.fetchone()
                self.id = id
                self.name = res[1]
                self.memo = res[2]
                return True
        except:
            pass

    def delete(self):
        if self.id != -1:
            try:
                with MySqliteDb() as db:
                    db.exectue('DELETE FROM mygroup where id=?',(self.id,))
                    db.execute('DELETE FROM con_gro WHERE gid=?',(self.id,))

                    return True
            except:
                print("数据删除失败")

    def load_from_name(self):
        if self.name:
            try:
                with MySqliteDb() as db:
                    res = db.execute('SELECT * FROM mygroup WHERE name=?', (self.name,))
                    res = res.fetchone()
                    self.id = res[0]
                    self.memo = res[2]
                return True
            except:
                print("数据删除失败")


    def all(self):
        try:
            with MySqliteDb() as db:
                res = db.execute('SELECT * FROM mygroup')
                res = res.fetchall()
            return res
        except:
            print("数据查询失败")

    def add_contact(self, cid):
        if cid and self.id != -1:
            try:
                with MySqliteDb() as db:
                    res = db.execute('INSERT INTO con_gro (cid, gid) VALUES (?,?)',(cid, self.id))
                return True
            except:
                print("数据添加失败")

    def del_contact(self, cid):
        try:
            with MySqliteDb() as db:
                db.execute('DELETE FROM con_gro where cid=? and gid=?', (cid, self.id))
            return True
        except:
            pass

    def all_contacts(self):
        if self.id != -1:
            try:
                with MySqliteDb() as db:
                    cts = []
                    cids = db.execute('SELECT cid FROM con_gro WHERE gid=?',(self.id, ))
                    cids = cids.fetchall()
                    for cid in cids:
                        c = Contact()
                        print(cid[0])
                        c.load(cid[0])
                        cts.append(c)
                return cts
            except:
                print("数据查询失败")

def info():
    sqls = [
        'SELECT * FROM contact',
        'SELECT * FROM mygroup',
        'SELECT * FROM con_gro',
    ]
    try:
        with MySqliteDb() as db:
            for sql in sqls:
                res = db.execute(sql)
                res = res.fetchall()
                for r in res:
                    print(r)
    except:
        print("数据查询失败! ")

if __name__ == '__main__':
    cts = [
        {'name':'Lily', 'home_tel':'0551-987654321', 'memo':'安徽'},
        {'name':'Bob', 'office_tel':'0551-987654321', 'memo':'上海'},
        {'name':'Mike', 'mobile_phone':'13838389438',},
        {'name':'John', 'home_tel':'010-987654321', 'memo':'北京'}
    ]

    gps = [
        {'name':"朋友"},
        {'name':"家人"},
        {'name':"学生"},
    ]
    print('初始化数据库')
    initDb()
    print('插入数据')
    for ct in cts:
        Contact(**ct).save()

    for gp in gps:
        Group(**gp).save()
    info()

    print("查询联系人, 并添加到组2")
    ct = Contact(name='Lily')
    ct.load_from_name()
    print(ct.id, ct.name)
    ct.add_to_group(2)
    #
    cta = Contact()
    cta.load(1)
    print(cta.id, cta.name)
    cta.add_to_group(1)

    ctb = Contact()
    ctb.load(3)
    print(ctb.id, ctb.name)
    ctb.add_to_group(2)
    #
    ctb = Contact()
    ctb.load(5) # 不存在, 不能将它添加到组
    # print(ctb.id, ctb.name)
    # ctb.add_to_group(2)
    #
    print("查询所有联系人: ")
    for r in Contact().all():
        print(r)
    # #
    print("查询所有组: ")
    for r in Group().all():
        print(r)
    # #
    print("查询指定组的成员: ")
    gp = Group(name='家人')
    gp.load_from_name()
    print(gp.id, gp.name)

    print("通过组添加成员: ")
    gp.add_contact(3)

    cts = gp.all_contacts()

    for ct in cts:
        print(ct.id, ct.name)

