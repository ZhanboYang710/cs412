from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User as AdminUser

# Create your models here.
class User(models.Model):
    ''' store data for user info '''
    first_name = models.TextField(blank=False)
    last_name = models.TextField(blank=False)
    address = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    profile_picture = models.ImageField(blank=True, default='default_avatar.jpeg')

    # User profile object associated with User of admin
    adminuser = models.ForeignKey(AdminUser, on_delete=models.CASCADE) # new

    def get_user_byId(self, id):
        user = User.objects.filter(pk = id)
        return user

    def get_movie_list(self):
        "access the movie_list owned by this user"
        movie_list = Movie_List.objects.filter(owner = self)
        return movie_list

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Movie(models.Model):
    ''' store data for info of each movie '''
    title = models.TextField(blank=False)
    length = models.FloatField(blank=False)
    director = models.TextField(blank=False)
    image = models.ImageField(blank=True)
    starring = models.TextField(blank=True)

    def __str__(self):
        return f'{self.title} by {self.director}'

class Movie_List(models.Model):
    ''' store the list of movies created by a user '''
    owner = models.ForeignKey("User", on_delete=models.CASCADE)
    movie = models.ForeignKey("Movie", on_delete=models.CASCADE)
    rating = models.DecimalField(blank=False, max_digits=3, decimal_places=1)
    review = models.TextField(blank=True, default='')

    def clean(self):
        if self.rating > 10:
            raise ValidationError('Rating cannot exceed 10.')

    def get_list_by_user(self, user):
        movielist = Movie_List.objects.filter(owner = user)
        return movielist

    def get_list_by_movie(self, movie):
        movielist = Movie.List.objects.filter(movie = movie)
        return movielist

    def __str__(self):
        return f"{self.owner}'s list"

class Recommendation(models.Model):
    ''' store info for each recommendation '''
    recom_for = models.ForeignKey("User", 
                                on_delete=models.CASCADE,
                                related_name='receiver')
    recom_from = models.ForeignKey("User", 
                                on_delete=models.CASCADE,
                                related_name='provider')
    guess_you_like = models.ForeignKey("Movie", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.recom_from}'s movie recom for {self.recom_for}"