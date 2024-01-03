from fastapi import FastAPI
from starlette.responses import JSONResponse
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from pydantic import EmailStr, BaseModel
from typing import List,Dict,Any


# class EmailSchema(BaseModel):
#     email: List[EmailStr]
#     body: Dict[str, Any]

conf = ConnectionConfig(
 MAIL_USERNAME="amitksinghmdv@gmail.com",
    MAIL_PASSWORD="vvrf maog opvd ndrk",
    MAIL_FROM="amitksinghmdv@gmail.com",
    MAIL_PORT=465,
    MAIL_SERVER="smtp.gmail.com",
    MAIL_STARTTLS=False,
    MAIL_SSL_TLS=True,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True,
    # TEMPLATE_FOLDER='./app/server/templates/email'
    TEMPLATE_FOLDER='./src2/app/muser/util/templates/email'
)


# app = FastAPI()

# @app.post("/email")
async def send_with_template(token_detail: dict):

    message = MessageSchema(
        subject="Fastapi-Mail module",
        recipients=["ak910221@gmail.com"],
        # template_body=email.model_dump().get("body"),
        template_body=token_detail,
        subtype=MessageType.html,
        )
    fm = FastMail(conf)
    await fm.send_message(message, template_name="email.html")
    # return JSONResponse(status_code=200, content={"message": "email has been sent"})