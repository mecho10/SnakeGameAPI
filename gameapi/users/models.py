from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    high_score = models.IntegerField(default=0)

    def __str__(self):
        return self.username

# Create your models here.
