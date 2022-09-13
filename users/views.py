from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .serializers import SerializersPassword


class PasswordUpdate(generics.UpdateAPIView):
    http_method_names = ['put', 'options']
    permission_classes = (IsAuthenticated,)
    serializer_class = SerializersPassword

    def get_object(self):
        return self.request.user
