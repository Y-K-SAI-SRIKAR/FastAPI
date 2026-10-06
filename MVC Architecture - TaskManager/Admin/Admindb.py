from .AdminDBConfig import engine, Session
from . import AdminModel

AdminModel.Base.metadata.create_all(bind = engine)

def con_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()
