from sqlalchemy.orm import Session
from src.users.dtos import UserSchema, LoginSchema
from src.users.model import UserModel
from fastapi import HTTPException, status
from pwdlib import PasswordHash
from src.utils.settings import settings
from datetime import datetime, timedelta
import jwt

password_hash = PasswordHash.recommended()

def get_password_hash(password):
    return password_hash.hash(password)

def verify_password(plain_password, hashed_password):
    return password_hash.verify(plain_password, hashed_password)




def register_user(body:UserSchema, db:Session):
    # username validation
    is_user = db.query(UserModel).filter(UserModel.username == body.username).first()
    if(is_user):
        raise HTTPException(400, detail="Username already Exist !")
    # email validation
    is_user = db.query(UserModel).filter(UserModel.email == body.email).first()
    if(is_user):
        raise HTTPException(400, detail="Email already Exist !")
    # convert password into hash_password
    hash_password = get_password_hash(body.password)

    new_user = UserModel(
        name = body.name,
        username = body.username,
        hash_password = hash_password,
        email = body.email,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def login_user(body:LoginSchema, db:Session):
    # validate username
    user = db.query(UserModel).filter(UserModel.username == body.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You Entered Wrong Username !")
    if not verify_password(body.password, user.hash_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You Entered Wrong Password !")
    # Generate token
    exp_time = datetime.now() + timedelta(minutes=settings.EXP_TIME)
    token = jwt.encode({"_id":user.id, "username":user.username, "exp":exp_time}, settings.SECRET_KEY, settings.ALGORITHM)
    return {"token":token}