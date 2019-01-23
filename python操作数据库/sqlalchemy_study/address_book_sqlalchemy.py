from sqlalchemy import create_engine, String, Integer, Column, ForeignKey, Table, Sequence, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

db_name = 'mysql+pymysql://root:123456@localhost:3306/sqlalchemy_study'

Base = declarative_base()
con_gro = Table('asso', Base.metadata,
                Column('con_id', Integer, ForeignKey('contact.id')),
                Column('gro_id', Integer, ForeignKey('mygroup.id'))
                )

class Contact(Base):
    __tablename__ = 'contact'
    id = Column(Integer, Sequence('contact_id'), primary_key=True)
    name = Column(String(20))
    home_tel = Column(String(20))
    office_tel = Column(String(20))
    mobile_phone = Column(String(20))
    memo = Column(Text)
    groups = relationship('Group',secondary=con_gro, backref='contacts')

class Group(Base):
    __tablename__ = 'mygroup'
    id = Column(Integer, Sequence('mygroup_id'), primary_key=True)
    name = Column(String(20))
    memo = Column(Text)

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

    engine = create_engine(db_name)
    Session = sessionmaker(bind=engine)
    session = Session()

    print("初始化数据库...")
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    print("插入数据...")
    for ct in cts:
        session.add(Contact(**ct))
    for gp in gps:
        session.add(Group(**gp))

    session.commit()

    print("从数据库中查询到的数据")
    for c in session.query(Contact).all():
        print(c.id, c.name, c.home_tel, c.office_tel, c.mobile_phone, c.memo)

    for g in session.query(Group).all():
        print(g.id, g.name, g.memo)


    print("查询联系人, 并添加到组2")
    ct = session.query(Contact).filter_by(name="Lily").first()   # 查询不到
    print(ct.id, ct.name)
    gp = session.query(Group).filter_by(id=2).first()
    gp.contacts.append(ct)


    gp = session.query(Group).filter_by(name='家人').first()
    gp.contacts.append(ct)

    print("删除联系人")
    c = session.query(Contact).filter_by(id=3).first()
    session.delete(c)

    print("删除组")
    g = session.query(Group).filter_by(id=1).first()
    session.delete(g)
    session.commit()

    for c in session.query(Contact).all():
        print(c.id, c.name)
    for g in session.query(Group).all():
        print(g.id, g.name)

