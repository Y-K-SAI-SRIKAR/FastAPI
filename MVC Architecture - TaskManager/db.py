from DBConfig import engine, Session
import AdminModel

AdminModel.Base.metadata.create_all(bind = engine)

def con_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()
