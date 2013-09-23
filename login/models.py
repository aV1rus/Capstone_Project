from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User)
    #picture = models.ImageField(null=True,blank = True, upload_to ="/pictures")

    def __unicode__(self):
        return "Profile for User {0} {1}. Last visit on {2}".format(self.user.first_name, self.user.last_name,self.user.last_login)


