from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import (
    PermissionsMixin,
    AbstractBaseUser
)


class User(AbstractBaseUser, PermissionsMixin):
    user_id = models.CharField(
        verbose_name="userid",
        max_length=12,
        unique=True
    )

    password = models.CharField(
        verbose_name='user password',
        max_length=128
    )

    last_login = models.DateTimeField(
        verbose_name='last login',
        blank=True,
        null=True
    )

    objects = BaseUserManager()

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    USERNAME_FIELD = 'user_id'

    def __str__(self):
        return self.user_id
