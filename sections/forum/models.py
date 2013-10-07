from django.db import models
from django.contrib.auth.models import User
from home.models import Major


class Thread(models.Model):
    user = models.ForeignKey(User)                              #user that created the thread
    title = models.CharField(max_length=40)                     #Project Name
    body = models.TextField()                                   #Project Description
    category = models.ForeignKey(Major)
    created_at = models.DateTimeField(auto_now_add=True)        #Created At

    def __unicode__(self):
        return " {0} {1} {2}".format(self.user, self.name, self.description)