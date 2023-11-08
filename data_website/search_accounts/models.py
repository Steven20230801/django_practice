from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
SERVER_CHOICES = [
    ("enfaureport", "enfaureport"),
    ("enfau2report", "enfau2report"),
]


class SearchAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # server = models.CharField(max_length=500)
    server = models.CharField(
        max_length=100, choices=SERVER_CHOICES, default="enfaureport"
    )
    login = models.IntegerField(max_length=500)
    created_at = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return f"{self.login}"
