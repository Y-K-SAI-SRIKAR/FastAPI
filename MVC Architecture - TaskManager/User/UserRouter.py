from fastapi import APIRouter,Depends,Request
from . import UserController
from .Userdb import con_Udb
from .UserDTO import UsersRequestSchema, UsersResponseSchema, UsersLoginSchema
from sqlalchemy.orm import Session

Userroutes = APIRouter(prefix="/uroutes")

@Userroutes.post("/register",response_model=UsersResponseSchema)
def register_user(body:UsersRequestSchema,db:Session=Depends(con_Udb)):
    return UserController.register_user(body,db)

@Userroutes.post("/login")
def login_user(body:UsersLoginSchema, db:Session=Depends(con_Udb)):
    return UserController.login_user(body,db)

@Userroutes.get("/auth",response_model = UsersResponseSchema)
def is_auth(request:Request, db:Session=Depends(con_Udb)):
    return UserController.is_auth(request,db)