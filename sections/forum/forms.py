from django import forms
from sections.projects.models import Projects, ProjectUpdates


class CreateThreadForm(forms.Form):
    title = forms.CharField(max_length=50)
    body = forms.CharField(widget=forms.Textarea)
    # proj_ref = forms.InlineForeignKeyField(Projects)
    # upload_ref = forms.InlineForeignKeyField(ProjectUpdates)