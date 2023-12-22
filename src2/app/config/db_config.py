from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from typing import Annotated
from fastapi import Depends

SQLALCHEMY_DATABASE_URL='mysql+pymysql://root:1234@127.0.0.1:3306/TodoApplicationDatabase'

# engine=create_engine(SQLALCHEMY_DATABASE_URL,connect_args={'check_same_thread': False})
engine=create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base=declarative_base()



def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency=Annotated[Session,Depends(get_db)]

