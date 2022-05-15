from abc import ABCMeta
from .models import User

from application.users.models import User


class UserService(metaclass=ABCMeta):
    model = User

    def find_by_pk(self, user_id) -> User:
        return User.objects.get(user_id=user_id)

    def filter_by_pk(self, user_id):
        return User.objects.filter(user_id=user_id)

    def delete_by_pk(self, user_id):
        return User.objects.delete(user_id=user_id)

    def create_user(self, userid, password):
        user = self.model(
            user_id=userid, is_active=True, is_admin=False
        )
        user.set_password(password)
        user.save()

        return user

    def get_user_data(self, user: User):
        return {
            'userid': user.userid,
            'is_active': user.is_active,
            'is_admin': user.is_admin,
            'is_superuser': user.is_superuser,
        }


class UserSignupService(UserService):

    def signup(self, userid, password):
        if self.filter_by_pk(user_id=userid):
            raise Exception("Duplicate USer")

        self.create_user(userid=userid, password=password)

        return True

    def _validator_userid(self, userid):
        return True

    def _validator_password(self, password):
        return True
