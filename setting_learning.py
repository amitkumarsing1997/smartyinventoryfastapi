# from fastapi import FastAPI
# from pydantic_settings import BaseSettings
#
#
# class Settings(BaseSettings):
#     app_name: str = "Awesome API"
#     admin_email: str
#     items_per_user: int = 50
#
#
# settings = Settings()
# app = FastAPI()
#
#
# @app.get("/info")
# async def info():
#     return {
#         "app_name": settings.app_name,
#         "admin_email": settings.admin_email,
#         "items_per_user": settings.items_per_user,
#     }


# from fastapi import Depends, FastAPI, HTTPException
#
# app = FastAPI()
#
# # Dependency function
# def fake_dependency(token: str = Depends(lambda x: x)):
#     if token != "fake-token":
#         raise HTTPException(status_code=401, detail="Invalid token")
#     return token
#
# # Route using the dependency
# @app.get("/protected")
# async def protected_route(token: str = Depends(fake_dependency)):
#     return {"message": "This is a protected route", "token": token}






from pydantic_settings import BaseSettings,SettingsConfigDict
from typing import Dict


class MySettings(BaseSettings):
    api_key: str
    debug: bool = False
    max_items: int = 10


# Example configuration dictionary
config_dict = {
    "api_key": "your_api_key_here",
    "debug": True,
    "max_items": 20
}

# Create an instance of MySettings using the configuration dictionary
settings = MySettings(**config_dict)

# Access the settings attributes
print(settings.api_key)  # Output: your_api_key_here
print(settings.debug)  # Output: True
print(settings.max_items)  # Output: 20
