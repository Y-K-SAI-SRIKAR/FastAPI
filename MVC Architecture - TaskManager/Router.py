from fastapi import APIRouter
import AdminController
from db import con_db
from AdminDTO import TaskSchema
from fastapi import Depends
from sqlalchemy.orm import Session
import AdminModel

routes = APIRouter(prefix="/routes")

@routes.post("/create")
def create_tasks(task:TaskSchema, db : Session=Depends(con_db)):
    return AdminController.create_task(task,db)

