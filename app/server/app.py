from fastapi import FastAPI

from app.server.routes.student import router as StudentRouter

from src2.app.admin.admin_schema import AdminResponse, AdminTodoRespSchema

app = FastAPI()

# app.include_router(StudentRouter, tags=["Student"], prefix="/student")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}