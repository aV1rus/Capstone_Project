from django.db import models
from login.models import Profile
# Create your models here.

class PrivateMessage(models.Model):
            sender = models.ForeignKey(Profile)
            receiver = models.ForeignKey(Profile)
            date_sent = models.DateTimeField(auto_now_add=True)
            content = models.TextField()
            def __unicode__(self):
                return " Message sent by {0} to {1} on {2}".format(self.sender, self.receiver, self.date_sent)




