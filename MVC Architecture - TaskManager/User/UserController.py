from . import UserModel
from fastapi import HTTPException,status
from pwdlib import PasswordHash
import jwt
from jwt.exceptions import InvalidTokenError
from datetime import datetime, timedelta, timezone
from Utils import Settings

password_hasher = PasswordHash.recommended()
def get_password(password):
    return password_hasher.hash(password)

def verify_password(plain_password,hashed_password):
    return password_hasher.verify(plain_password,hashed_password)
    

def register_user(body,db):
    exist_username = db.query(UserModel.Users).filter(UserModel.Users.UserName == body.UserName).first()
    if exist_username:
        raise HTTPException(400,detail="UserName Already Taken Try another UserName")
    exist_email = db.query(UserModel.Users).filter(UserModel.Users.UserEmail == body.UserEmail).first()
    if exist_email:
        raise HTTPException(400,detail="UserEmail Already Taken Try another Email")
    hashed_password = get_password(body.Password)
    new_user = UserModel.Users(
        Name=body.Name,
        UserName=body.UserName,
        UserEmail=body.UserEmail,
        HashPassword=hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def login_user(body,db):
    user = db.query(UserModel.Users).filter(UserModel.Users.UserName == body.UserName).first()
    if not user:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail = "Incorrect UserName")
    verified_password = verify_password(body.Password, user.HashPassword)
    if not verified_password:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail = "Incorrect Password")
    exp_time = datetime.now(timezone.utc)+timedelta(minutes=Settings.settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    token =  jwt.encode({"_id":user.Id,"exp":exp_time}, Settings.settings.SECURITY_KEY, Settings.settings.ALGORITHM)
    return {"Login Success":token}

