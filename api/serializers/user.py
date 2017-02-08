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
            'is_active',
            'password',
            'username'
        ]
