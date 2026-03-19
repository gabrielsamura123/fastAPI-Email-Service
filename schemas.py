from pydantic import BaseModel, Field, EmailStr

class RegisterEmailUsers (BaseModel) :
               email: EmailStr = Field(..., examples=["gabriel@gmail.com"])
               subject: str = Field(..., examples=["Email of greetings"])
               body: str = Field(..., examples=["Anything you want as the para of the email"])
               
