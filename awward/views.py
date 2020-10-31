from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .models import Profile, Project, Rating
from .forms import projectaddition, profileupdate
from .functions import averagingrates
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import projectSerializer,profileSerializer


# Create your views here.

@login_required(login_url= 'login/')
def home(request):
    project = Project.objects.get(id = 1)
    projects = Project.objects.all()
    projects =  projects.reverse()
    ratings = Rating.objects.filter(project=project)
    rates = averagingrates(ratings)    
    project1 = Project.objects.get(id = 1)
    

    return render(request, 'home.html', {"projects":projects,"rates":rates,"project1":project1})


def register(request):

    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
           
            form.save()
            
            user = form.cleaned_data['username']
            defaultprofile = Profile.objects.get(id = 7)
            profilepic = defaultprofile.profilepic
            new_profile = Profile(name=user, profilepic = profilepic)
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


def logoutpage(request):
    pass




@login_required(login_url= 'login/')
def updateprofile(request):
    form = profileupdate()
    user = request.user
    if request.method == "POST":
        form = profileupdate(request.POST, request.FILES)
        profile = Profile.objects.get(name=user.username)

        print(form.is_valid())
        if form.is_valid():
            profile = Profile.objects.get(name=user.username)
            profilepic = form.cleaned_data['profilepic']
            profile.profilepic = profilepic        
            profile.bio = request.POST.get("bio")
            profile.Phone = request.POST.get("phone")
            profile.email = request.POST.get("email")
            profile.save()
            

        return redirect("profilepage")
    
    return render(request,'profile/update.html', {"form":form})

@login_required(login_url= 'login/')
def profilepage(request):

    user = request.user
    profile = Profile.objects.get(name=user.username)
    projects = Project.objects.filter(User=profile)

    return render (request, 'profile/home.html', {"profile":profile, "projects":projects})


@login_required(login_url= 'login/')
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

@login_required(login_url= 'login/')
def showproject(request):
    projects = Project.objects.all()

    return render(request, "projects/display.html", {"projects":projects})



@login_required(login_url= 'login/')
def oneproject(request, id):

    project = Project.objects.get(id = id)
    ratings = Rating.objects.filter(project=project) 
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

@api_view(['GET'])
def projectsapi(request):

    projects = Project.objects.all()
    serializer = projectSerializer(projects, many = True)

    return Response(serializer.data)

@api_view(['GET'])
def singleprojectsapi(request, id):

    projects = Project.objects.get(id = id)
    serializer = projectSerializer(projects, many = False)

    return Response(serializer.data)

@api_view(['GET'])
def profilesapi(request):

    profiles = Profile.objects.all()
    serializer = profileSerializer(profiles, many = True)

    return Response(serializer.data)

@api_view(['GET'])
def singleprofilesapi(request, id):

    profiles = Profile.objects.get(id = id)
    serializer = profileSerializer(profiles, many = False)

    return Response(serializer.data)

def allendpoints(request):

    return render(request, 'endpoints.html')


def searchproject(request):
    if 'project' in request.GET and request.GET["project"]:
        searchedproject = request.GET.get("project")
        project = Project.objects.filter(Title = searchedproject)
        print(project)
    
        return render(request, 'search.html', {"projects":project})

    return render(request, 'search.html')

#login and register styling
#Rest api
#Search
