from django import forms


class CreateThreadForm(forms.Form):
    title = forms.CharField(max_length=50)
    body = forms.CharField(widget=forms.Textarea)
    # proj_ref = forms.InlineForeignKeyField(Projects)
    # upload_ref = forms.InlineForeignKeyField(ProjectUpdates)