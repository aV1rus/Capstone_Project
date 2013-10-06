from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


# Create your models here.
def validate_file_extension(value):
    if not value.name.endswith('.jpg'):
        raise ValidationError('Invalid File format.')
    if not value.name.endswith('.png'):
        raise ValidationError('Invalid file Format.')

class Profile(models.Model):
    picture = models.FileField(null=True, blank=True, upload_to="profile_pictures/", validators=[validate_file_extension])
    user = models.OneToOneField(User)
    major = models.CharField(max_length=30, null=True)
    headline = models.TextField(null=True)
    #profile_picture = models.FileField(null=True,blank = True, upload_to ="/pictures")

    def __unicode__(self):
        return "Profile for User {0} {1}. Last visit on {2}".format(self.user.first_name, self.user.last_name, self.user.last_login)



