from pydantic import BaseModel

class TaskCreate(BaseModel):
    title: str
    description: str

class TaskUpdate(BaseModel):
    is_completed: bool

class Task(BaseModel):
    id: int
    title: str
    description: str
    is_completed: bool

    class Config:
        orm_mode = True