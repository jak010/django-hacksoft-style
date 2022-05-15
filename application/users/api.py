from functools import cached_property

from django.contrib.auth import authenticate, login, logout

from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .services import UserService, UserSignupService, UserProfileService

from application.api.mixins import ApiAuthMixin


class UserSignupApi(APIView):
    """ 유저 등록 api """

    class InputSerializer(serializers.Serializer):
        userid = serializers.CharField(max_length=12)
        password = serializers.CharField(max_length=128)

    @cached_property
    def service(self) -> UserSignupService:
        return UserSignupService()

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.service.signup(
            **serializer.validated_data
        )

        return Response(status=status.HTTP_201_CREATED)


class UserSessionLoginApi(APIView):
    """ 유저 Session Login Api"""

    class InputSerializer(serializers.Serializer):
        userid = serializers.CharField(max_length=12)
        password = serializers.CharField(max_length=128)

    @cached_property
    def service(self) -> UserService:
        return UserService()

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(request, **serializer.validated_data)
        if user is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        login(request, user)

        return Response({
            'session': {
                'id': request.session.session_key,
                'expiry_age': request.session.get_expiry_age(),
                'expiry_date': request.session.get_expiry_date()
            },
            'data': self.service.get_user_data(user=user)
        })


class UserProfileApi(ApiAuthMixin, APIView):

    @cached_property
    def service(self) -> UserService:
        return UserService()

    def get(self, request):
        data = self.service \
            .get_user_data(user=request.user)

        return Response(data)


class UserProfileUpdateApi(ApiAuthMixin, APIView):
    class InputSerializer(serializers.Serializer):
        description = serializers.CharField(max_length=65535)

    @cached_property
    def service(self) -> UserProfileService:
        return UserProfileService()

    def put(self, request):
        """ 유저 프로필 업데이트하기 """
        from application.users.models import UserProfile

        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user_profile = self.service.find_by(user=request.user)
        if user_profile is None:
            UserProfile(user=request.user.id, **serializer.validated_data)
        else:
            user_profile.description = serializer.validated_data['description']
            user_profile.save()

        return Response(200)
