from django.urls import path

from .views import (
    ToDoItemsListView,
    ToDoItemCreateView,
    ToDoItemDeleteView,
    ToDoItemToggleView,
)

app_name = "todo-list"

urlpatterns = [
    path("", ToDoItemsListView.as_view(), name="items-list"),
    path("create/", ToDoItemCreateView.as_view(), name="create-item"),
    path("<int:pk>/confirm-delete/", ToDoItemDeleteView.as_view(), name="delete-item"),
    path("<int:pk>/toggle/", ToDoItemToggleView.as_view(), name="toggle-item"),
]
