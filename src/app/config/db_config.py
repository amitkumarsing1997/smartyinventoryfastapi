from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# SQLALCHEMY_DATABASE_URL='sqlite:///./todosapp.db'
SQLALCHEMY_DATABASE_URL='mysql+pymysql://root:1234@localhost/TodoApplicationDatabase'
# SQLALCHEMY_DATABASE_URL='postgresql://postgres:1234@localhost/TodoApplicationDatabase'
# SQLALCHEMY_DATABASE_URL='mysql+pymysql://root:1234@127.0.0.1:3306/TodoApplicationDatabase'

# engine=create_engine(SQLALCHEMY_DATABASE_URL,connect_args={'check_same_thread': False})
engine=create_engine(SQLALCHEMY_DATABASE_URL,connect_args={'check_same_thread': False})

SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base=declarative_base()

 






from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base

# Database configuration
SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:1234@127.0.0.1:3306/todoapplicationdatabase2'
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# class Database:
#     def __init__(self):
#         self._engine = engine
#         self._SessionLocal = SessionLocal

#     def get_db(self) -> Session:
#         db = self._SessionLocal()
#         try:
#             yield db
#         finally:
#             db.close()

# # Create a global instance of the Database class
# db = Database()

# Now, you can use this global instance in other files or modules
# For example, in your FastAPI application file (main.py):
# from fastapi import FastAPI, Depends
# from your_module import db_dependency

# app = FastAPI()

# @app.get("/some-endpoint")
# async def some_endpoint(db: Session = Depends(db.get_db)):
#     # Use the db session here
#     # Example: result = db.query(...).filter(...).all()
#     return {"message": "Data fetched successfully"}

# rom sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base

# SQLALCHEMY_DATABASE_URL='mysql+pymysql://root:1234@127.0.0.1:3306/smartstock4'
# engine=create_engine(SQLALCHEMY_DATABASE_URL,connect_args={'check_same_thread': False})
# SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)
# Base=declarative_base()


# print("connection successful")


# def get_db():
#     db=SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# db_dependency=Annotated[Session,Depends(get_db)]