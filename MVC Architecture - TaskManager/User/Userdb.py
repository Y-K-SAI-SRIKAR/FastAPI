from .UserDBConfig import Session, engine
from . import UserModel

UserModel.Base.metadata.create_all(bind=engine)

def con_Udb():
    db = Session()
    try:
        yield db
    finally:
        db.close()
