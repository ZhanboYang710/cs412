## blog/urls.py
## description: URL patterns for the blog app

from django.urls import path
from .views import ShowAllBlogView # our view class definition 

urlpatterns = [
    # map the URL (empty string) to the view
    path(r'', ShowAllBlogView.as_view(), name='show_all_blog'), # generic class-based view
]