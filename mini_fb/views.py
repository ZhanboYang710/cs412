from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView
from .models import *

# Create your views here.
class ShowAllProfilesView(ListView):
    '''subclass of ListView to show all the profiles'''
    model = Profile
    template_name = 'mini_fb/show_all_profiles.html'
    context_object_name = 'profiles' 
        # context variables refering to Profile objects