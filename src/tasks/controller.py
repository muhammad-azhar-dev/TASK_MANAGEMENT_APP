from src.tasks.dtos import TaskSchema
from sqlalchemy.orm import Session
from src.tasks.model import TaskModel
from fastapi import HTTPException

def create_task(body:TaskSchema, db:Session):
    data = body.model_dump()
    new_task = TaskModel(
        title = data["title"],
        description = data["description"],
        is_completed = data["is_completed"]
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return {"status":"Task Created Successfully", "data":new_task}

def get_tasks(db:Session):
    tasks = db.query(TaskModel).all()
    return {"status":"Tasks Fetched Successfully", "data":tasks}

def get_one_task(task_id:int, db:Session):
    task = db.query(TaskModel).get(task_id)
    if not task:
        raise HTTPException(404, detail="task_id is Incorrect!")
    return {"status":"Task Fetched Successfully", "data":task}