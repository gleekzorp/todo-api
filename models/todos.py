from pydantic import BaseModel


class TodoModel(BaseModel):
    id: int
    title: str
    done: bool
