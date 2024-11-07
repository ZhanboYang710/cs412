from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
# new model prototype

class Profile(models.Model):
    ''' Hold the user's info registered for the app '''

    user = models.ForeignKey(User, on_delete=models.CASCADE)

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

    def get_messages_lastTofirst(self):
        ''' return all messages but in order of latest to oldest '''

        messages = StatusMessage.objects.filter(profile=self).order_by('-timestamp')
        return messages

    def get_friends(self):
        ''' return a full list of friend relationships '''

        list_friend1 = Friend.objects.filter(profile1=self) 
        # if(len(list_friend1) == 0):
        #     raise Exception("no object found in list friend 1")
        friend_profiles1 = [f.profile2 for f in list_friend1]
        list_friend2 = Friend.objects.filter(profile2=self)  
        friend_profiles2 = [f.profile1 for f in list_friend2]

        firends = friend_profiles1 + friend_profiles2
        # if(len(firends) == 0):
        #     raise Exception("no object found!")
        return firends

    def add_friend(self, other):
        ''' add a friend for a profile '''
        friend = Friend.objects

        if(self == other):
            raise Exception("No self-friending")
        elif(friend.filter(profile1=self, profile2=other) | 
                friend.filter(profile1=other, profile2=self)):
                raise Exception("Frienship already existed!")
        else:
            friend.create(profile1=self, profile2=other)

        return 

    def get_friend_suggestions(self):
        ''' provide friend recommendations '''
        profile = Profile.objects
        current_friend = self.get_friends()
        cf = [i.pk for i in current_friend]
        cf.append(self.pk)
        potential_friend = profile.exclude(pk__in = cf) 

        return potential_friend

    def get_news_feed(self):
        ''' return all news feed for this profile '''
        
        friends = self.get_friends()
        news_messages = [friend.get_messages_lastTofirst() for friend in friends]

        return news_messages

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

class Friend(models.Model):
    ''' Hold friend status '''

    profile1 = models.ForeignKey('Profile', related_name="profile1", on_delete=models.CASCADE)
    profile2 = models.ForeignKey('Profile', related_name="profile2", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        ''' return a string of friend model '''
        return f'{self.profile1} & {self.profile2}'

