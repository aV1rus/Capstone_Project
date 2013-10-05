from django.db import models
from django.contrib.auth.models import User


class Projects(models.Model):
    user = models.ForeignKey(User)                           #user that created project
    name = models.CharField(max_length=40)                      #Project Name
    description = models.CharField(max_length=300)              #Project Description
    created_at = models.DateTimeField(auto_now_add=True)        #Created At

    def __unicode__(self):
        return " {0} {1} {2}".format(self.user, self.name, self.description)


# class Project(models.Model):
#     project_ref = models.ManyToOneRel(Projects)                 #reference to main project
#     user = models.ForeignKey(User)                              #user that made the change/update
#     description = models.CharField(max_length=300)              #description of change made
#     file_location = models.CharField(max_length=50)             #Location on server file is saved at
#     created_at = models.DateTimeField(auto_now_add=True)        #Date change was made
#
#     def __unicode__(self):
#         return " {0} {1} {2}".format(self.user, self.description, self.project_ref)


class ProjectMembers(models.Model):
    user = models.ManyToManyField(User)                         #User referencing
    project = models.ManyToManyField(Projects)                  #project referencing

    def __unicode__(self):
        return " {0} {1}".format(self.user, self.project)