from fastapi import APIRouter
from . import AdminController
from .db import con_db
from .AdminDTO import TaskSchema
from fastapi import Depends
from sqlalchemy.orm import Session


Adminroutes = APIRouter(prefix="/routes")

@Adminroutes.post("/task")
def create_tasks(task:TaskSchema, db:Session=Depends(con_db)):
    return AdminController.create_task(task,db)

@Adminroutes.get("/task")
def get_all_tasks(db:Session = Depends(con_db)):
    return AdminController.get_all_tasks(db)

@Adminroutes.get("/task/{id}")
def get_task_by_id(taskId:int,db:Session=Depends(con_db)):
    return AdminController.get_task_by_id(taskId,db)

@Adminroutes.put("/task")
def update_task_by_id(task:TaskSchema,taskId:int,db:Session=Depends(con_db)):
    return AdminController.update_task_by_id(task,taskId,db)

@Adminroutes.delete("/task")
def delete_task_by_id(taskId:int,db:Session=Depends(con_db)):
    return AdminController.delete_task_by_id(taskId,db)