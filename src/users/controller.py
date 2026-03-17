from sqlalchemy.orm import Session
from src.users.dtos import UserSchema
from src.users.model import UserModel
from fastapi import HTTPException
from pwdlib import PasswordHash

password_hash = PasswordHash.recommended()
def get_password_hash(password):
    return password_hash.hash(password)



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