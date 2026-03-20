from src.tasks.dtos import TaskSchema
from sqlalchemy.orm import Session
from src.tasks.model import TaskModel
from fastapi import HTTPException
from src.users.model import UserModel

def create_task(body:TaskSchema, db:Session, user:UserModel):
    data = body.model_dump()
    new_task = TaskModel(
        title = data["title"],
        description = data["description"],
        is_completed = data["is_completed"],
        user_id = user.id
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

def get_tasks(db:Session, user:UserModel):
    tasks = db.query(TaskModel).filter(TaskModel.user_id == user.id).all()
    return tasks

def get_one_task(task_id:int, db:Session, user:UserModel):
    task:UserModel = db.query(TaskModel).get(task_id)
    if not task:
        raise HTTPException(404, detail="task_id is Incorrect !")
    if task.user_id != user.id:
        raise HTTPException(404, detail="You are not Allowed to get this task !")
    return task

def update_task(body:TaskSchema, task_id:int, db:Session, user:UserModel):
    task:UserModel = db.query(TaskModel).get(task_id)
    if not task:
        raise HTTPException(404, detail="task_id is Incorrect !")
    if task.user_id != user.id:
        raise HTTPException(404, detail="You are not allowed to update this task !")

    data = body.model_dump()
    for field, value in data.items():
        setattr(task, field, value)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

def delete_task(task_id:int, db:Session, user:UserModel):
    task:UserModel = db.query(TaskModel).get(task_id)
    if not task:
        raise HTTPException(404, detail="task_id is Incorrect !")
    if task.user_id != user.id:
        raise HTTPException(404, detail="You are not allowed to delete this task !")

    db.delete(task)
    db.commit()
    return None