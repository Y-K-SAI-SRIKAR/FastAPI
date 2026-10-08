from pydantic import BaseModel

class UsersRequestSchema(BaseModel):
    Name:str
    UserName:str
    UserEmail:str
    Password:str

class UsersResponseSchema(BaseModel):
    Id:int
    Name:str
    UserName:str
    UserEmail:str

class UsersLoginSchema(BaseModel):
    UserName:str
    Password:str
    