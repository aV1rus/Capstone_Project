from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from home.models import Major


# Create your models here.
def validate_file_extension(value):
    if not value.name.endswith('.jpg'):
        raise ValidationError('Invalid File format.')
    if not value.name.endswith('.png'):
        raise ValidationError('Invalid file Format.')


class Profile(models.Model):
    picture = models.FileField(null=True, blank=True, upload_to="user_photos/", default='defaults/default_profile_pic.jpg')#, validators=[validate_file_extension]) #, default='defaults/default_profile_pic.jpg'
    user = models.OneToOneField(User)
    major = models.ForeignKey(Major, null=True, blank=True)
    headline = models.TextField(null=True, blank=True)
    # profile_picture = models.FileField(null=True, blank=True, upload_to="user_photos", default='defaults/default_profile_pic.jpg')

    def __unicode__(self):
        return "Profile for User {0} {1} <{3}>. Last visit on {2}".format(self.user.first_name, self.user.last_name, self.user.last_login, self.user.username)
