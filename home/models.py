from django.db import models


class Major(models.Model):
    name = models.CharField(max_length=200)                      #Category Name
    acr = models.CharField(max_length=10)                        #Category Acronym

    def __unicode__(self):
        return self.name