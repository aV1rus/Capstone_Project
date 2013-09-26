from django import forms
from django.contrib.auth.models import User
from login.models import Profile

class SettingsFom(forms.ModelForm):

    class Meta:
        model = User
