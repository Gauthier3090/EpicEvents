from rest_framework import permissions, status
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.settings import api_settings

from .serializers import SerializersPassword, UserSerializer
from .models import User


class CreateUser(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

    def post(self, request, *args, **kwargs):
        data = request.data.copy()
        serializer = UserSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            User.objects.create(
                username=user.username,
                first_name=user.first_name,
                last_name=user.last_name,
                password=user.password,
                email=user.email,
                phone=user.phone,
                mobile=user.mobile
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PasswordUpdate(UpdateAPIView):
    http_method_names = ['put', 'options']
    permission_classes = permissions.IsAuthenticated
    serializer_class = SerializersPassword

    def get_user(self):
        return self.request.user
