from django.db import models

# Create your models here.
# new model prototype

class Profile(models.Model):
    ''' Hold the user's info registered for the app '''

    first_name = models.TextField(blank=False)
    last_name = models.TextField(blank=False)
    city = models.TextField(blank=False)
    email = models.EmailField(blank=False)
    address = models.TextField(blank=False)
    profile_image_url = models.URLField(blank=False)

    def __str__(self):
        ''' return string representation of profile object '''

        return 