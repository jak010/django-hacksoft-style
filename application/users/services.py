from abc import ABCMeta
from typing import Optional

from django.db import transaction
from django.db.models import QuerySet

from application.users.models import User

from application.api.types import DjangoModelType


class UserService(metaclass=ABCMeta):
    model: DjangoModelType = User  # Generic 타입 없을 떄 18번라인 Warning 뜸

    def find_by_pk(self, userid) -> Optional[model]:
        try:
            user = self.model.objects.get(userid=userid)
        except self.model.DoesNotExist:
            return None

        return user

    def filter_by_pk(self, userid) -> QuerySet:
        return self.model.objects.filter(userid=userid)

    def delete_by_pk(self, userid):
        return self.model.objects.delete(userid=userid)

    def create_user(self, userid, password):
        user = self.model(
            userid=userid, is_active=True, is_admin=False
        )
        user.set_password(password)
        user.save()

        return user


class UserSignupService(UserService):

    @transaction.atomic
    def signup(self, userid, password):
        user = self.filter_by_pk(userid=userid)

        if not user:
            self.create_user(userid=userid, password=password)

        return user
