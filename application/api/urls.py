from django.urls import path, include

urlpatterns = [
    path('users/', include(('application.users.urls', 'users')))
]
