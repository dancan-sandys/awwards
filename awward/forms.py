from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile, Project,Rating

class projectaddition(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['User']

class profileupdate(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profilepic']
        