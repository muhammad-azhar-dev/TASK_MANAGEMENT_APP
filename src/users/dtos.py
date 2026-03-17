from pydantic import BaseModel

class UserSchema(BaseModel):
    name : str
    username : str
    password : str
    email : str

class UserOut(BaseModel):
    id : int
    name : str
    username : str
    email : str