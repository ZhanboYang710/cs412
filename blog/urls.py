## blog/urls.py
## description: URL patterns for the blog app

from django.urls import path
from django.conf import settings
from django.contrib.auth import views as auth_views ## NEW
from . import views

urlpatterns = [
    # map the URL (empty string) to the view
    ## new view for 'random', refactor 'show_all'
    path(r'', views.RandomArticleView.as_view(), name='random'), ## new; 10/8
    path(r'show_all_blog', views.ShowAllBlogView.as_view(), 
            name='show_all_blog'), # generic class-based view; refactored

    path(r'article/<int:pk>', views.ArticlePageView.as_view(), 
            name = 'article'), ## show one article ### NEW

    # path(r'create_comment', views.CreateCommentView.as_view(), 
            # name = 'create_comment'), ### FIRST (WITHOUT PK)

    path(r'article/<int:pk>/create_comment', views.CreateCommentView.as_view(),
            name='create_comment'), ### NEW

    path(r'create_article', views.CreateArticleView.as_view(), 
            name='create_article'), ## 10/17
    
    path(r'register/', views.RegistrationView.as_view(),
            name='register'), # 10/31

        # authentication views
    path(r'login/', auth_views.LoginView.as_view(template_name='blog/login.html'),
                name='login'), ## NEW
    path(r'logout/', auth_views.LogoutView.as_view(next_page='show_all_blog'),
                name='logout'), ## NEW
]