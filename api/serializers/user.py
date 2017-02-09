from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """
    User Serializer

    Description
    -----------
    Serializes the user model
    """

    class Meta:
        model = User
        fields = [
            'id',
            'date_joined',
            'email',
            'first_name',
            'is_active',
            'last_name',
            'password',
            'username'
        ]

    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'])
