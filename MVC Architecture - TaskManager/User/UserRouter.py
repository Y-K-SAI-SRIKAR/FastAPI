from fastapi import APIRouter,Depends
from . import UserController
from .Userdb import con_Udb
from .UserDTO import UsersRequestSchema, UsersResponseSchema
from sqlalchemy.orm import Session

Userroutes = APIRouter(prefix="/uroutes")

@Userroutes.post("/register")
def register_user(body:UsersRequestSchema, response_model=UsersResponseSchema, db:Session=Depends(con_Udb)):
    return UserController.register_user(body,db,response_model)