from django import forms


class CreateProjectForm(forms.Form):
    title = forms.CharField(max_length=50)
    description = forms.CharField(widget=forms.Textarea)
    file = forms.FileField(required=False)


class UploadProjectForm(forms.Form):
    description = forms.CharField(widget=forms.Textarea)
    file = forms.FileField(required=False)