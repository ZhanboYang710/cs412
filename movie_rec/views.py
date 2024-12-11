from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, View
from .models import *
from .forms import *
from django.urls import reverse
import random
from typing import Any, Dict # python version <3.9

from django.contrib.auth.mixins import LoginRequiredMixin ## NEW
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login

# Create your views here.

class ShowAllMoviesView(ListView):
    '''this is a view to display all the movies in the database'''
    '''next-stage: potentially sorting using rating or release date'''
    model = Movie
    template_name = 'movie_rec/show_all_movies.html'
    context_object_name = 'movies'

    # def dispatch(self, request):
    #     "show logged in user actions"


class MoviePageView(DetailView):
    '''this creates page for individual movie'''
    model = Movie
    template_name = 'movie_rec/show_single_movie.html'
    context_object_name = 'movie'

class CreateMovieView(LoginRequiredMixin, CreateView):
    '''this create a new movie through form interaction'''
    form_class = CreateMovieForm
    template_name = 'movie_rec/creat_movie_form.html'

    def get_login_url(self) -> str:
        '''return the URL of the login page'''
        return reverse('login')

    def form_valid(self, form):
        '''check the inputs for movie creation forms'''
        print(f'CreaetMovieView.form_valid(): form.cleanned_data = (form.cleanned_data)')
        
        return super().form_valid(form)


class ShowAllUsersView(ListView):
    '''this view handles display of all the user'''
    model = User
    template_name = 'movie_rec/show_all_users.html'
    context_object_name = 'users'

class ShowUserView(DetailView):
    '''this is a view to handle individual user's info display'''
    model = User
    template_name = 'movie_rec/show_user_profile.html'
    context_object_name = 'user'

class CreateUserView(CreateView):
    ''' view to handle form to create new User '''
    form_class = CreateUserForm
    template_name = 'movie_rec/create_user_form.html'
    
    # def get_login_url(self) -> str:
    #     ''' return URL for login '''
    #     return reverse('login')

    def form_valid(self, form):
        ''' check the inputs for form '''
        print(f'CreaetUserView.form_valid(): form.cleanned_data = (form.cleanned_data)')

        return super().form_valid(form)

    def get_context_data(self, **kwargs: Any): 

        return


class ShowUserMovieListView(ListView):
    '''display the movies in the movie list of the designated user'''
    model = Movie_List
    template_name = 'movie_rec/show_user_movie_list.html'
    context_object_name = 'movielist'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        ''' retrieve the associated user'''
        # first, retireve superclass context
        context = super().get_context_data(**kwargs)

        # secondly, locate specific profile
        this_user = User.objects.get(pk = self.kwargs['pk'])

        # finally, update the context array
        context['user'] = this_user
        context['movie_list'] = Movie_List.objects.filter(owner = this_user)
        context['list_type'] = type(context['movie_list']).__name__  # Add type of list
        return context

class ShowMovieReviewView(DetailView):
    '''display each movie review of movies in the user's list'''
    model = Movie_List
    template_name = 'movie_rec/show_user_movie_review.html'
    context_object_name = 'movie_review'


# below is creating movie_list object
class CreateMovieReviewMovieView(LoginRequiredMixin, CreateView):
    '''create movie_list from a movie interface '''
    form_class = CreateMovieReviewForm
    template_name = 'movie_rec/create_movie_form_movie.html'


class RegistrationView(CreateView):
    '''Handle registration'''
    form_class = UserCreationForm # builtin from django.contrib.auth.forms
    template_name = 'movie_rec/register.html'

    def dispatch(self, request, *args, **kwargs):
        '''dispatch method'''
        if self.request.POST:
            print(f'RegistrationView.dispatch: self.request.POST={self.request.POST}')
            # reconstruct the UserCreateForm from the POST data
            form = UserCreationForm(self.request.POST)

            if not form.is_valid():
                print(f"form.errors={form.errors}")

                ## Let someonebody else fix it
                return super().dispatch(request, *args, **kwargs)

            # save the form, which creates a new User
            user = form.save() #this will commit the insert to the database
            print(f"registrationView.dispatch: created user {user}.")

            # log the User in
            login(self.request, user)
            print(f"RegistrationView.dispatch: {user} is logged in.")

            User.objects.create(user=user, first_name=request.POST['first_name'], last_name=request.POST['last_name'], city=request.POST['city'], email_address=request.POST['email_address'], image_file=request.FILES.get('image_file'), )
            
            # return a message: 
            return redirect(reverse('show_all_profiles'))


        ## Let CreateView.dispatch handle the HTTP GET request
        return super().dispatch(request, *args, **kwargs)