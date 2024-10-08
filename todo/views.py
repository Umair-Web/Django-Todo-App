from django.shortcuts import render,redirect
from .models import Todos
def todoList(request):
    todos=Todos.objects.order_by('-id')
    return render(request,'todo/index.html',{'todos':todos})


def home_page(request):
    return redirect("todoList")


def create_todo(request):
    if request.method=='POST':
        title=request.POST.get('title')

        desc=request.POST.get('description')

        Todos.objects.create(title=title,desc=desc)
    return redirect("todoList")

def complete_todo(request,todo_id):
    todo=Todos.objects.get(id=todo_id)
    todo.completed=True
    todo.save()
    return redirect("todoList")

def delete_todo(request,todo_id):
    todo=Todos.objects.get(id=todo_id)
    todo.delete()
    return redirect("todoList")