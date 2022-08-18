from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from .models import User


class SerializersPassword(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password_confirm = serializers.CharField(write_only=True, required=True)
    password_old = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('password_old', 'password', 'password_confirm')

        @staticmethod
        def check(self, attrs):
            if attrs['password'] != attrs['password_confirm']:
                raise serializers.ValidationError({"password": "Passwords didn't match"})
            return attrs
