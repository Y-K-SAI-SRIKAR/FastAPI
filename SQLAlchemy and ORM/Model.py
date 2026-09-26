from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,Float

Base = declarative_base()
class Students(Base):
    __tablename__="students"
    Id = Column(Integer,primary_key=True,index=True)
    Name = Column(String)
    Dept = Column(String)
    Cgpa = Column(Float)


"""
declarative_base allows to define the architecture of the Relational Entity i.e DB table such as 
    1. Configure Data Types
    2. Key Constraints and Indexing
    
"""