from django.urls import path

from .api import (
    UserSignupApi,
    UserSessionLoginApi,
)

urlpatterns = [
    path("signup", UserSignupApi.as_view()),
    path("session/login", UserSessionLoginApi.as_view())
]
