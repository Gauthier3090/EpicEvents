from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(
        required=True,
        allow_blank=False
    )
    last_name = serializers.CharField(
        required=True,
        allow_blank=False
    )
    email = serializers.CharField(
        required=True,
        allow_blank=False
    )
    mobile = serializers.CharField(
        max_length=20,
        required=True,
        allow_blank=True
    )
    phone = serializers.CharField(
        max_length=20,
        required=True,
        allow_blank=True
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={
            'input_type': 'password',
            'placeholder': 'Password'
        }
    )

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'phone', 'mobile', 'team', 'password')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'email': {'required': True},
            'mobile': {'read_only': True},
            'password': {'write_only': True},
        }

    def save(self, **kwargs):
        user = User(
            username=self.validated_data['username'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            email=self.validated_data['email'],
            phone=self.validated_data['phone'],
            mobile=self.validated_data['mobile'],
        )
        password = self.validated_data['password']

        if password is None:
            raise serializers.ValidationError({'password': "Password is empty."})

        user.set_password(password)
        user.save()
        return user


class SerializersPassword(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password_confirm = serializers.CharField(write_only=True, required=True)
    password_old = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = get_user_model()
        fields = ('password_old', 'password', 'password_confirm')

        @staticmethod
        def check(attrs):
            if attrs['password'] != attrs['password_confirm']:
                raise serializers.ValidationError({"password": "Passwords didn't match"})
            return attrs
