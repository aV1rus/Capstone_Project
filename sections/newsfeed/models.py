from django.db import models
from django.contrib.auth.models import User


class NewsFeed(models.Model):
    user = models.ForeignKey(User)                              #user which the update is referencing
    title = models.CharField(max_length=50)                     #title which the users friends will see
    #url = models.CharField(max_length=100)                     #url that forwards to what it is referencing
    view = models.CharField(max_length=100)                     #url that forwards to what it is referencing
    params = models.CharField(max_length=100)                   #url that forwards to what it is referencing

    created_at = models.DateTimeField(auto_now_add=True)        #Created At

    def __unicode__(self):
        return " {0} {1} {2}".format(self.user, self.title, self.url)