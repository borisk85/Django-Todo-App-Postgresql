from django.shortcuts import render, redirect
from .models import Todo


# Create your views here.


def list_todo_items(request):
    context = {'todo_list': Todo.objects.all()}
    return render(request, 'todos/index.html', context)


def insert_todo(request):
    todo = Todo(content=request.POST['content'])
    todo.save()
    return redirect('/')


def delete_todo(request, todo_id):
    todo_to_delete = Todo.objects.get(id=todo_id)
    todo_to_delete.delete()
    return redirect('/')
