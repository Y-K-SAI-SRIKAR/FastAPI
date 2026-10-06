from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

DB_URL = "mysql+pymysql://root:Srikar2201@localhost:3306/taskmanager"
engine = create_engine(DB_URL)
Session = sessionmaker(autocommit=False,
                        autoflush=False,
                        bind=engine
                        )