## mini_fb/urls.py
## description: URL patterns for the mini facebook app

from django.urls import path
from django.conf import settings
from . import views

# all of the URLs that are part of this app
urlpatterns = [
    path(r'', views.home, name="home"),
    # path(r'about', views.about, name="about"),
    
]