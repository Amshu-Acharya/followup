from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=50, blank=True)
    objects = UserManager()
