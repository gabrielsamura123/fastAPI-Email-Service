from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

import os
from dotenv import load_dotenv # type: ignore

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)
DATABASE_EMAIL_URL = os.getenv("DATABASE_URL")

email_engine = create_engine(url=DATABASE_EMAIL_URL)
email_session_local = sessionmaker(autocommit=False, autoflush=False, bind=email_engine)
email_base = declarative_base()