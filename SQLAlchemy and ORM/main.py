from DBConfig import engine,SessionLocal
import Model
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends

app = FastAPI()

Model.Base.metadata.create_all(bind=engine)

def ConDb():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def health():
    return "App is Running"

@app.get("/students/all")
def get_all(db:Session = Depends(ConDb)):
    db_stud = db.query(Model.Students).all()
    if db_stud:
        return db_stud
    return "No Students Found"

