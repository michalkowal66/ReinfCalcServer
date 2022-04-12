from django.db import models
from django.contrib import auth


# Create your models here.
class User(auth.models.User, auth.models.PermissionsMixin):
    def __str__(self):
        return self.username


class Task(models.Model):
    owner = models.ForeignKey(User, related_name='task', on_delete=models.CASCADE)
    save_file = models.CharField(max_length=2048)
    results = models.CharField(max_length=2048, blank=True)
