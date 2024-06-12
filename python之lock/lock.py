import pymysql
from concurrent.futures import ThreadPoolExecutor
from threading import current_thread
import threading
import random
import redis
import uuid
import time


class Db(object):
    def __init__(self, host=None, username=None, pwd=None, dbname=None):
        self.pool = {}
        self.host = host
        self.username = username
        self.pwd = pwd
        self.dbname = dbname

    def get_instance(self):
        name = current_thread().name
        if name not in self.pool:
            conn = pymysql.connect(self.host, self.username, self.pwd, self.dbname)
            self.pool[name] = conn
        return self.pool[name]


class RedisClient(object):
    def __init__(self, host=None, port=6379, pwd=None, db=10):
        self.host = host
        self.port = port
        self.pwd = pwd
        self.db = db
        self.redis_client = redis.Redis(host=host, port=port, password=pwd, db=db)

    def acquire_lock(self, lock_name, acquire_time=10, time_out=10):
        indentifier = str(uuid.uuid4())
        end = time.time() + acquire_time
        lock = "string:lock:" + lock_name
        while time.time() < end:
            if self.redis_client.set(lock, indentifier, ex=time_out, nx=True):
                return indentifier
            time.sleep(0.01)
        return False

    def release_lock(self, lock_name, identifier):
        lock = "string:lock:" + lock_name
        pip = self.redis_client.pipeline(True)
        while True:
            try:
                pip.watch(lock)
                lock_value = self.redis_client.get(lock)
                if not lock_value:
                    return True
                if lock_value.decode() == identifier:
                    pip.multi()
                    pip.delete(lock)
                    pip.execute()
                    return True
                pip.unwatch()
                break
            except redis.exceptions.WatchError:
                print("redis watch error")
        return False




class Test(object):
    def __init__(self):
        self.max_id = 10000
        self.start_id = 1
        self.db = Db('localhost', 'root', '123456', 'test')
        self.redis = RedisClient('127.0.0.1')
        self.lock = threading.Lock()
        self.main()

    def main(self):
        threads = []
        # func = self.insert_func
        # func = self.insert_func2
        # func = self.update_func
        # func = self.update_for_func
        # func = self.update_happy_lock
        func = self.redis_lock_func
        for i in range(100):
            t = threading.Thread(target=func)
            # if i == 80:
            #     time.sleep(10)
            t.start()
            threads.append(t)
        for t in threads:
            t.join()

    def insert_func(self):
        db = self.db.get_instance()
        cursor = db.cursor()
        while True:
            if self.start_id >= self.max_id:
                break
            s = self.start_id
            with self.lock:
                self.start_id += 50
                if self.start_id > self.max_id:
                    self.start_id = self.max_id
            e = self.start_id
            # create table archives(id int unsigned not null auto_increment primary key);
            for i in range(s, e):
                sql = "insert into archives(id) values(%s)"
                params = (i, )
                try:
                    cursor.execute(sql, params)
                    db.commit()
                    print(current_thread().name, ":", sql, params, ":success")
                except:
                    db.rollback()
                    print(current_thread().name, ":", sql, params, ":failed")
                    raise

    def insert_func2(self):
        db = self.db.get_instance()
        cursor = db.cursor()
        while True:
            if self.start_id >= self.max_id:
                cursor.close()
                break
            s = self.start_id
            with self.lock:
                self.start_id += 50
                if self.start_id > self.max_id:
                    self.start_id = self.max_id
            e = self.start_id
            # create table archives(id int unsigned not null auto_increment primary key);
            for i in range(s, e):
                sql = "insert into archives2(id, group_id) values(%s, %s)"
                params = (i, random.randint(0, 50))
                try:
                    cursor.execute(sql, params)
                    db.commit()
                    print(current_thread().name, ":", sql, params, ":success")
                except:
                    db.rollback()
                    print(current_thread().name, ":", sql, params, ":failed")
                    raise

    def update_func(self):
        db = self.db.get_instance()
        cursor = db.cursor()
        while True:
            sql = "select a.id,a.status, a.group_id from archives2 a where a.status=0 and not exists(select 1 from archives2 b where b.group_id=a.group_id and b.status!=0) order by rand() limit 1"
            params = ()
            try:
                cursor.execute(sql)
                data = cursor.fetchone()
                if not data:
                    cursor.close()
                    break
                id, _, _ = data
                sql = "update archives2 set status=1 where id=%s"
                params = (id, )
                cursor.execute(sql, params)
                db.commit()
                print(current_thread().name, ":", sql, params, ":success")
            except:
                db.rollback()
                print(current_thread().name, ":", sql, params, ":failed")
                raise

    def update_for_func(self):
        db = self.db.get_instance()
        while True:
            cursor = db.cursor()
            sql = "select a.id,a.status, a.group_id from archives2 a where a.status=0 and not exists(select 1 from archives2 b where b.group_id=a.group_id and b.status!=0) order by rand() limit 1 for update"
            params = ()
            try:
                cursor.execute(sql)
                data = cursor.fetchone()
                print(data)
                if not data:
                    db.commit()
                    break
                id, _, _ = data
                sql = "update archives2 set status=1 where id=%s"
                params = (id, )
                cursor.execute(sql, params)
                db.commit()
                print(current_thread().name, ":", sql, params, ":success")
            except:
                db.rollback()
                print(current_thread().name, ":", sql, params, ":failed")
                raise
            finally:
                cursor.close()
        db.close()

    def update_happy_lock(self):
        db = self.db.get_instance()
        i = 0
        while i<100:
            cursor = db.cursor()
            name = current_thread().name + str('-') + str(i)
            sql = "update archives3 set owner=%s, version=version+1 where version=0 limit 1"
            params = (name, )
            try:
                cursor.execute(sql, params)
                db.commit()
                print(current_thread().name, ":", sql, params, ":success")
            except:
                db.rollback()
                print(current_thread().name, ":", sql, params, ":failed")
                raise
            finally:
                cursor.close()
                i += 1
        db.close()

    def redis_lock_func(self):
        name = current_thread().name
        identifier = self.redis.acquire_lock('bbb')
        if identifier:
            print(name, "获取锁")
            db = self.db.get_instance()
            cursor = db.cursor()
            sql = "select a.id,a.status, a.group_id from archives2 a where a.status=0 and not exists(select 1 from archives2 b where b.group_id=a.group_id and b.status!=0) order by rand() limit 1"
            params = ()
            try:
                cursor.execute(sql)
                data = cursor.fetchone()
                if not data:
                    cursor.close()
                    return
                id, _, _ = data
                sql = "update archives2 set status=1 where id=%s"
                params = (id, )
                cursor.execute(sql, params)
                db.commit()
                print(current_thread().name, ":", sql, params, ":success")
            except:
                db.rollback()
                print(current_thread().name, ":", sql, params, ":failed")
                raise
            finally:
                cursor.close()
                db.close()
                print(name, "释放锁")
                self.redis.release_lock('bbb', identifier)
        else:
            print(name, "获取锁超时")
if __name__ == '__main__':
    Test()
