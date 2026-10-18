from fastapi import APIRouter, Depends
from . import AdminController
from .Admindb import con_db
from .AdminDTO import TaskSchema, TaskResponseSchema
from fastapi import Depends
from sqlalchemy.orm import Session
from User import UserModel
from Utils import Helper
from typing import List


Adminroutes = APIRouter(prefix="/routes")

@Adminroutes.post("/task")
def create_tasks(task:TaskSchema,user:UserModel=Depends(Helper.is_auth) ,db:Session=Depends(con_db)):
    return AdminController.create_task(task,db,user)

@Adminroutes.get("/task",response_model =List[TaskResponseSchema])
def get_all_tasks(user:UserModel=Depends(Helper.is_auth),db:Session = Depends(con_db)):
    return AdminController.get_all_tasks(db,user)

@Adminroutes.get("/task/{taskId}",response_model =List[TaskResponseSchema])
def get_task_by_id(taskId:int,user:UserModel=Depends(Helper.is_auth),db:Session=Depends(con_db)):
    return AdminController.get_task_by_id(taskId,db)

@Adminroutes.put("/task/{taskId}")
def update_task_by_id(task:TaskSchema,taskId:int,user:UserModel=Depends(Helper.is_auth),db:Session=Depends(con_db)):
    return AdminController.update_task_by_id(task,taskId,db,user)

@Adminroutes.delete("/task")
def delete_task_by_id(taskId:int,user:UserModel=Depends(Helper.is_auth),db:Session=Depends(con_db)):
    return AdminController.delete_task_by_id(taskId,db,user)