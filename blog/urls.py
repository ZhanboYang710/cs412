## blog/urls.py
## description: URL patterns for the blog app

from django.urls import path
#from .views import ShowAllBlogView # our view class definition 
from .views import *

urlpatterns = [
    # map the URL (empty string) to the view
    ## new view for 'random', refactor 'show_all'
    path('', RandomArticleView.as_view(), name='random'), ## new; 10/8
    path('show_all_blog', ShowAllBlogView.as_view(), name='show_all_blog'), # generic class-based view; refactored
    path('article/<int:pk>', ArticlePageView.as_view(), name = 'article'), 
        ## show one article ### NEW
    path('create_comment', CreateCommentView.as_view(), name = 'create_comment'), 
        ### FIRST (WITHOUT PK)
    path('article/<int:pk>/create_comment', CreateCommentView.as_view(), name='create_comment'),
        ### NEW
]