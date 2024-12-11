from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User as AdminUser

# Create your models here.
class FilmUser(models.Model):
    ''' store data for filmuser info '''
    first_name = models.TextField(blank=False)
    last_name = models.TextField(blank=False)
    address = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    profile_picture = models.ImageField(blank=True, default='default_avatar.jpeg')

    # User profile object associated with User of admin
    adminuser = models.ForeignKey(AdminUser, on_delete=models.CASCADE) # new

    def get_film_list(self):
        "access the film_list owned by this user"
        film_list = Film_List.objects.filter(owner = self)
        return film_list

    def get_recom_list(self):
        ''' acquire a list of all the recommedations for current user '''
        
        return 

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Film(models.Model):
    ''' store data for info of each film '''
    title = models.TextField(blank=False)
    length = models.FloatField(blank=False)
    director = models.TextField(blank=False)
    image = models.ImageField(blank=True)
    starring = models.TextField(blank=True)

    def __str__(self):
        return f'{self.title} by {self.director}'

class Film_List(models.Model):
    ''' store the list of films created by a user '''
    owner = models.ForeignKey("FilmUser", on_delete=models.CASCADE)
    film = models.ForeignKey("Film", on_delete=models.CASCADE)
    rating = models.DecimalField(blank=False, max_digits=3, decimal_places=1)
    review = models.TextField(blank=True, default='')

    def clean(self):
        if self.rating > 10:
            raise ValidationError('Rating cannot exceed 10.')

    def get_list_by_user(self, user):
        filmlist = Film_List.objects.filter(owner = user)
        return filmlist

    def get_list_by_film(self, film):
        filmlist = Film.List.objects.filter(film = film)
        return filmlist

    def __str__(self):
        return f"{self.owner}'s list"

class Recommendation(models.Model):
    ''' store info for each recommendation '''
    recom_for = models.ForeignKey("FilmUser", 
                                on_delete=models.CASCADE,
                                related_name='receiver')
    recom_from = models.ForeignKey("FilmUser", 
                                on_delete=models.CASCADE,
                                related_name='provider')
    guess_you_like = models.ForeignKey("Film", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.recom_from}'s film recom for {self.recom_for}"