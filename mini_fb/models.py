from django.db import models

# Create your models here.
# new model prototype

class Profile(models.Model):
    ''' Hold the user's info registered for the app '''

    first_name = models.TextField(blank=False)
    last_name = models.TextField(blank=False)
    city = models.TextField(blank=False)
    email_address = models.EmailField(blank=False)
    # email_address = models.TextField(blank=False)
    profile_image_url = models.URLField(blank=True)

    def __str__(self):
        ''' return string representation of profile object '''

        return f'{self.first_name} {self.last_name}'