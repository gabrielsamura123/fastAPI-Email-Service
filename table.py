from sqlalchemy import Column, String, Integer
from .database_connect import email_base

class Email_Users (email_base) :
               __tablename__="email_users"
               id = Column(Integer, index=True, primary_key=True)
               email = Column(String)
               subject = Column(String)
               body = Column(String)
               
