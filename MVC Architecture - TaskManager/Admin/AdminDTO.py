from pydantic import BaseModel

class TaskSchema(BaseModel):
    TaskId : int
    TaskName : str
    TaskDesc : str
    TaskStatus : bool=False


"""
DTO is Data Transfer Object which is used for passing states from frontend to DB layer.
Usually DTO operates with a pydantic model while acting as a persistant layer between DB and Frontend.

"""