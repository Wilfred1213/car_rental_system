from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255, null=True)
    second_name = models.CharField(max_length=255, null=True)
    photo = models.ImageField(upload_to='media', null=True)

