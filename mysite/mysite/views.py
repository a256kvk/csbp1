from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

def homePageView(request):
    username = request.user.username
    return render(request, "index.html", {"un": username})

def registerView(request):
    #if request.method == "POST":
    #    form = UserCreationForm(request.POST)
    if request.method == "GET":
        form = UserCreationForm(request.GET)
        if form.is_valid():
            form.save()
            return redirect("/accounts/login/")

    return render(request, "register.html", {"form": UserCreationForm()})
