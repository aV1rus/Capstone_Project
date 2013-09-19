from django import forms
from login.models import User

class RegForm(forms.ModelForm):
    class meta:
        model = User
