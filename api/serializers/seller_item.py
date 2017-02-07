from rest_framework import serializers

from api.models import SellerItemModel


class SellerItemSerializer(serializers.ModelSerializer):
    """
    Seller Item Serializer

    Description
    -----------
    Serializes the seller item model
    """
    item_id = serializers.PrimaryKeyRelatedField(
        many=False,
        read_only=True)

    seller_id = serializers.PrimaryKeyRelatedField(
        many=False,
        read_only=True)

    class Meta:
        model = SellerItemModel
        fields = [
            'id',
            'item_id',
            'seller_id'
        ]
