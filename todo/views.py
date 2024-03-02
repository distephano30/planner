from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import logout, login
from .models import todo
from .forms import todoForm, RegisterForm
import datetime

# from django.db.models.lookups import GreaterThan, LessThan
# Create your views here.
@login_required
def index(request):
    todo_overdue = todo.objects.filter(due_date__lte = datetime.date.today() - datetime.timedelta(days=1)).filter(assign_to = request.user)
    todo_upcoming = todo.objects.filter(due_date__gte = datetime.date.today()).filter(assign_to = request.user)
    todo_completed = todo.objects.filter(progress__icontains = 'completed').filter(assign_to = request.user)
    todo_all = todo.objects.exclude(progress__icontains = 'completed')
    my_tasks = todo.objects.filter(assign_to = request.user).exclude(progress__icontains = 'completed')
 
    if request.method == 'POST':
        form = todoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    
    form = todoForm()
    context = {
        'form': form,
        'list': todo_all,
        'upcoming': todo_upcoming,
        'overdue': todo_overdue,
        'completed': todo_completed,
        'my_tasks' : my_tasks
    }
    return render(request, 'index.html', context)

def edit_task(request, id):
    queryset = todo.objects.filter(assign_to = request.user)
    task = get_object_or_404(queryset, pk=id)
    
    if request.method == 'GET':
        context = { 'form': todoForm(instance=task), 'id': id}
        return render(request, 'edit_task.html', context )
    elif request.method == 'POST':
        form = todoForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return render(request, 'edit_task.html', {'form': form})

def delete_task(request, id):
    queryset = todo.objects.filter(assign_to = request.user)
    task = get_object_or_404(queryset, pk=id)

    context = {'task': task}
    if request.method == 'GET':
        return render(request, 'delete_task.html', context)
    elif request.method == 'POST':
        task.delete()
        return redirect('index')

def sign_up(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'registration/register.html', {'form': form})
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'User registration completed successfully')
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'registration/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')