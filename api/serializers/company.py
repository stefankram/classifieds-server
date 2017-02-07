from rest_framework import serializers

from api.models import CompanyModel


class CompanySerializer(serializers.ModelSerializer):
    """
    Company Serializer

    Description
    -----------
    Serializes the company model
    """
    address_id = serializers.PrimaryKeyRelatedField(
        many=False,
        read_only=True)

    billing_id = serializers.PrimaryKeyRelatedField(
        many=False,
        read_only=True)

    password_id = serializers.PrimaryKeyRelatedField(
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