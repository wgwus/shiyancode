from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String,Integer


engine = create_engine('mysql+mysqldb://root@localhost:3306/shiyanlougithub?charset=utf8')
Base = declarative_base()

class respositories(Base):

    __tablename__ = 'respositories'
    
    id = Column(Integer,primary_key=True)
    name = Column(String(64),index=True)
    datetime = Column(String(64),index=True)
    
    commits=Column(Integer)
    branches=Column(Integer)

    releases=Column(Integer)
    
if __name__=='__main__':
    Base.metadata.create_all(engine)
