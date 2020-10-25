from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .models import Profile, Project, Rating
from .forms import projectaddition

# Create your views here.

def home(request):

    return render(request, 'home.html')

def register(request):

    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
           
            form.save()
            
            user = request.user
            new_profile = Profile(name=user.username)
            new_profile.saveprofile()
    
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

def updateprofile(request):
    form = profileupdate()

    if request.method == "POST":
        
        user = request.user
        profile = Profile.objects.get(name=user.username)
        profile.profilepic = request.POST.get("pic")
        profile.bio = request.POST.get("bio")
        profile.Phone = request.POST.get("phone")
        profile.email = request.POST.get("email")
        profile.save()

        return redirect("home")
    
    return render(request,'profile/update.html', {"form":form})

def profilepage(request):

    user = request.user
    profile = Profile.objects.get(name=user.username)

    return render (request, 'profile/home.html', {"profile":profile})

def addproject(request):
    form = projectaddition()
    if request.method == "POST":
        form = projectaddition(request.POST)
        user = request.user
        profile = Profile.objects.get(name=user.username)
        
        if form.is_valid():
            new_project = form.save(commit=False)
            new_project.User = profile
            new_project.save()

            return redirect("home")

    return render(request, "projects/addproject.html", {"form":form})

def showproject(request):
    projects = Project.objects.all()

    return render(request, "projects/display.html")





