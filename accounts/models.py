from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    identifier_id = models.CharField('Identifier ID', max_length=10, null=True)
    email = models.EmailField('Email', unique=True)
    username = models.CharField('Name', max_length=150, blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['-date_joined']

    def __str__(self):
        return f'{self.email}'
