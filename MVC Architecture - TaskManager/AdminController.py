import AdminModel

def create_task(task,db):
    db_task = AdminModel.Tasks(**task.model_dump())
    db.add(db_task)
    db.commit()
    return "Task Created Successfully"

def get_all_tasks(db):
    db_task = db.query(AdminModel.Tasks).all()
    if db_task:
        return db_task
    else:
        return "No Tasks Exist"

def get_task_by_id(taskId,db):
    db_task = db.query(AdminModel.Tasks).filter(AdminModel.Tasks.TaskId == taskId).first()
    if db_task:
        return db_task
    else:
        return "No Such Tasks Found"

def delete_task_by_id(taskId,db):
    db_task = db.query(AdminModel.Tasks).filter(AdminModel.Tasks.TaskId == taskId).first()
    if db_task:
        db.delete(db_task)
        db.commit()
        return "Operation Success"
    else:
        return "No Task Exists"

def update_task_by_id(task,taskId,db):
    db_task = db.query(AdminModel.Tasks).filter(AdminModel.Tasks.TaskId == taskId).first()
    if db_task:
        db_task.TaskName = task.TaskName
        db_task.TaskDesc = task.TaskDesc
        db_task.TaskStatus = task.TaskStatus
        db.commit()
        return "Operation Success"
    else:
        return "No Such Task Exists"
