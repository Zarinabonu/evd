from django.contrib.auth.models import User
from django.db import models


class Idea(models.Model):
    user = models.CharField(max_length=70)
    email = models.EmailField()
    title = models.CharField(max_length=100,null=True)
    description = models.TextField(null=True)