from fastapi import APIRouter, Depends, status, Request
from sqlalchemy.orm import Session
from src.users import controller
from src.users.dtos import UserSchema, UserOut, LoginSchema
from src.utils.db import get_db

user_routes = APIRouter(prefix="/user")

@user_routes.post("/register", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def register(body:UserSchema, db:Session=Depends(get_db)):
    return controller.register_user(body, db)

@user_routes.post("/login", status_code=status.HTTP_200_OK)
def login_user(body:LoginSchema, db:Session=Depends(get_db)):
    return controller.login_user(body, db)

@user_routes.get("/is_auth", response_model=UserOut, status_code=status.HTTP_200_OK)
def is_auth(request:Request, db:Session=Depends(get_db)):
    return controller.is_auth(request, db)