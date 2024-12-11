from django import forms
from .models import *

class CreateMovieForm(forms.ModelForm):
    ''' Form a new movie '''
    class Meta: 
        model = Movie
        fields = ['title', 'length', 'director', 'image', 'starring']

class CreateUserForm(forms.ModelForm):
    ''' Form a new User '''
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'address', 'email']

class CreateMovieReviewForm(forms.ModelForm):
    ''' Form a review from a movie '''
    class Meta:
        model = Movie_List
        fields = ['rating']

