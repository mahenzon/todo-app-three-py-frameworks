from fastapi import (
    APIRouter,
    Request,
    Depends,
    Form,
    status,
    HTTPException,
)
from fastapi.responses import RedirectResponse

from sqlalchemy.orm import Session

from models import TodoItem
from models.db import get_session
from utils import templates

router = APIRouter(tags=["ToDo"])


@router.get("/", name="todo-list")
def list_todos(
    request: Request,
    session: Session = Depends(get_session),
):
    return templates.TemplateResponse(
        "index.html",
        context={
            "request": request,
            "todos": session.query(TodoItem).order_by(TodoItem.id).all(),
        },
    )


@router.post("/", name="add-todo")
def add_todo(
    request: Request,
    todo_text: str = Form(..., alias="todo-text"),
    session: Session = Depends(get_session),
):
    todo_item = TodoItem(text=todo_text)
    session.add(todo_item)
    session.commit()
    return RedirectResponse(
        url=request.url_for("todo-list"),
        status_code=status.HTTP_302_FOUND,
    )


def todo_dependency(
    todo_id: int,
    session: Session = Depends(get_session),
) -> TodoItem:
    todo: TodoItem | None = session.get(TodoItem, todo_id)
    if todo is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"ToDo #{todo_id} not found!",
        )

    return todo


@router.post("/{todo_id}/delete/", name="delete-todo")
def delete_todo(
    request: Request,
    session: Session = Depends(get_session),
    todo: TodoItem = Depends(todo_dependency),
):
    session.delete(todo)
    session.commit()

    return RedirectResponse(
        url=request.url_for("todo-list"),
        status_code=status.HTTP_302_FOUND,
    )


@router.post("/{todo_id}/toggle/", name="toggle-todo")
def toggle_todo(
    request: Request,
    session: Session = Depends(get_session),
    todo: TodoItem = Depends(todo_dependency),
):
    todo.done = not todo.done
    session.commit()

    return RedirectResponse(
        url=request.url_for("todo-list"),
        status_code=status.HTTP_302_FOUND,
    )
