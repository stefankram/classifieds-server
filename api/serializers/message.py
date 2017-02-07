from rest_framework import serializers

from api.models import MessageModel


class MessageSerializer(serializers.ModelSerializer):
    """
    Message Serializer

    Description
    -----------
    Serializes the message model
    """
    buyer_id = serializers.PrimaryKeyRelatedField(
        many=False,
        read_only=True)

    seller_id = serializers.PrimaryKeyRelatedField(
        many=False,
        read_only=True)

    class Meta:
        model = MessageModel
        fields = [
            'id',
            'buyer_id',
            'created_at',
            'message',
            'recipient',
            'seller_id'
        ]