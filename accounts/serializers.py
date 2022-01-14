from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from accounts.models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, trim_whitespace=False, required=True)
    is_staff = serializers.BooleanField(read_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name', 'is_staff']

    def validate_password(self, value):
        if not validate_password(value):
            return value

    def create(self, data):
        return CustomUser.objects.create_user(**data)