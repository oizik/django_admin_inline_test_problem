# type: ignore

import auto_prefetch
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.functions import Lower


class User(AbstractUser):

    company: models.CharField = models.CharField(
        max_length=100, blank=True, null=True
    )


class Login(auto_prefetch.Model):
    """Represents a record of a user login event."""

    user = auto_prefetch.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="logins"
    )

    ip = models.GenericIPAddressField()
    user_agent = models.TextField()
    date = models.DateTimeField(auto_now_add=True, db_index=True)

    domain = models.CharField(max_length=255)

    http_host = models.CharField(null=True, max_length=255)
    remote_host = models.CharField(null=True, max_length=255)
    server_name = models.CharField(null=True, max_length=255)

    class Meta:
        indexes = [models.Index(Lower('domain'), name='email_domain_idx')]

    def save(self, *args, **kwargs):
        _, domain = self.user.email.rsplit('@', maxsplit=1)
        self.domain = domain
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f'{self.user.email} - {self.ip} - {str(self.date)}'
