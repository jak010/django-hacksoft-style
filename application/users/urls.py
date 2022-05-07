from django.urls import path

from .api import (
    UserSignupApi
)

urlpatterns = [
    path("signup", UserSignupApi.as_view())
]
