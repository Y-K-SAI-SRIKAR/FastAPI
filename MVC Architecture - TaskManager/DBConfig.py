from sqlalchemy.orm import session_maker
from sqlalchemy import create_engine

DB_URL = ""
engine = create_engine(DB_URL)
Session = session_maker(autocommit=False,
                        autoFlus=False,
                        bind=engine
                        )
