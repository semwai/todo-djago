from django.db import models
from django.contrib.auth.models import User, Group
# Create your models here.

class UserGroup(Group):
    pass 

class Project(models.Model):
    name = models.CharField(max_length=100)
    create_date = models.DateField()
    group = models.ForeignKey(UserGroup, on_delete = models.CASCADE)

class TaskGroup(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    project =  models.ForeignKey(Project, on_delete = models.CASCADE)

class Task(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    create_date = models.DateField()
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    group = models.ForeignKey(TaskGroup, on_delete = models.CASCADE)

