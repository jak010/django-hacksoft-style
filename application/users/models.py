from django.db import models
from django.contrib.auth.models import (
    BaseUserManager as BUM,
    PermissionsMixin,
    AbstractBaseUser
)


class UserManager(BUM):

    def create_user(self, userid, password):
        user = self.model(
            userid=userid,
            is_active=True,
            is_admin=False
        )

        if password is not None:
            user.set_password(password)
        else:
            user.set_unusable_password()

        user.full_clean()
        user.save(using=self._db)

        return user

    def create_superuser(self, userid, password):
        user = self.model(
            userid=userid,
            password=password,
            is_active=True,
            is_admin=True,
        )

        user.is_superuser = True
        user.save(using=self._db)

        return user


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

    object = BUM()

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    USERNAME_FIELD = 'user_id'

    def __str__(self):
        return self.user_id
