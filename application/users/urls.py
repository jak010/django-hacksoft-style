from django.urls import path

from .api import (
    UserSignupApi
)

urlpatterns = [
    
    path(
        route="signup",
        view=UserSignupApi.as_view()
    )
]
