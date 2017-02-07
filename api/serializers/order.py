from rest_framework import serializers

from api.models import OrderModel


class OrderSerializer(serializers.ModelSerializer):
    """
    Order Serializer

    Description
    -----------
    Serializes the order model
    """
    buyer_id = serializers.PrimaryKeyRelatedField(
        many=False,
        read_only=True)

    seller_id = serializers.PrimaryKeyRelatedField(
        many=False,
        read_only=True)

    class Meta:
        model = OrderModel
        fields = [
            'id',
            'buyer_id',
            'completed',
            'created_at',
            'description',
            'prepaid',
            'price',
            'purchase_date',
            'seller_id'
        ]
