from rest_framework import serializers

from api.models import SellerModel


class SellerSerializer(serializers.ModelSerializer):
    """
    Seller Serializer

    Description
    -----------
    Serializes the seller model
    """
    address_id = serializers.PrimaryKeyRelatedField(
        many=False,
        read_only=True)

    billing_id = serializers.PrimaryKeyRelatedField(
        many=False,
        read_only=True)

    company_id = serializers.PrimaryKeyRelatedField(
        many=False,
        read_only=True)

    class Meta:
        model = SellerModel
        fields = [
            'id',
            'address_id',
            'billing_id',
            'company_id',
            'created_at',
            'description',
            'email',
            'first_name',
            'last_name',
            'password_id',
            'phone',
            'profile_pic'
        ]
