from functools import cached_property

from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .services import UserService, UserSignupService


class UserSignupApi(APIView):
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
