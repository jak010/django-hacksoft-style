from django.urls import path

from .api import (
    UserSignupApi,
    UserSessionLoginApi,
    UserProfileApi,
    UserProfileUpdateApi,

)

urlpatterns = [

    path(
        route="signup",
        view=UserSignupApi.as_view()
    ),
    path(
        route="session/login",
        view=UserSessionLoginApi.as_view()
    ),
    path(
        route="session/profile",
        view=UserProfileApi.as_view()
    ),
    path(
        route="session/profile/update",
        view=UserProfileUpdateApi.as_view()
    )

]
