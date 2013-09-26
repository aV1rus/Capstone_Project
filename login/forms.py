from django import forms


class ConnectionForm(forms.Form):
    username = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'placeholder':'Username'}), label="")
    password = forms.CharField(max_length=30, widget=forms.PasswordInput(attrs={'placeholder':'Password'}),label="")
    
class RegistrationForm(forms.Form):
    email = forms.EmailField(max_length=30, label="", widget=forms.TextInput(attrs={'placeholder':'Email'}))
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder':'Username'}), label="")
    password = forms.CharField(max_length=30, widget=forms.PasswordInput(attrs={'placeholder':'Password'}),label="")
    password_confirm = forms.CharField(max_length=30, widget=forms.PasswordInput(attrs={'placeholder':'Reenter password'}),label="")

