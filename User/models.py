from django.contrib.auth.models import User
from django.db import models


class Register_profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    phone = models.IntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)
    device_token = models.CharField(max_length=255)
