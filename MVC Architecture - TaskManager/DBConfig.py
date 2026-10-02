from sqlalchemy.orm import session_maker
from sqlalchemy import create_engine

DB_URL = "mysql+pymysql://root:Srikar2201@localhost:3306/taskmanager"
engine = create_engine(DB_URL)
Session = session_maker(autocommit=False,
                        autoFlus=False,
                        bind=engine
                        )

