from sqlmodel import SQLModel, Field, Column, VARCHAR
from enum import Enum
from typing import Union, Optional


class Status(Enum):
    open = "open"
    done = "done"


class ToDoInput(SQLModel):
    description: str
    status: Status


class ToDo(ToDoInput, table=True):
    id: int = Field(default=None, primary_key=True)


class Token(SQLModel):
    access_token: str
    token_type: str


class TokenData(SQLModel):
    username: Union[str, None] = None


class UserOutput(SQLModel):
    id: int
    username: str


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(sa_column=Column("username", VARCHAR, unique=True, index=True))
    password_hash: str = ""
