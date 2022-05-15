from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import (
    PermissionsMixin,
    AbstractBaseUser
)

from application.common.models import BaseModel


class User(AbstractBaseUser, PermissionsMixin):
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

    objects = BaseUserManager()

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'userid'

    def __str__(self):
        return self.userid

    class Meta:
        db_table = "user"


class UserProfile(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)
    description = models.TextField(max_length=65535)
    date_of_birth = models.DateField(null=True)

    objects = models.Manager()

    class Meta:
        db_table = "user_profile"
