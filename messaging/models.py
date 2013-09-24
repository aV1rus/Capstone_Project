from django.db import models
from login.models import Profile
# Create your models here.

class PrivateMessage(models.Model):
            sender = models.ForeignKey(Profile)
            recie