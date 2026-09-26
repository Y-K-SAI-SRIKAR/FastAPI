from DBConfig import engine,SessionLocal
import Model
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, Body

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
def get_all(db:Session = Depends(ConDb)): #this undergoes Dependency Injection
    db_stud = db.query(Model.Students).all()
    if db_stud:
        return db_stud
    return "No Students Found"

@app.get("/students/{id}")
def get_by_id( id:int,db:Session = Depends(ConDb)): #this undergoes Dependency Injection
    db_stud = db.query(Model.Students).filter(Model.Students.Id == id).first()
    if db_stud:
        return db_stud
    return "No such Student Found"

@app.post("/students/add")
def add_student(Id: int = Body(...),Name: str = Body(...),Dept: str = Body(...),Cgpa: float = Body(...), db:Session=Depends(ConDb)):
    db_stud = Model.Students(Id=Id,Name=Name,Dept=Dept,Cgpa=Cgpa)
    db.add(db_stud)
    db.commit()
    return "Student added Successfully"

@app.put("/students/update")
def upd_student(id:int,Name: str = Body(...),Dept: str = Body(...),Cgpa: float = Body(...),db:Session= Depends(ConDb)):
    db_stud = db.query(Model.Students).filter(Model.Students.Id == id).first()
    if db_stud :
        db_stud.Name = Name
        db_stud.Dept = Dept
        db_stud.Cgpa = Cgpa
        db.commit()
        return "Updated Student"
    return "No Student found"

@app.delete("/students/delete")
def del_student(id:int,db:Session=Depends(ConDb)):
    db_stud = db.query(Model.Students).filter(Model.Students.Id == id).first()
    if db_stud:
        db.delete(db_stud)
        db.commit()
        return "Deleted Student"
    return "No student found"


"""
Dependecny Injection : 
Dependencies are the requirements for the methods to execute.
The methods have to request or call for dependecy during execution, dependencies are not directly allocated to methods.
So, whenever the dependency is requested , API fetches the requirement and injects into the method for processing the sates.
This process is called Dependency Injection.

"""