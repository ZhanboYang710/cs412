from django.db import models
from django.urls import reverse

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

    def get_status_messages(self):
        ''' return all the status messages for this profile '''

        messages = StatusMessage.objects.filter(profile=self).order_by('timestamp')
        return messages

    def get_absolute_url(self):
        ''' return URL to display one instance of profile '''

        return reverse('show_profile', kwargs={'pk': self.pk})


class StatusMessage(models.Model):
    ''' Hold users' status messages '''

    timestamp = models.DateTimeField(blank=False)
    message = models.TextField(blank=False)
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE)

    def __str__(self):
        ''' return a string representation of this object '''
        
        return f'{self.message}; {self.timestamp}'

    def get_images(self):
        ''' access the images associated with this status message '''
        images = Image.objects.filter(status=self)
        # print(images)
        return images


class Image(models.Model):
    ''' Store image in media directory '''

    img_file = models.ImageField(blank=True)
    timestamp = models.DateTimeField(auto_now=True)
    status = models.ForeignKey('StatusMessage', on_delete=models.CASCADE)