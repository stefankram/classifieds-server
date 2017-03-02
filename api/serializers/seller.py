from django.contrib.auth.models import User
from rest_framework import serializers

from api.models import AddressModel
from api.models import BillingModel
from api.models import CompanyModel
from api.models import SellerModel


class SellerSerializer(serializers.ModelSerializer):
    """
    Seller Serializer

    Description
    -----------
    Serializes the seller model
    """
    address_id = serializers.PrimaryKeyRelatedField(
        many=False,
        read_only=False,
        queryset=AddressModel.objects.all())

    billing_id = serializers.PrimaryKeyRelatedField(
        many=False,
        read_only=False,
        queryset=BillingModel.objects.all())

    company_id = serializers.PrimaryKeyRelatedField(
        many=False,
        read_only=False,
        queryset=CompanyModel.objects.all())

    user_id = serializers.PrimaryKeyRelatedField(
        many=False,
        read_only=False,
        queryset=User.objects.all())

    class Meta:
        model = SellerModel
        fields = [
            'id',
            'address_id',
            'billing_id',
            'company_id',
            'description',
            'phone',
            'profile_pic',
            'user_id'
        ]
