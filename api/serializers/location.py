from rest_framework import serializers

from api.models import LocationModel


class LocationSerializer(serializers.ModelSerializer):
    """
    Location Serializer

    Description
    -----------
    Serializes the location model
    """
    seller_id = serializers.PrimaryKeyRelatedField(
        many=False,
        read_only=True)

    class Meta:
        model = LocationModel
        fields = [
            'id',
            'latitude',
            'longitude',
            'seller_id'
        ]
