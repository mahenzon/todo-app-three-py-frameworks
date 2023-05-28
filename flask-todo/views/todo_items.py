from flask import render_template, request, redirect, url_for, flash, Blueprint

from models import db, TodoItem

todo_app = Blueprint("todo_app", __name__)


@todo_app.get("/", endpoint="list")
def todos_list():
    todos = db.session.query(TodoItem).order_by(TodoItem.id).all()
    return render_template("index.html", todos=todos)


@todo_app.post("/")
def add_todo():
    text = request.form.get("todo-text")
    if text:
        todo = TodoItem(text=text)
        db.session.add(todo)
        db.session.commit()
    else:
        flash("error, text not passed")
    return redirect(url_for("todo_app.list"))


@todo_app.post("/<int:todo_id>/toggle/", endpoint="toggle")
def toggle_todo(todo_id: int):
    todo: TodoItem = db.get_or_404(TodoItem, todo_id)
    todo.done = not todo.done
    db.session.commit()
    return redirect(url_for("todo_app.list"))


@todo_app.post("/<int:todo_id>/delete/", endpoint="delete")
def delete_todo(todo_id: int):
    todo: TodoItem = db.get_or_404(TodoItem, todo_id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("todo_app.list"))
