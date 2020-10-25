from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile, Project,Rating

class profileupdate(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['name']