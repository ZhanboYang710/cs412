from django import forms
from .models import Profile, StatusMessage

class CreateProfileForm(forms.ModelForm):
    ''' Form to add a new profile '''

    class Meta:
        ''' associating this form with a class, select fields '''
        model = Profile
        fields = ['first_name', 'last_name', 'city', 
                    'email_address', 'profile_image_url',]

class CreateStatusMessageForm(forms.ModelForm):
    ''' Form to add status message '''

    timestamp = forms.SplitDateTimeField(label="Premiee Date/time")

    class Meta:
        ''' associating this form to class StatusMessage, select fields '''
        model = StatusMessage
        fields = ['timestamp', 'message',]
    
class UpdateProfileForm(forms.ModelForm):
    ''' Form to update existing profile '''

    class Meta:
        model = Profile
        fields = [ 'city', 'email_address', 'profile_image_url',]

class UpdateStatusMessageForm(forms.ModelForm):
    ''' Form to update existing status message '''
    class Meta:
        model = StatusMessage
        fields = ['timestamp', 'message',]