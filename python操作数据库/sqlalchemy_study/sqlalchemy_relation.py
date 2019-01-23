from sqlalchemy import create_engine,Column,Integer,String,ForeignKey

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

db_name = 'mysql+pymysql://root:123456@localhost:3306/sqlalchemy_study'

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    addresses = relationship('Address',backref='itsuser')

class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer,primary_key=True)
    uid = Column(Integer,ForeignKey('user.id'))
    address = Column(String(100))

engine = create_engine(db_name)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
