from django.db import models
from django.contrib.auth.models import (
    BaseUserManager as BUM,
    PermissionsMixin,
    AbstractBaseUser
)


class User(BUM, AbstractBaseUser, PermissionsMixin):
    userid = models.CharField(
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

    is_active = True
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.userid

    def is_staff(self):
        return self.is_admin
