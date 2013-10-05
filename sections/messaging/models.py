from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class PrivateMessage(models.Model):
            sender = models.ForeignKey(User, related_name='send+')
            receiver = models.ForeignKey(User, related_name='rec+')
            date_sent = models.DateTimeField(auto_now_add=True)
            content = models.TextField()

            def __unicode__(self):
                return " Message sent by {0} to {1} on {2}".format(self.sender, self.receiver, self.date_sent)




