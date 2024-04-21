from django.shortcuts import render, get_object_or_404, redirect
from add.models import Todo
from add.form import TodoForm
from django.contrib import messages


# Create your views here.


def todo_list(request):
    todos = Todo.objects.all()
    search = request.GET.get('search')
    if search:
        todos = Todo.objects.filter(name__icontains=search)
    context = {'todos': todos}
    return render(request, 'todo_list.html', context)


def todo_detail(request, pk):
    todo = get_object_or_404(Todo, id=pk)
    form = TodoForm(request.POST or None, instance=todo)
    if form.is_valid():
        form.save()
        return redirect('todo_list')
    context = {'todo': todo, 'form': form}
    return render(request, 'todo_detail.html', context)


def todo_create(request):
    form = TodoForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Todo has been created!')
        return redirect('/')
    context = {'form': form}
    return render(request, 'todo_create.html', context)


def todo_delete(request, pk):
    todo = get_object_or_404(Todo, id=pk)
    if request.method == 'POST':
        todo.delete()
        messages.success(request, 'Todo has been deleted')
        return redirect('/')
    context = {'todo': todo}
    return render(request, 'todo_delete.html', context)


def todo_edit(request, pk):
    todo = get_object_or_404(Todo, id=pk)
    form = TodoForm(request.POST or None, instance=todo)
    if form.is_valid():
        form.save()
        redirect(request, 'todo_detail', id=pk)
    context = {'todo': todo, 'form': form}
    return render(request, 'todo_edit.html', context)
