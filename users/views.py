from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .serializers import SerializersPassword, UserSerializer
from .models import User


class CreateUser(generics.CreateAPIView):
    
    http_method_names = ['post', 'options']
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        data = request.data.copy()
        serializer = UserSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            User.objects.create(
                username=user.first_name,
                first_name=user.first_name,
                last_name=user.last_name,
                password=user.password,
                email=user.email,
                phone=user.phone,
                mobile=user.mobile
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PasswordUpdate(generics.UpdateAPIView):
    http_method_names = ['put', 'options']
    permission_classes = permissions.IsAuthenticated
    serializer_class = SerializersPassword

    def get_user(self):
        return self.request.user
