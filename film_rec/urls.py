from django.urls import path
from django.conf import settings
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path(r'', views.ShowAllMoviesView.as_view(), name="show_all_movies"),
    path(r'show_all', views.ShowAllMoviesView.as_view(), name="show_all_movies"),
    path(r'show_single_film/<int:pk>', views.MoviePageView.as_view(), name="show_single_movie"),

    path(r'users', views.ShowAllUsersView.as_view(), name="show_all_users"),
    path(r'user/<int:pk>', views.ShowUserView.as_view(), name="show_user_profile"),
    path(r'user/<int:pk>/movie_list', views.ShowUserMovieListView.as_view(), name="show_user_movie_list"),
    path(r'user/<int:user_id>/movie_list/<int:movie_id>', views.ShowMovieReviewView.as_view(), name="show_user_movie_review"),
]