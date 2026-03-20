from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from src.utils.db import Base

class TaskModel(Base):
    __tablename__ = "user_tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    is_completed = Column(Boolean)

    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))