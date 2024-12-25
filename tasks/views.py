from django.shortcuts import render, redirect
from .forms import TaskForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger




def home(request):
    tasks = Task.objects.all()
    return render(request, 'home.html', {'tasks': tasks})

def create_task(request):
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'task_form.html',
                  {'form': form})



def update_task(request,id):
    task = get_object_or_404(Task, pk=id)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_detail', id=id)

    return render(request, 'task_form.html',
                  {'form': form,})



def delete_task(request, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()
    return redirect('home')



def detail_task(request, id):
    task = get_object_or_404(Task, pk=id)
    task.save()
    return render(request, 'task_detail.html', {'task': task})
