from rest_framework import serializers

from api.models import BuyerModel


class BuyerSerializer(serializers.ModelSerializer):
    """
    Buyer Serializer

    Description
    -----------
    Serializes the buyer model
    """
    address_id = serializers.PrimaryKeyRelatedField(
        many=False,
        read_only=True)

    billing_id = serializers.PrimaryKeyRelatedField(
        many=False,
        read_only=True)

    password_id = serializers.PrimaryKeyRelatedField(
        many=False,
        read_only=True)

    class Meta:
        model = BuyerModel
        fields = [
            'id',
            'address_id',
            'billing_id',
            'created_at',
            'email',
            'first_name',
            'last_name',
            'password_id',
            'phone',
            'profile_pic'
        ]
