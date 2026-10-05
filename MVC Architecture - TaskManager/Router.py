from fastapi import APIRouter
import AdminController
from db import con_db
from AdminDTO import TaskSchema
from fastapi import Depends
from sqlalchemy.orm import Session
import AdminModel

routes = APIRouter(prefix="/routes")

@routes.post("/task")
def create_tasks(task:TaskSchema, db:Session=Depends(con_db)):
    return AdminController.create_task(task,db)

@routes.get("/task")
def get_all_tasks(db:Session = Depends(con_db)):
    return AdminController.get_all_tasks(db)

@routes.get("/task/{id}")
def get_task_by_id(taskId:int,db:Session=Depends(con_db)):
    return AdminController.get_task_by_id(taskId,db)

@routes.put("/task")
def update_task_by_id(task:TaskSchema,taskId:int,db:Session=Depends(con_db)):
    return AdminController.update_task_by_id(task,taskId,db)

@routes.delete("/task")
def delete_task_by_id(taskId:int,db:Session=Depends(con_db)):
    return AdminController.delete_task_by_id(taskId,db)