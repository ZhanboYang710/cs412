## formdata/urls.py
## define the URLs for this app

from django.urls import path
from django.conf import settings
from . import views

# define a list of valid URL patterns:
urlpatterns = [
    path(r'', views.show_form, name="show_form"), 
        ## try to match up the name of the function to handle, 
        ## with the name, the template's name, and 
    path(r'submit', views.submit, name="submit"), ## new! 
]