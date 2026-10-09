from fastapi import APIRouter, Depends
from . import AdminController
from .Admindb import con_db
from .AdminDTO import TaskSchema
from fastapi import Depends
from sqlalchemy.orm import Session
from User import UserModel
from Utils import Helper


Adminroutes = APIRouter(prefix="/routes")

@Adminroutes.post("/task")
def create_tasks(task:TaskSchema,user:UserModel=Depends(Helper.is_auth) ,db:Session=Depends(con_db)):
    return AdminController.create_task(task,db)

@Adminroutes.get("/task")
def get_all_tasks(user:UserModel=Depends(Helper.is_auth),db:Session = Depends(con_db)):
    return AdminController.get_all_tasks(db)

@Adminroutes.get("/task/{id}")
def get_task_by_id(taskId:int,user:UserModel=Depends(Helper.is_auth),db:Session=Depends(con_db)):
    return AdminController.get_task_by_id(taskId,db)

@Adminroutes.put("/task")
def update_task_by_id(task:TaskSchema,taskId:int,user:UserModel=Depends(Helper.is_auth),db:Session=Depends(con_db)):
    return AdminController.update_task_by_id(task,taskId,db)

@Adminroutes.delete("/task")
def delete_task_by_id(taskId:int,user:UserModel=Depends(Helper.is_auth),db:Session=Depends(con_db)):
    return AdminController.delete_task_by_id(taskId,db)