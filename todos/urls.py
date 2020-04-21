from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_todo_items),
    path('insert_todo/', views.insert_todo, name='insert_todo'),
    path('delete_todo/<int:todo_id>/', views.delete_todo, name='delete_todo')
]
