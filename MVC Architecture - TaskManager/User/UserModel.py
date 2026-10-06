from sqlalchemy.ext.declarative import declarative_base
from sqlachemy import Column,Integer,String

Base = declarative_base() 

class Users(Base):
    __tablename__ = "Users"
    Id = Column(Integer,primary_key=True,index=True)
    Name = Column(String,nullable=False)
    UserName = Column(String,nullable=False)
    UserEmail = Column(String,nullable=False)
    HashPassword = Column(String,nullable=False)
