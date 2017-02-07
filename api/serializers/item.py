from rest_framework import serializers

from api.models import ItemModel


class ItemSerializer(serializers.ModelSerializer):
    """
    Item Serializer

    Description
    -----------
    Serializes the item model
    """
    class Meta:
        model = ItemModel
        fields = [
            'id',
            'available',
            'created_at',
            'name',
            'item_type'
        ]
