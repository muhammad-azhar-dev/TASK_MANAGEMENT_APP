from fastapi import FastAPI
from src.utils.db import Base, engine
from src.tasks.model import TaskModel

try:
    Base.metadata.create_all(engine)
    print("-------------- Database Connected ----------------")
except Exception as e:
    print("-------------- Database Connection ERROR ----------------")

app = FastAPI(title="This is my Task Management Application")

