from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'register/$', views.register, name='register'),
    url(r'login/$', views.loginpage, name='login'),
    url(r'profile/update/$', views.updateprofile, name='updateprofile'),
    url(r'profile/home/$', views.profilepage, name='profilepage'),
    url(r'project/add/$', views.addproject, name="addproject"),
    url(r'projects/$', views.showproject, name='projects'),
    url(r'project/single/(\d+)$', views.oneproject, name='single'),
    url(r'projects/api/$', views.projectsapi, name='projectsapi'),
    url(r'profiles/api/$', views.profilesapi, name='profilesapi'),
    url(r'project/api/(\d+)$', views.singleprojectsapi, name='singleprojectsapi'),
    url(r'profile/api/(\d+)$', views.singleprofilesapi, name='singleprofilesapi'),
    url(r'endpoints/$', views.allendpoints, name='endpoints'),
    url(r'searchproject/$', views.searchproject, name='searchproject'),

    
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)