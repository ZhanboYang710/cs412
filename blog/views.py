
# Create your views here.

# blog/views.py
# define the views for the blog app

from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from .models import * ## import the models (e.g., Article)
from .forms import *
from django.urls import reverse
import random

from django.contrib.auth.mixins import LoginRequiredMixin ## NEW
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login

# class-based view
class ShowAllBlogView(ListView):
    '''the view to show all Articles'''
    '''Create a subclass of ListView to display all blog articles.'''
    model = Article # the model to display
                    # retrieve objects of type Article from the database
    template_name = 'blog/show_all_blog.html'
    context_object_name = 'articles' # context variable to use in the template
                                    # how to find the data in the template file

    def dispatch(self, request):
        '''add this method to show/debug logged in user'''

        print(f"Logged in user: request.user={request.user}")
        print(f"Logged in user: request.user.is_authenticated={request.user.is_authenticated}")

        return super().dispatch(request)

## new content for 10/8/2024
class RandomArticleView(DetailView):
    '''Show the details for one article.'''
    model = Article
    template_name = 'blog/article.html'
    context_object_name = 'article'

    #  pick one article at random:
    def get_object(self):
        '''Return one Article object chosen at random.'''

        all_articles = Article.objects.all()
        return random.choice(all_articles)

## Create DetailView to show one article by its PK:
class ArticlePageView(DetailView):
    '''Show the details for one article.'''
    model = Article
    template_name = 'blog/article.html' ## reusing same template!!
    context_object_name = 'article'

# 10/10
from typing import Dict, Any

class CreateCommentView(CreateView):
    '''A view to create a new comment on an Article.
       on Get: send back the form to display.
       on POST: read/process the form, and save new Comment to the database.
    '''

    form_class = CreateCommentForm
    template_name = "blog/create_comment_form.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        '''
        Build the dict of context data for this view.
        '''

        #superclass context data
        context = super().get_context_data(**kwargs)

        # find the corresponding article
        article = Article.objects.get(pk=self.kwargs['pk'])

        # add article to context data
        context['article'] = article
        return context

    def form_valid(self, form):
        '''
        Handle the form submission. We need to set the foreign key by 
        attaching the Article to the Comment object.
        We can find the article PK in the URL (self.kwargs).
        '''

        print(form.cleaned_data)
        article = Article.objects.get(pk=self.kwargs['pk'])
        # print(article)
        form.instance.article = article
        return super().form_valid(form)

    ## show how the reverse function uses the urls.py to find the URL pattern
    def get_success_url(self) -> str:
        '''Return the URL to redirect to after successfully submitting form.'''
        #return reverse('show_all')
        return reverse('article', kwargs={'pk': self.kwargs['pk']})

        ## note: this is not ideal, because we are redirected to the main page.




# 10/17
class CreateArticleView(LoginRequiredMixin, CreateView):
    '''A view class to create a new Article instance.'''

    form_class = CreateArticleForm
    template_name = 'blog/create_article_form.html'

    def get_login_url(self) -> str:
        '''return the URL of the login page'''
        return reverse('login')

    def form_valid(self, form):
        '''This method is called as part of the form processing.'''

        print(f'CreateArticleView.form_valid(): form.cleaned_data=(form.cleaned_data)')

        # find the logged in user
        user = self.request.user
        print(f"CreateArticleView user={user} article.user={user}")

        # attach user to form instance (Article object):
        form.instance.user = user

        # let the superclass do the real work
        return super().form_valid(form)


## week Oct31
class RegistrationView(CreateView):
    ''' Handle registration of new Users. '''

    template_name = 'blog/register.html' # we write this
    form_class = UserCreationForm # built-in from django.contrib.auth.forms

    def dispatch(self, request: HttpRequest, *args:Any, **kwargs: Any) -> HttpResponse:
        ''' Handle the User creation form submission '''

        # if we received an HTTP POST, we handle it
        if self.request.POST:

            print(f'RegistrationView.dispatch: self.request.POST=(self.request.POST)')

            # reconstruct the UserCreateForm form the POST data
            form = UserCreationForm(self.request.POST) # UserCreationForm() looks for all the 
                                                       # field it needs from requst.POST dictionary

            if not form.is_valid():
                print(f'form.errors={form.errors}')

                # let CreateView.dispatch handle the problem
                return super().dispatch(request, *args, **kwargs) # return the form with the errors,
                                                                  # let user to figure it out

            # save the form, which creates a new User
            user = form.save() # this will commit the insert to the database
                                # created when the model instance is created
            print(f'RegistrationView.dispatch: created user {user}')

            # log the User in
            login(self.request, user)
            print(f'RegistationView.dispatch: {user} is logged in.')
            
            ###  note for mini_fb/: attach the FK user to the Profile form instance 
                                        # can't leave FK empty or get "No Constraint" error


            # return a response:
            return redirect(reverse('show_all'))

