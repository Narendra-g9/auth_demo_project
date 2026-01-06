from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 
from django.contrib.auth.decorators import login_required 

def home(request):
    return render(request, "app1/home.html") 

def register_view(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registration successful.")
            return redirect("login")
        messages.error(request,"Fix errors.")
    else:
        form=UserCreationForm()
    return render(request,"app1/register.html",{"form":form})

def login_view(request):
    if request.method=="POST":
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user=authenticate(username=form.cleaned_data["username"],password=form.cleaned_data["password"])
            if user:
                login(request,user)
                return redirect("details")
        messages.error(request,"Invalid credentials.")
    else:
        form=AuthenticationForm()
    return render(request,"app1/login.html",{"form":form})

def logout_view(request):
    logout(request)
    return redirect("home")

@login_required(login_url="login")
def details(request):
    return render(request,"app1/details.html")
