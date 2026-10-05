import AdminModel


def create_task(task,db):
    db_task = AdminModel.Tasks(**task.model_dump())
    db.add(db_task)
    db.commit()
    return "Task Created Successfully"


