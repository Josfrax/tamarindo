from django.db import models
from django.contrib.auth.models import AbstractUser

from .manager import UserManager


class User(AbstractUser):
    rut = models.CharField(max_length=9, unique=True, null=False)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=12, null=True, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)

    objects = UserManager()

    def __str__(self):
        return self.email