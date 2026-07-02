from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseForbidden
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

from .models import PostModel
from .forms import CreateForm

def homePageView(request):
    posts = PostModel.objects.all()
    return render(request, "index.html", {"posts": posts})

def registerView(request):
    #if request.method == "POST":
    #    form = UserCreationForm(request.POST)
    if request.method == "GET":
        form = UserCreationForm(request.GET)
        if form.is_valid():
            form.save()
            return redirect("/accounts/login/")

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
        post = PostModel.objects.get(id=post_id)
        #if request.user.id != post.account.id:
        #    return HttpResponseForbidden()
        post.delete()
        return redirect("/")
