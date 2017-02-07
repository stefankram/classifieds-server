from rest_framework import serializers

from api.models import RatingModel


class RatingSerializer(serializers.ModelSerializer):
    """
    Rating Serializer

    Description
    -----------
    Serializes the rating model
    """
    buyer_id = serializers.PrimaryKeyRelatedField(
        many=False,
        read_only=True)

    seller_id = serializers.PrimaryKeyRelatedField(
        many=False,
        read_only=True)

    class Meta:
        model = RatingModel
        fields = [
            'id',
            'buyer_id',
            'created_at',
            'review',
            'recipient',
            'score',
            'seller_id'
        ]
