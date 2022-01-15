from datetime import datetime

from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import CustomUser
from accounts.serializers import UserSerializer


class LoginView(ObtainAuthToken):
    pass


class LogoutView(APIView):

    def post(self, request, *args, **kwargs):
        self.request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserList(ListAPIView):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.filter(deleted_at__isnull=True)


class UserRetrieve(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.filter(deleted_at__isnull=True)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.deleted_at = datetime.now()
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserRegister(CreateAPIView):
    permission_classes = []
    serializer_class = UserSerializer
