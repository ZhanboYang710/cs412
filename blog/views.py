
# Create your views here.

# blog/views.py
# define the views for the blog app
#from django.shortcuts import render
# from .models import Article
from django.views.generic import ListView
from .models import * ## import the models (e.g., Article)

# class-based view
class ShowAllBlogView(ListView):
    '''the view to show all Articles'''
    '''Create a subclass of ListView to display all blog articles.'''
    model = Article # the model to display
                    # retrieve objects of type Article from the database
    template_name = 'blog/show_all.html'
    context_object_name = 'articles' # context variable to use in the template
                                    # how to find the data in the template file
