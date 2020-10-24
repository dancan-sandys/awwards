from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate


# Create your views here.

def home(request):

    return render(request, 'home.html')

def register(request):

    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    
            return redirect('home')

    return render(request, 'accounts/register.html',{"form":form})

def loginpage(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)

            return redirect('home')

        else:
            
            message = 'The username or password you entered is incorrect'
            username = request.POST.get("username")
            return render(request, 'accounts/login.html', {"message": message,"username":username})


    return render(request, 'accounts/login.html')