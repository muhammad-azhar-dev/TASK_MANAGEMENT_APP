from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from src.users import controller
from src.users.dtos import UserSchema, UserOut
from src.utils.db import get_db

user_routes = APIRouter(prefix="/user")

@user_routes.post("/register", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def register(body:UserSchema, db:Session=Depends(get_db)):
    return controller.register_user(body, db)