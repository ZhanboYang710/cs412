## urls.py
## description: URL patterns for the hw app

from django.urls import path
from django.conf import settings
from . import views                     ## from the current directory import views file

# all of the urls that are a part of this app
urlpatterns = [
    path(r'', views.home, name="home"),  ## this attach a func to handle the url
    path(r'about', views.about, name="about"),
]