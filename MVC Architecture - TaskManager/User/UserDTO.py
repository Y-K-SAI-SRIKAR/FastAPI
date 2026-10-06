from pydantic import BaseModel

class UsersRequestSchema(BaseModel):
    Id:int
    Name:str
    UserName:str
    UserEmail:str
    HashPassword:str

class UsersResponseSchema(BaseModel):
    Id:int
    Name:str
    UserName:str
    UserEmail:str
