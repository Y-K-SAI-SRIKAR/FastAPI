from . import UserModel
from fastapi import HTTPException
from pwdlib import PasswordHash

password_hash = PasswordHash.recommended()
def get_password(password):
    return password_hash.hash(password)
    

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
    return "User Created Successfully !"
