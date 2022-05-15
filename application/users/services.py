from abc import ABCMeta

from application.users.models import User
from application.api.ServiceImpl import BaseService


class UserService(BaseService):
    model: User = User

    def find_by(self, userid):
        return User.objects.get(userid=userid)

    def filter_by(self, userid):
        return User.objects.filter(userid=userid)

    def delete_by(self, userid):
        return User.objects.delete(user_id=userid)

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
        if self.filter_by(userid=userid):
            raise Exception("Duplicate USer")

        self.create_user(userid=userid, password=password)

        return True

    def _validator_userid(self, userid):
        return True

    def _validator_password(self, password):
        return True
