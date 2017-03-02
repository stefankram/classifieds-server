from rest_framework import serializers

from api.models import BuyerModel
from api.models import MessageModel
from api.models import SearchModel
from api.models import SellerModel


class MessageSerializer(serializers.ModelSerializer):
    """
    Message Serializer

    Description
    -----------
    Serializes the message model
    """
    buyer_id = serializers.PrimaryKeyRelatedField(
        many=False,
        read_only=False,
        queryset=BuyerModel.objects.all())

    search_id = serializers.PrimaryKeyRelatedField(
        many=False,
        read_only=False,
        queryset=SearchModel.objects.all())

    seller_id = serializers.PrimaryKeyRelatedField(
        many=False,
        read_only=False,
        queryset=SellerModel.objects.all())

    class Meta:
        model = MessageModel
        fields = [
            'id',
            'buyer_id',
            'created_at',
            'message',
            'recipient',
            'search_id',
            'seller_id'
        ]
