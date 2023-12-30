from fastapi import APIRouter, Depends, HTTPException
from typing import Optional
import models as md
from sqlmodel import Session, select
from db import get_session
from auth import get_current_user
from typing_extensions import Annotated


router = APIRouter(prefix="/api/todos")


@router.get("/")
def get_todos(session: Annotated[Session, Depends(get_session)]) -> list:
    query = select(md.ToDo)
    return list(session.exec(query).all())


@router.get("/{item_id}", response_model=md.ToDo)
def todo_by_id(item_id: int, session: Annotated[Session, Depends(get_session)]) -> md.ToDo:
    todo: Optional[md.ToDo] = session.get(md.ToDo, item_id)
    if todo:
        return todo
    else:
        raise HTTPException(status_code=404, detail=f"No todo with id={item_id}.")


@router.post("/", response_model=md.ToDo)
def add_todo(todo_input: md.ToDoInput,
             session: Annotated[Session, Depends(get_session)],
             current_user: Annotated[md.User, Depends(get_current_user)]) -> md.ToDo:
    new_todo = md.ToDo.model_validate(todo_input)
    session.add(new_todo)
    session.commit()
    session.refresh(new_todo)
    return new_todo


@router.delete("/{item_id}", status_code=204)
def remove_todo(item_id: int, session: Annotated[Session, Depends(get_session)],
                current_user: Annotated[md.User, Depends(get_current_user)]) -> None:
    todo = session.get(md.ToDo, item_id)
    if todo:
        session.delete(todo)
        session.commit()
    else:
        raise HTTPException(status_code=404, detail=f"No todo with id={item_id}.")


@router.put("/{item_id}", response_model=md.ToDo)
def change_todo(item_id: int, new_data: md.ToDoInput,
                session: Annotated[Session, Depends(get_session)],
                current_user: Annotated[md.User, Depends(get_current_user)]) -> md.ToDo:
    todo: Optional[md.ToDo] = session.get(md.ToDo, item_id)
    if todo:
        todo.status = new_data.status
        todo.description = new_data.description
        session.commit()
        return todo
    else:
        raise HTTPException(status_code=404, detail=f"No todo with id={item_id}.")
