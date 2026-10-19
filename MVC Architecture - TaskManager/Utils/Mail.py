from fastapi import FastAPI
from fastapi_mail import MessageSchema,ConnectionConfig, MessageType, FastMail
from pydantic import EmailStr, BaseModel 
from typing import List
from . import Settings

class EmailSchema(BaseModel):
    email : List[EmailStr]

config = ConnectionConfig(
    MAIL_USERNAME = Settings.settings.APP_EMAIL,
    MAIL_PASSWORD = Settings.settings.APP_PASSWORD,
    MAIL_FROM = Settings.settings.APP_EMAIL,
    MAIL_PORT = 587,
    MAIL_SERVER = "smtp.gmail.com",
    MAIL_FROM_NAME="Srikar Yerraguntla",
    MAIL_STARTTLS = True,
    MAIL_SSL_TLS = False,
    USE_CREDENTIALS = True,
    VALIDATE_CERTS = True
)

async def mail_message(email: EmailSchema):
    html = """<p>Hello, I am Srikar. I have sent This Email as part of my FastAPI Learning.</p> """
    message = MessageSchema(
        subject="Acknowledgement mail",
        recipients=[email],
        body=html,
        subtype=MessageType.html)

    fm = FastMail(config)
    await fm.send_message(message)
    return "Mail Sent Successfully"