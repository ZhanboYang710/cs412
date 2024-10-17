
# Create your views here.

# blog/views.py
# define the views for the blog app
#from django.shortcuts import render
# from .models import Article
from django.views.generic import ListView, DetailView
from .models import * ## import the models (e.g., Article)
import random

# class-based view
class ShowAllBlogView(ListView):
    '''the view to show all Articles'''
    '''Create a subclass of ListView to display all blog articles.'''
    model = Article # the model to display
                    # retrieve objects of type Article from the database
    template_name = 'blog/show_all_blog.html'
    context_object_name = 'articles' # context variable to use in the template
                                    # how to find the data in the template file

##
## new content for 10/8/2024
##
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

### 
# 10/10
###
from django.views.generic.edit import CreateView
from django.urls import reverse

from .forms import CreateCommentForm

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

