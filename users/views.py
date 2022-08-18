from rest_framework import generics, permissions
from .serializers import SerializersPassword


class PasswordUpdate(generics.UpdateAPIView):
    http_method_names = ['put', 'options']
    permission_classes = permissions.IsAuthenticated
    serializer_class = SerializersPassword

    def get_user(self):
        return self.request.user
