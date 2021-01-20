from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Todos,Project
from .forms import ListForm,ProjectForm
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
# Create your views here.


def create(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)
        if form.is_valid:
            form.save()
            return redirect("projects")
            #todo_list = Todos.objects.all()
            #project_list=Project.objects.all()
            #return render(request,'todo_app/create.html',{'todo_list':todo_list,'project_list':project_list})
            
    else:
        todo_list = Todos.objects.all()
        project_list=Project.objects.all()
        return render(request,'todo_app/create.html',{'todo_list':todo_list,'project_list':project_list})

def createproject(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("projects")
            #project_list=Project.objects.all()
            #return render(request,'todo_app/createproject.html',{'project_list':project_list})
    else:
        project_list=Project.objects.all()
        return render(request,'todo_app/createproject.html',{'project_list':project_list})

def deleteTodos(request,Todos_id):
    todo = Todos.objects.get(pk=Todos_id)
    todo.delete()
    return redirect("projects")

def deleteProject(request,Project_id):
    project = Project.objects.get(pk=Project_id)
    project.delete()
    return redirect("projects")

def yes_finish(request,Todos_id):
    todo = Todos.objects.get(pk=Todos_id)
    todo.finished=False
    todo.save()
    return redirect("projects")

def no_finish(request,Todos_id):
    todo = Todos.objects.get(pk=Todos_id)
    todo.finished=True
    todo.save()
    return redirect("projects")

def update(request,Todos_id):
    if request.method == 'POST':
        todo_list=Todos.objects.get(pk=Todos_id)
        form = ListForm(request.POST or None,instance=todo_list)
        if form.is_valid:
            todo_list.title=request.POST.get("title")
            todo_list.technical_specialist=request.POST.get("technical_specialist")
            todo_list.notes=request.POST.get("notes")
            todo_list.description=request.POST.get("description")
            todo_list.save()
            return redirect("projects")
    else:
        todo_list = Todos.objects.filter(id=Todos_id)
        project_list=Project.objects.all()
        return render(request,'todo_app/update.html',{'todo_list':todo_list,'project_list':project_list})

def calculate(request,Todos_id):
        td=Todos.objects.get(pk=Todos_id)
        separate=td.description.split()
        a=0
        for word in separate:
            a=a+1
        estimated_time=a*3
        td.estimated_elapsed_time=estimated_time
        td.save()
        return redirect("projects")

def todoUpdate(request):
    if request.POST:
        cardID = request.POST.getlist('cardID')[0]
        listID = request.POST.getlist('listID')[0]
        todo = Todos.objects.filter(id=cardID).update(status=listID)
        todo.save()

    return redirect("projects")

def projects(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)
        if form.is_valid:
            form.save()
            return redirect("projects")
            #project_list = Project.objects.all()
            #return render(request,'todo_app/index.html',{'project_list':project_list})
    else:
        project_list = Project.objects.all()
        return render(request,'todo_app/projects.html',{'project_list':project_list})

def detailProject(request,Project_id):
    todo_list = Todos.objects.all().filter(project_name=Project_id)
    return render(request,'todo_app/detail.html',{'todo_list':todo_list})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'todo_app/signup.html', {'form': form})
 
 
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('projects')
    else:
        form = AuthenticationForm()
    return render(request, 'todo_app/login.html', {'form': form})
 
 
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        form = AuthenticationForm()
    return redirect('login')