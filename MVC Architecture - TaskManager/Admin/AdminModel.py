from User import UserModel
from sqlalchemy import Column,Integer,String,Boolean,ForeignKey

Base = UserModel.Base

class Tasks(Base):
    __tablename__="Tasks"
    TaskId = Column(Integer,primary_key=True,index=True,autoincrement=True)
    TaskName = Column(String(50))
    TaskDesc = Column(String(100))
    TaskStatus = Column(Boolean)
    UserId = Column(Integer,ForeignKey("Users.Id",ondelete="CASCADE"))

