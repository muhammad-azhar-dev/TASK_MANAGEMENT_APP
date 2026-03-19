from fastapi import Request, HTTPException, status, Depends
from jwt import InvalidTokenError
from src.utils.settings import settings
from src.users.model import UserModel
from sqlalchemy.orm import Session
from src.utils.db import get_db
import jwt

def is_auth(request:Request, db:Session = Depends(get_db)):
    try:
        token = request.headers.get("authorization")
        if not token:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You are unauthorized !")
        token = token.split(" ")[-1]

        # validate token
        data = jwt.decode(token, settings.SECRET_KEY, settings.ALGORITHM)
        user_id = data.get("_id")
        username = data.get("username")


        # check user id has user or not
        user = db.query(UserModel).filter(UserModel.id == user_id).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You are unauthorized !")
        # check username exist or not
        user = db.query(UserModel).filter(UserModel.username == username).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You are unauthorized !")
        return user
    except InvalidTokenError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You are unauthorized !")