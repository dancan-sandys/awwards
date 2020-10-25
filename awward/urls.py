from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.home, name='home'),
    url('register/$', views.register, name='register'),
    url('login/$', views.loginpage, name='login'),
    url('profile/update/$', views.updateprofile, name='updateprofile')

]