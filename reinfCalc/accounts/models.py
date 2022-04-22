from django.db import models
from django.contrib import auth
from django.utils import timezone


# Create your models here.
class User(auth.models.User, auth.models.PermissionsMixin):
    def __str__(self):
        return self.username


class Task(models.Model):
    owner = models.ForeignKey(User, related_name='task', on_delete=models.CASCADE)
    element_type = models.CharField(max_length=64)
    results = models.CharField(max_length=2048)
    creation_date = models.DateTimeField(default=timezone.now(), blank=True)
