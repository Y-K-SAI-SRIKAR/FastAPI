from DBConfig import engine
import Model
from sqlalchemy.orm import session
from Model import Base
from fastapi import FastAPI, Depends

app = FastAPI()

Model.Base.metadata.create_all(bind=engine)

def ConDb():
    db = session()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def health():
    return "App is Running"

