from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required
import json
from django.utils import timezone, timesince

def index(request):
    content = {}
    if request.user.is_authenticated:

        todolists = TodoList.objects.filter(owner=request.user)
        todos = {}

        for todolist in todolists:
            gettodos = Todo.objects.filter(todolist=todolist)
            todos[todolist.name] = gettodos

        content = {
            "todolists": TodoList.objects.filter(owner=request.user),
            "todos": todos,
            }

    return render(request, "todo/index.html", content)


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            messages.error(request,"Invalid username and/or password.")
    
    return render(request, "todo/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):

    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            messages.error(request, "Passwords must match.")
            return render(request, "todo/register.html")

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            messages.error(request, "Username already taken.")
            return render(request, "todo/register.html")
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "todo/register.html")

def createlist(request):

    if request.method == "POST":

        listcount = len(TodoList.objects.filter(owner=request.user))
        listcount = listcount+1 if listcount != 0 else "" #ith list item (For ex: New List 5)

        name = request.POST["addnewlist"]
        name = f"New List {listcount}" if name == "" else name #if list item textbox is null then 

        newlist = TodoList.objects.create(name=name, owner=request.user)
        newlist.save()

    return HttpResponseRedirect(reverse('index'))

@login_required
@csrf_exempt
def delete(request,id):

    if request.method == 'PUT':

        data = json.loads(request.body)

        if data.get("type","") == "deletelist":

            getlist = TodoList.objects.get(id=id)
            getlist.delete()

        elif data.get("type","") == "deletetodo":

            gettodo = Todo.objects.get(id=id)
            gettodo.delete()

    return HttpResponse(status=204)
            
@login_required
@csrf_exempt
def updatestatus(request):

    if request.method == "PUT":

        data = json.loads(request.body)
        todoid = data.get("todoid","")
        status = data.get("typevalue","")

        if data.get("type","") == "status":

            getlist = Todo.objects.get(id=todoid)
            getlist.status= True if status == "True" else False
            getlist.save()

        return HttpResponse(status=204)

@login_required
def add(request, id):

    if request.method == "POST":

        todolist = TodoList.objects.get(id=id)
        name = request.POST["name"]
        description = request.POST["description"]
        status = True if "status" in request.POST else False 
        deadline = request.POST["deadline"]

        todo = Todo.objects.create(todolist=todolist, name=name, description=description, status=status, deadline=deadline)
        todo.save()

        return HttpResponseRedirect(reverse('index'))


@login_required
def filter(request, filter, id):
    content = {}

    if request.user.is_authenticated:

        todolists = TodoList.objects.filter(owner=request.user)
        todos = {}

        for todolist in todolists:

            if todolist.id == id:

                if filter == "completed":
                    todos[todolist.name] =  Todo.objects.filter(todolist=todolist, status=True)

                elif filter == "notcompleted":
                    todos[todolist.name] =  Todo.objects.filter(todolist=todolist, status=False)

                elif filter == "expired":
                    temptodos = Todo.objects.filter(todolist=todolist)
                    results = list()

                    for temptodo in temptodos:
                        timediff=timesince.timeuntil(temptodo.deadline).split(',')[0]

                        if timediff=="0\xa0minutes":
                            results.append(temptodo)

                    todos[todolist.name] = results 
            else:
                todos[todolist.name] =  Todo.objects.filter(todolist=todolist)

        content = {
            "todolists": TodoList.objects.filter(owner=request.user),
            "todos": todos,
            }

    return render(request, "todo/index.html", content)

@login_required
def order(request, ordering, id):

    content = {}

    if request.user.is_authenticated:

        todolists = TodoList.objects.filter(owner=request.user)
        todos = {}

        for todolist in todolists:

            if todolist.id == id:

                if ordering == "ascending":
                    todos[todolist.name] =  Todo.objects.filter(todolist=todolist).order_by('-name')

                elif ordering == "descending":
                    todos[todolist.name] =  Todo.objects.filter(todolist=todolist).order_by('name')

                elif ordering == "created":
                    todos[todolist.name] =  Todo.objects.filter(todolist=todolist).order_by('created_at')

                elif ordering == "deadline":
                    todos[todolist.name] =  Todo.objects.filter(todolist=todolist).order_by('deadline')

                elif ordering == "completed":
                    todos[todolist.name] =  Todo.objects.filter(todolist=todolist).order_by('-status')

                elif ordering == "notcompleted":
                    todos[todolist.name] =  Todo.objects.filter(todolist=todolist).order_by('status')

            else:
                todos[todolist.name] =  Todo.objects.filter(todolist=todolist)

        content = {
            "todolists": TodoList.objects.filter(owner=request.user),
            "todos": todos,
            }

    return render(request, "todo/index.html", content)
