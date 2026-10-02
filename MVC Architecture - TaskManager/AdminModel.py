from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,Boolean

Base = declarative_base()

class Tasks(Base):
    __tablename__="Tasks"
    TaskId = Column(Integer,primary_key=True,index=True)
    TaskName = Column(String(50))
    TaskDesc = Column(String(100))
    TaskStatus = Column(Boolean=False)

