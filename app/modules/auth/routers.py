from fastapi import (
    APIRouter,
    Depends,
    status,
)
from typing import Union
from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str
    password: str
    is_admin: Union[bool, None] = None
    
route = APIRouter(prefix="/auth", tags=["Auth"])
    

@route.get("/login")
def login():
    return {"msg": "Login Success"}


@route.post("/register")
def register(user: User):
    return {"msg": "Register Success"}


@route.post("/logout")
def logout():
    return {"msg": "Logout Success"}


@route.get("/me")
def me():
    return {"msg": "Current User Details"}