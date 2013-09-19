from django.db import models

# Create your models here.
class User(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    userName = models.CharField(max_length=30)
    registration_date = models.DateTimeField(auto_now_add=True, verbose_name="Registration Date")
    last_visit = models.DateTimeField(auto_now_add=True, verbose_name="Last Visit")
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=30)

    def __unicode__(self):
        return self.id


