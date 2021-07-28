from django.db import models
from django.contrib.auth.models import User, Group
from django.utils.translation import gettext_lazy as _
from django.urls import reverse


# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=100)
    create_date = models.DateField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/project/{self.id}'


class UserGroup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    class Access(models.TextChoices):
        GUEST = 'GU', _('Guest')
        USER = 'US', _('User')
        ADMIN = 'AD', _('Admin')

    access = models.CharField(
        max_length=2,
        choices=Access.choices,
        default=Access.USER,
    )

    def __str__(self):
        return "User %s in project %s" % (self.user, self.project)


class TaskGroup(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    create_date = models.DateField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(TaskGroup, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
