from django import forms
from django.contrib.auth.models import User
from sections.user_profile.models import Profile


class SettingsForm(forms.ModelForm):

    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required= False)
    email = forms.EmailField(required=False)

    class Meta:
        model = Profile
        exclude = ('user',)

