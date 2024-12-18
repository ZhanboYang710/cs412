## mini_fb/urls.py
## description: URL patterns for the mini facebook app

from django.urls import path
from django.conf import settings
from . import views
from django.contrib.auth import views as auth_views

# all of the URLs that are part of this app
urlpatterns = [
    path(r'', views.ShowAllProfilesView.as_view(), name="show_all_profiles"),
    # path(r'about', views.about, name="about"),
    path(r'profile/<int:pk>', 
            views.ShowProfilePageView.as_view(), 
            name='show_profile'),
    path(r'create_profile',
            views.CreateProfileView.as_view(),
            name='create_profile'),
    path(r'profile/<int:pk>/create_status',
            views.CreateStatusMessageView.as_view(),
            name='create_status'),
    path(r'profile/<int:pk>/update',
            views.UpdateProfileView.as_view(),
            name='update_profile'),
    path(r'status/<int:pk>/delete',
            views.DeleteStatusMessageView.as_view(),
            name='delete_status'),
    path(r'status/<int:pk>/update',
            views.UpdateStatusMessageView.as_view(),
            name='update_status'),
    path(r'profile/<int:pk>/add_friend/<int:other_pk>',
            views.CreateFriendView.as_view(),
            name='create_friend'),
    path(r'profile/<int:pk>/friend_suggestions',
            views.ShowFriendSuggestionsView.as_view(),
            name='friend_suggestions'),
    path(r'profile/<int:pk>/news_feed',
            views.ShowNewsFeedView.as_view(),
            name='show_newsfeed'),
    path(r'login/',
            auth_views.LoginView.as_view(template_name='mini_fb/login.html'),
            name='login'),
    path(r'logout/',
            auth_views.LogoutView.as_view(next_page='show_all_profiles'),
            name='logout'),
]