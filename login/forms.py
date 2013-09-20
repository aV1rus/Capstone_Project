from django import forms
from login.models import Profile

class ConnectionForm(forms.Form):
    username = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'placeholder':'Username'}), label="")
    password = forms.CharField(max_length=30, widget=forms.PasswordInput(attrs={'placeholder':'Password'}),label="")
    
