from sqlalchemy import create_engine, String, Integer, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_name = "mysql+pymysql://root:123456@localhost:3306/sqlalchemy_study"
Base = declarative_base()
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))

engine = create_engine(db_name)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
