from django.db import models
from django.contrib.auth.models import User
from home.models import Major


## TODO :: Eventually TItle and Body should NOT be included in the Thread table and should only ref the first post held in comment

class Thread(models.Model):
    user = models.ForeignKey(User)                              #user that created the thread
    category = models.ForeignKey(Major)                         #Major that the category falls under
    created_at = models.DateTimeField(auto_now_add=True)        #Created At

    def __unicode__(self):
        return " {0} {1} {2}".format(self.user, self.title, self.body)


class Comments(models.Model):
    user = models.ForeignKey(User)                              #user that created the comment
    title = models.CharField(max_length=40)                     #Title that will display for comment
    body = models.TextField()                                   #Body of comment
    thread_ref = models.ForeignKey(Thread)                      #Thread comment is ref
    created_at = models.DateTimeField(auto_now_add=True)        #Created At

    def __unicode__(self):
        return " {0} {1} {2}".format(self.user, self.title, self.body)
