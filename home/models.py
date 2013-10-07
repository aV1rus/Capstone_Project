from django.db import models


class Major(models.Model):
    name = models.CharField(max_length=50)                      #Category Name
    acr = models.CharField(max_length=4)                        #Category Acronym