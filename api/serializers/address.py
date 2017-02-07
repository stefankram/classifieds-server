from rest_framework import serializers

from api.models import AddressModel


class AddressSerializer(serializers.ModelSerializer):
    """
    Address Serializer

    Description
    -----------
    Serializes the address model
    """
    class Meta:
        model = AddressModel
        fields = [
            'id',
            'city',
            'country',
            'postal_code',
            'province',
            'street'
        ]
