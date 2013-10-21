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

    def __unicode__(self):
        return "Profile for User {0} {1} <{3}>. Last visit on {2}".format(self.user.first_name, self.user.last_name, self.user.last_login, self.user.username)



# This will be ignored for time being because we should consider making EVERYONE friends by default or ignoring the friend factor since we all go to same school...
# EXAMPLE :: At work I can see everyone's profile that works for the company
#
# class Friends(models.Model):
#     user_1 = models.ForeignKey(User)
#     user_2 = models.ForeignKey(User)
#
#     def __unicode__(self):
#         return "{0} {1}".format(self.user_1.first_name, self.user_2.first_name)
