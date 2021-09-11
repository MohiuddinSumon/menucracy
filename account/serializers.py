from django.contrib.auth import password_validation
from django.contrib.auth.base_user import BaseUserManager
from rest_framework import serializers
from account.models import User, UserType


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=50, min_length=6, write_only=True,
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'user_types')

    def validate_email(self, value):
        user = User.objects.filter(email=value)
        if user:
            raise serializers.ValidationError("Email is already taken")
        return BaseUserManager.normalize_email(value)

    def validate_password(self, value):
        password_validation.validate_password(value)
        return value

    def create(self, validated_data):
        if validated_data['user_types'] == UserType.ADMIN:
            return User.objects.create_superuser(**validated_data)
        else:
            return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=50, min_length=6, write_only=True,
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    class Meta:
        model = User
        fields = ['username', 'password']
        # read_only_fields = ['token']

