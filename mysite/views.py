from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseForbidden
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
from django.db import connection

from .models import PostsModel, PrivateNotesModel
from .forms import CreateForm

def homePageView(request):
    posts = PostsModel.objects.all()
    return render(request, "index.html", {"posts": posts})

def privateNotesView(request):
    if request.method == "POST":
        content = request.POST["content"]
        print("update or create")
        PrivateNotesModel.objects.update_or_create(account=request.user, defaults={"content":content})
    try:
        notes=PrivateNotesModel.objects.get(account=request.user).content
    except PrivateNotesModel.DoesNotExist:
        notes=""
    return render(request, "private_notes.html", {"notes": notes})

def userView(request,user_id):
    user = User.objects.get(id=user_id)
    posts = PostsModel.objects.filter(account=user)
    return render(request, "user.html", {"posts": posts, "user_id": user_id, "username": user.username})

def searchUserView(request):
    if request.method == "POST":
        query = request.POST["query"]
        ### SQL INJECTION
        #fixed code:
        #r=User.objects.filter(username__contains=query)

        #vulnerable code:
        with connection.cursor() as cur:
            res=cur.execute(f"SELECT id, username FROM auth_user WHERE username LIKE '%{query}%'")
            r=[{"id": q[0],"username": q[1]} for q in res.fetchall()]
        #^vulnerable code
    else:
        r=None
    return render(request, "search_user.html", {"results":r})

def registerView(request):
    #if request.method == "POST":
    #    form = UserCreationForm(request.POST)
    if request.method == "GET":
        form = UserCreationForm(request.GET)
        if form.is_valid():
            form.save()
            return redirect("/login/")

    return render(request, "register.html", {"form": UserCreationForm()})

def createView(request):
    if request.method == "POST":
        form = CreateForm(request.POST)
        if form.is_valid():
            form.save(request.user)
    return render(request, "create.html", {"form": CreateForm()})

def deleteView(request):
    if request.method == "POST":
        post_id = request.POST["id"]
        post = PostsModel.objects.get(id=post_id)
        #if request.user.id != post.account.id:
        #    return HttpResponseForbidden()
        post.delete()
        return redirect("/")
