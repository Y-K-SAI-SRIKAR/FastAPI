from sqlalchemy.orm import sessionmaker,create_engine

DB_URL = "mysql://root:Srikar2201@localhost:3306/fastapi"
engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autoFlush = False, autoCommit = False, bind = engine)

"""
SQLAlchemy is a python SQL toolkit along with ORM support.

ORM Stands for Object Relational Mapping which is a tool for converting the Objects of the model class
into the records of the relational entity in a DataBase.

Session is like a transaction or a communication token which was create to communicate with the DB

Engine is like a connector which establishes association between the Model and DataBase Table.
"""