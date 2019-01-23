from sqlite3 import connect

db_name = 'test'


class Contect:
    def __init__(self, name='', home_tel='', office_tel='', mobile_phone='', memo=''):
        self.id = -1
        self.name = name
        self.home_tel = home_tel
        self.office_tel = office_tel
        self.mobile_phone = mobile_phone
        self.memo = memo
        self.keys = ('home_tel', 'office_tel', 'mobile_phone', 'memo')

    def save(self):
        if self.id == -1:
            params_dict = {k:getattr(self,k) for k in self.keys if getattr(self,k)}
            keys = tuple(k for k in self.keys if k in params_dict)
            quotes = ','.join(("?" for _ in range(len(params_dict))))
            param_tuple = [self.name,]
            for key in keys:
                param_tuple.append(params_dict[key])
            param_tuple = tuple(param_tuple)
            sql = 'INSERT INTO contact (name,%s) VALUES (?, %s)'%(','.join(keys), quotes)
            print(sql,param_tuple)

c = Contect('zhangsan','13838389438','qwewqe')
c.save()

