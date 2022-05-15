# get_auth_header
# SessionAsHeaderAuthentication
# CsrfExemptedSessionAuthentication
from importlib import import_module
from django.conf import settings
from django.contrib import auth

from rest_framework.permissions import IsAuthenticated, BasePermission

from rest_framework.authentication import (
    BaseAuthentication,
    SessionAuthentication
)


class CsrfExemptedSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return


class SessionAsHeaderAuthentication(BaseAuthentication):

    def _get_auth_header(self, headers):
        value = headers.get("Authorization")

        if not value:
            return None

        auth_type, auth_value = value.split()[:2]

        return auth_type, auth_value

    def authenticate(self, request):
        auth_header = self._get_auth_header(request.headers)
        if auth_header is None:
            return None

        auth_type, auth_value = auth_header

        # 헤더 요청 예제
        ## Authorization: Session ....
        if auth_type != "Session":
            return None

        engine = import_module(settings.SESSION_ENGINE)
        SessionStore = engine.SessionStore
        session_key = auth_value

        request.session = SessionStore(session_key)
        user = auth.get_user(request)

        return user, None


class ApiAuthMixin:
    authentication_classes = [
        CsrfExemptedSessionAuthentication,
        SessionAsHeaderAuthentication
    ]
    permission_classes = (IsAuthenticated,)
