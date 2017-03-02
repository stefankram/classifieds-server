from django.contrib.auth.models import User
from rest_framework import serializers

from api.models import AddressModel
from api.models import BillingModel
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
        read_only=False,
        queryset=AddressModel.objects.all())

    billing_id = serializers.PrimaryKeyRelatedField(
        many=False,
        read_only=False,
        queryset=BillingModel.objects.all())

    user_id = serializers.PrimaryKeyRelatedField(
        many=False,
        read_only=False,
        queryset=User.objects.all())

    class Meta:
        model = CompanyModel
        fields = [
            'id',
            'address_id',
            'billing_id',
            'created_at',
            'description',
            'logo_pic',
            'phone',
            'user_id'
        ]
