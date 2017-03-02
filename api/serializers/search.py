from rest_framework import serializers

from api.models import BuyerModel
from api.models import ItemModel
from api.models import SearchModel


class SearchSerializer(serializers.ModelSerializer):
    """
    Search Serializer

    Description
    -----------
    Serializes the search model
    """
    buyer_id = serializers.PrimaryKeyRelatedField(
        many=False,
        read_only=False,
        queryset=BuyerModel.objects.all())

    item_id = serializers.PrimaryKeyRelatedField(
        many=False,
        read_only=False,
        queryset=ItemModel.objects.all())

    class Meta:
        model = SearchModel
        fields = [
            'id',
            'buyer_id',
            'created_at',
            'description',
            'item_id',
            'latitude',
            'longitude',
            'radius'
        ]
