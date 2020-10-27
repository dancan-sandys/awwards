from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .models import Profile, Project, Rating
from .forms import projectaddition, profileupdate
from .functions import averagingrates

# Create your views here.

def home(request):
    
    projects = Project.objects.all()
    ratings = Rating.objects.all()
    rates = averagingrates(ratings)    
    project1 = Project.objects.get(id = 1)
    

    return render(request, 'home.html', {"projects":projects,"rates":rates,"project1":project1})

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
    user = request.user
    if request.method == "POST":
        form = profileupdate(request.POST, request.FILES)
        profile = Profile.objects.get(name=user.username)

        if form.is_valid():
            profile.profilepic = form.save(commit = False)
        
        
        user = request.user
        profile.bio = request.POST.get("bio")
        profile.Phone = request.POST.get("phone")
        profile.email = request.POST.get("email")
        profile.save()

        return redirect("home")
    
    return render(request,'profile/update.html', {"form":form})

def profilepage(request):

    user = request.user
    profile = Profile.objects.get(name=user.username)
    projects = Project.objects.filter(User=profile)

    return render (request, 'profile/home.html', {"profile":profile, "projects":projects})



# def addproject(request):

#     form = projectaddition()
#     if request.method == "POST":
#         form = projectaddition(request.POST)
#         if form.is_valid():
#             form.save()

#             return redirect('home')

#     return render(request, 'projects/addproject.html',{"form":form})


def addproject(request):
    form = projectaddition()
    if request.method == "POST":
        form = projectaddition(request.POST, request.FILES)
       
        
        if form.is_valid():
            user = request.user
            profile = Profile.objects.get(name=user.username)
            new_project = form.save(commit=False)
            new_project.User = profile
            new_project.save()

            return redirect("home")
        
    return render(request, "projects/addproject.html", {"form":form})

def showproject(request):
    projects = Project.objects.all()

    return render(request, "projects/display.html", {"projects":projects})

def oneproject(request, id):

    project = Project.objects.get(id = id)
    ratings = Rating.objects.all() 
    if request.method == "POST":
        creativity = request.POST.get("creativity")
        design = request.POST.get("design")
        functionality = request.POST.get("functionality")
        average = (int(creativity)+int(design)+int(functionality)) / 3
        user = request.user
        profile = Profile.objects.get(name = user.username)
        


        new_rating = Rating(Design=design, Usability = functionality, Content = creativity, Average= average,Rater= profile, project=project)
        new_rating.saverating()
    
    try:
        ratings = Rating.objects.filter(project=project)
        rates =averagingrates(ratings) 
    except:
        rates = ['No ratings','No ratings','No ratings','No ratings']

     

    return render(request, "projects/one.html", {"project":project,"rates":rates, "ratings":ratings})



# rates
# project submission
# profilepage
# login
# logout