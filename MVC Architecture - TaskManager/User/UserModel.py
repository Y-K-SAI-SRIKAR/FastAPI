from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String

Base = declarative_base() 

class Users(Base):
    __tablename__ = "Users"
    Id = Column(Integer,primary_key=True,index=True)
    Name = Column(String(50),nullable=False)
    UserName = Column(String(50),nullable=False)
    UserEmail = Column(String(100),nullable=False)
    HashPassword = Column(String(255),nullable=False)
