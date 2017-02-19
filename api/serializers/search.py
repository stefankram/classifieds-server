from rest_framework import serializers

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
        read_only=True)

    item_id = serializers.PrimaryKeyRelatedField(
        many=False,
        read_only=True)

    class Meta:
        model = SearchModel
        fields = [
            'id',
            'buyer_id',
            'created_at',
            'description',
            'item_id'
        ]
