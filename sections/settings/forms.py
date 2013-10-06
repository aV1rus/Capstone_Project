from django import forms
from django.contrib.auth.models import User
from login.models import Profile

class SettingsForm(forms.ModelForm):

    #picture = forms.FileField(required=False)
    major = forms.CharField(required=False)
    headline = forms.CharField(widget=forms.Textarea, required=False)
    class Meta:
        model = User
        fields = ('first_name','last_name','email',)
