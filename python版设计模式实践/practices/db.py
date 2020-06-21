from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import create_engine, text
import pandas as pd
import re


class SQL(object):
    def __init__(self, sql, params=None, engine=None):
        self.sql = sql
        self.params = params

class FetchSQL(SQL):
    def to_dict():
        pass

    def to_cos():
        pass

    def to_frame():
        pass

    def to_csv(sync=None):
        if sync is None:
            pass

    def to_excel():
        pass

    def to_txt():
        pass

    def to_iter():
        pass

class ExecuteSQL(SQL):
    def run():
        pass



class ConnectMixin(object):

    @property
    def url(self):
        pass

    @property
    def config(self):
        pass



class ShortConnectMixin(object):
    @property
    def url(self):
        template = "{schema}://{user}:{passwd}@{host}:{port}/{name}"
        url = template.format(self.db_schema, self.passwd, self.host, self.port, self.name)
        if self.db_schema.find('mysql') != -1:
            encode_param_str =  "?charset=utf8"
            return url + encode_param_str
        else:
            return url

    @property
    def config(self):
        return {
            "db_schema" : self.schema,
            "db_user" : self.user,
            "db_passwd" : self.passwd,
            "db_host" : self.host,
            "db_port" : self.port,
            "db_name" : self.name,
        }


class LongConnectMixin(object):
    @property
    def url(self):
        return self._url

    @property
    def config(self):
        pattern = re.compile(r'^(?P<db_schema>mysql\+(mysqlconnector|mysqldb|pymysql)|postgres)://(?P<db_user>\w+):(?P<db_passwd>.+)@(?P<db_host>.+):(?P<db_port>\d+)/(?P<db_name>\w+)(\?charset=utf8)?$')
        result = pattern.match(self._url)
        if not result:
            raise Exception("db_url format is error...")
        return {
            "db_schema" : result.group('db_schema'),
            "db_user" : result.group('db_user'),
            "db_passwd" : result.group('db_passwd'),
            "db_host" : result.group('db_host'),
            "db_port" : result.group('db_port'),
            "db_name" : result.group('db_name')
        }


class MysqlMixin(object):

    def create_engine(self, url):
        engine = create_engine(url, echo=True, pool_size=100)
        return engine

    def _get_session(self, engine):
        if not engine:
            raise Exception("get session error; engine not exist")
        session_factory = sessionmaker(bind=engine)
        session = session_factory()
        return session

    def backup(self):
        pass

    def restore(self):
        pass

    @property
    def qps(self):
        pass

    @property
    def connections(self):
        pass

    def add_user(self):
        pass

    def grant_privilege(self):
        pass

class PostgresMixin(DbMixin):

    def create_engine(self, url):
        engine = create_engine(url, echo=True, pool_size=100, client_encoding='utf-8')
        return engine

    def _get_session(self, engine):
        if not engine:
            raise Exception("get session error; engine not exist")
        session_factory = sessionmaker(bind=engine)
        session = session_factory()
        return session


    def backup(self):
        pass

    def restore(self):
        pass

    @property
    def qps(self):
        pass

    @property
    def connections(self):
        pass


class AbstractConfig(object):
    def load_config(self):
        pass

    def flash_config(self):
        pass

    def change_user(self):
        pass


class POIConfig(AbstractConfig, MysqlMixin):
    _env = get_envinfo()
    _fushion_config = load_fusion_config()

    def load_config(self):
        config['db_user'] = self.poi_fusion_config.get('dbuser')
        config['db_passwd'] = self.poi_fusion_config.get('dbpasswd')
        config['db_host'] = self.poi_fusion_config.get('dbhost')
        config['db_port'] = self.poi_fusion_config.get('dbport')
        config['db_name'] = self.poi_fusion_config.get('dbname')
        config['db_schema'] = 'mysql+mysqldb'
        return config



class YMarkConfig(AbstractConfig):
    _env = get_envinfo()
    _fushion_config = load_fusion_config()

    def __init__(self):
        self.ymark_fusion_config = _fushion_config[_env]["poi"]

    def load_config(self):
        config['db_user'] = self.ymark_fusion_config.get('dbuser')
        config['db_passwd'] = self.ymark_fusion_config.get('dbpasswd')
        config['db_host'] = self.ymark_fusion_config.get('dbhost')
        config['db_port'] = self.ymark_fusion_config.get('dbport')
        config['db_name'] = self.ymark_fusion_config.get('dbname')
        return config



class KeyConfigAnalysizer(object):
    _registry = {
        "ymark": YMarkConfig,
        "poi": POIConfig
    }
    def __init__(self, key):
        self.key = key

    @classmethod
    def register_config(cls, key, config_class):
        pass

    def create_registry_obj(self):
        return KeyConfigAnalysizer._registry[self.key]()

    @property
    def config(self):
        obj = self.create_register_obj(self.key)
        return obj.load_config()

    @property
    def url(self):
        obj = self.create_register_obj(self.key)
        return obj.load_url()



class DB(object):
    _registed_config = {
        "poi": POIConfig,
        ""
    }
    def __init__(self, key=None, db_url=None, db_schema=None, connect_args=None):
        if key is not None:
            self._config = self._registed_config[key]
        elif db_url is not None:
            self._config = LongConnectMixin(db_url)
        elif db_schema is not None and connect_args is not None:
            self._config = ShortConnectMixin(db_schema, **connect_args)


    @property
    def url(self):
        pass

    @property
    def config(self):
        pass

    def fetch(sql, params=None):
        engine = self.create_engine()
        return FetchSQL(sql, params, engine)

    def create_engine(self):
        pass

    def backup(self):
        pass

    def restore(self):
        pass

    def state(self):
        return connection

    @property
    def qps(self):
        pass

    @property
    def connections(self):
        pass

    def add_user(self):
        pass

    def change_user(self, db_user, db_passwd):
        pass


    def modify_priviledge():
        pass

    def execute(self):
        engine = self.create_engine()
        return ExecuteSQL(sql, params, engine).run()

    def execute_many(self):
        pass
