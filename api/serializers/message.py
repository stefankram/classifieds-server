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
        model = CompanyModel
        fields = [
            'id',
            'address_id',
            'billing_id',
            'created_at',
            'description',
            'email',
            'logo_pic',
            'name',
            'password_id',
            'phone'
        ]
