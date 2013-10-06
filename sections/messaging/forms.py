from django import forms
from sections.messaging.models import PrivateMessage


class Compose(forms.ModelForm):
    class Meta:
        model = PrivateMessage
        fields =('receiver','content',)