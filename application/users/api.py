from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response


class UserSignupApi(APIView):
    class InputSerializer(serializers.Serializer):
        userid = serializers.CharField(max_length=12)
        password = serializers.CharField(max_length=128)

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(200)
