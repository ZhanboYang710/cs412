from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import *

# Create your views here.
class ShowAllProfilesView(ListView):
    '''subclass of ListView to show all the profiles'''
    model = Profile
    template_name = 'mini_fb/show_all_profiles.html'
    context_object_name = 'profiles' 
        # context variables refering to Profile objects

class ShowProfilePageView(DetailView):
    '''subclass of DetailView to show individual profile page'''
    model = Profile
    template_name = 'mini_fb/show_profile.html'
    context_object_name = 'profile'


class CreateProfileView(CreateView):
    form_class = CreateProfileForm
    template_name = 'mini_fb/create_profile_form.html'

    def form_valid(self, form):
        ''' check the inputs for profile-creating form '''
        print(f'CreateProfileView.form_valid(): form.cleaned_data=(form.cleaned_data)')

        return super().form_valid(form)

from typing import Any, Dict
#
class CreateStatusMessageView(CreateView):
    form_class = CreateStatusMessageForm
    template_name = 'mini_fb/create_status_form.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        ''' retrieve the associated profile this creation of status belong to '''
        # first, retireve superclass context
        context = super().get_context_data(**kwargs)

        # secondly, locate specific profile
        this_profile = Profile.objects.get(pk = self.kwargs['pk'])

        # finally, update the context array
        context['profile'] = this_profile
        return context

    def form_valid(self, form):
        ''' check the inputs for status-creating form '''
        this_profile = Profile.objects.get(pk = self.kwargs['pk'])
        print(self.kwargs['pk'])
        form.instance.profile = this_profile

        # save the status message to database
        sm = form.save()

        # read the file from the form:
        files = self.request.FILES.getlist('files')

        # create Image objects to obtain files and save in DB
        for f in files:
            new_image = Image.objects.create(img_file=f, status=sm)
            Image.save(new_image)

        return super().form_valid(form)

    def get_success_url(self) -> str:
        ''' redirecting url after sucess creation of status '''

        return reverse('show_profile', kwargs={'pk': self.kwargs['pk']})


class UpdateProfileView(UpdateView):
    ''' update profiles '''
    model = Profile
    
    form_class = UpdateProfileForm
    template_name = 'mini_fb/update_profile_form.html'

    
class DeleteStatusMessageView(DeleteView):
    ''' Delete a Status Message '''
    model = StatusMessage
    template_name = 'mini_fb/delete_status_form.html'
    context_object_name = 'status'

    def get_success_url(self): 
        return reverse('show_profile', kwargs={'pk': self.object.profile.pk})

class UpdateStatusMessageView(UpdateView):
    ''' Update a status message '''
    model = StatusMessage
    form_class = UpdateStatusMessageForm
    template_name = 'mini_fb/update_status_form.html'

    def get_success_url(self):
        return reverse('show_profile', kwargs={'pk': self.object.profile.pk})

