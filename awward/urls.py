from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.home, name='home'),
    url('register/$', views.register, name='register'),
    url('login/$', views.loginpage, name='login'),
    url('profile/update/$', views.updateprofile, name='updateprofile'),
    url('profile/home/$', views.profilepage, name='profilepage'),
    url('project/add/$', views.addproject, name="addproject"),
    url('projects/$', views.showproject, name='projects'),
    url('project/single', views.oneproject, name='single'),
]