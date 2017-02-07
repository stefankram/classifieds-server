from rest_framework import serializers

from api.models import PasswordModel


class PasswordSerializer(serializers.ModelSerializer):
    """
    Password Serializer

    Description
    -----------
    Serializes the password model
    """

    class Meta:
        model = PasswordModel
        fields = [
            'id',
            'hash',
            'salt'
        ]
