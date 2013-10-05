from django import forms


class CreateProjectForm(forms.Form):
    title = forms.CharField(max_length=50, required=True)
    description = forms.CharField(widget=forms.Textarea, required=True)
    file = forms.FileField(required=True)


class UploadProjectForm(forms.Form):
    description = forms.CharField(widget=forms.Textarea, required=True)
    file = forms.FileField(required=True)