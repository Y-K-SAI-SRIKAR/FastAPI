from fastapi import status, HTTPException,Request, Depends
from sqlalchemy.orm import Session
from User import UserModel
from User import Userdb
from jwt.exceptions import InvalidTokenError
import jwt
from datetime import datetime, timedelta, timezone
from Utils import Settings

def is_auth(request:Request, db:Session=Depends(Userdb.con_Udb)):
    try:
        auth_token = request.headers.get("AuthKey")
        if not auth_token:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail = "You are not Logged in")
        token_num = auth_token.split(" ")[-1]
        data = jwt.decode(token_num, Settings.settings.SECURITY_KEY, Settings.settings.ALGORITHM)
        auth_user = db.query(UserModel.Users).filter(UserModel.Users.Id == data["_id"]).first()
        if not auth_user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail = "You are UnAuthorized")
        return auth_user
    except InvalidTokenError as e:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail = "Session Expired, Login Again.")