from rest_framework import serializers

from api.models import BillingModel


class BillingSerializer(serializers.ModelSerializer):
    """
    Billing Serializer

    Description
    -----------
    Serializes the billing model
    """
    class Meta:
        model = BillingModel
        fields = [
            'id',
            'card_network',
            'card_number',
            'card_security_code',
            'card_expiry'
        ]
