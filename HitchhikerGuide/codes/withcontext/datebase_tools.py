#!/usr/bin/env python
from pymysql import connect


class CustomDatabase(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.conn = connect(host=self.host, user='root', password='123456',
                            database='ioep')

    def __enter__(self):
        return self.conn

    def __exit__(self, ctx_type, ctx_value, ctx_traceback):
        self.conn.close()


if __name__ == "__main__":
    sql = "show databases;"
    try:
        with CustomDatabase("192.168.80.128", 3306) as conn:
            cursor = conn.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            print(rows)
            cursor.close()

    except Exception as e:
        print(e)

    try:
        conn = connect(host="192.168.80.128", port=3306, password="123456",
                       user="root", database="ioep")
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        print(rows)
        cursor.close()
        conn.close()
    except Exception as e:
        print(e)
