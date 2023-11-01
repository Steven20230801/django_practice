from django.contrib.auth.models import User
from django.db import models


class Users(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100, default="")
    brand = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.user.username
