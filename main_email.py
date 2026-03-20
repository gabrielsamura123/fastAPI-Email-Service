import os
from dotenv import load_dotenv # type: ignore
from fastapi import FastAPI, Depends, HTTPException, BackgroundTasks

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig # type: ignore
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr
from schemas import RegisterEmailUsers
from sqlalchemy.orm import Session
from database_connect import email_session_local, email_engine, email_base
from table import Email_Users

email_app = FastAPI()
email_base.metadata.create_all(bind=email_engine)

email_app.add_middleware(
               CORSMiddleware,
               allow_origins=["*"],
               allow_credentials=True,
               allow_methods=["*"],
               allow_headers=["*"],
)

def get_db():
               db = email_session_local()
               try:
                              yield db
               finally:
                              db.close()
                              


conf = ConnectionConfig(
               MAIL_USERNAME=os.getenv("MAIL_USERNAME"),
               MAIL_PASSWORD=os.getenv("MAIL_PASSWORD"),
               MAIL_FROM=os.getenv("MAIL_FROM"),
               MAIL_PORT=int(os.getenv("MAIL_PORT")),
               MAIL_SERVER=os.getenv("MAIL_SERVER"), 
               MAIL_STARTTLS=True,
               MAIL_SSL_TLS=False,
               USE_CREDENTIALS=True,
               VALIDATE_CERTS=False
)

fm = FastMail(conf)

# CREATING THE EMAIL ENDPOINTS

@email_app.get("/", tags=["Email Service"])
async def root():
               return {"message": "Welcome to the Email Service API!"}

@email_app.post("/sendMail/", tags=["Email Service"])
async def send_mail(email: RegisterEmailUsers, db: Session = Depends(get_db)) :
               message = MessageSchema(
                              subject=email.subject,
                              recipients=[conf.MAIL_FROM],
                              body=f"Message from: {email.email}\n\n{email.body}",
                              subtype="plain"
               )
               try:
                              await fm.send_message(message)
                              new_email_user = Email_Users(email=email.email, subject=email.subject, body=email.body)
                              db.add(new_email_user)
                              db.commit()
                              db.refresh(new_email_user)
                              return {"message": "Email has been sent", "email_user": new_email_user}
               except Exception as e:
                              raise HTTPException(status_code=500, detail=f"Failed to send email: {str(e)}")