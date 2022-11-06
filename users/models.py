from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    company: models.CharField = models.CharField(
        max_length=100, blank=True, null=True
    )
