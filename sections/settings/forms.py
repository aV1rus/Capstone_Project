from django import forms
from django.contrib.auth.models import User
from sections.user_profile.models import Profile


class SettingsForm(forms.ModelForm):

    first_name = forms.CharField(max_length=30, required=False,widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=30, required= False,widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    email = forms.EmailField(required=False,widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    headline = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Profile Headline'}),required=False)


    class Meta:
        model = Profile
        exclude = ('user','headline',)

