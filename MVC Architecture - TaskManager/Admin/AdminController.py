from . import AdminModel
from fastapi import HTTPException

def create_task(task,db,user):
    db_task = AdminModel.Tasks(**task.model_dump(),UserId=user.Id)
    db.add(db_task)
    db.commit()
    return "Task Created Successfully"

def get_all_tasks(db, user):
    db_task = db.query(AdminModel.Tasks).filter(AdminModel.Tasks.UserId==user.Id).all()
    if db_task:
        return db_task
    else:
        return []

def get_task_by_id(taskId,db):
    db_task = db.query(AdminModel.Tasks).filter(AdminModel.Tasks.TaskId == taskId).first()
    if db_task:
        return db_task
    else:
        return "No Such Tasks Found"

def delete_task_by_id(taskId,db,user):
    db_task = db.query(AdminModel.Tasks).filter(AdminModel.Tasks.TaskId == taskId).first()
    if db_task and (db_task.UserId == user.Id):
        db.delete(db_task)
        db.commit()
        return "Operation Success"
    else:
        raise HTTPException(401,detail="UnAuthorized Action")

def update_task_by_id(task,taskId,db,user):
    db_task = db.query(AdminModel.Tasks).filter(AdminModel.Tasks.TaskId == taskId).first()
    if db_task and (db_task.UserId == user.Id):
        db_task.TaskName = task.TaskName
        db_task.TaskDesc = task.TaskDesc
        db_task.TaskStatus = task.TaskStatus
        db.commit()
        return "Operation Success"
    else:
        raise HTTPException(401,detail="UnAuthorized Action")