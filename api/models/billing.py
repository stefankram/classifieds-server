from django.core.exceptions import ValidationError
from django.db import models
from django.core.validators import MinLengthValidator
from datetime import date


class BillingModel(models.Model):
    """
    Billing Model

    Description
    -----------
    Contains the billing information of a user

    Constants
    ---------
    NETWORKS: [(code: string, network: string)]
        A list of all credit card networks (Visa, MasterCard, American Express)

    Instance Variables
    ------------------
    card_network: string
        The credit card's network
    card_number: string
        The credit card number
    card_security_code: string
        The credit card's security code
    card_expiry: date
        The credit card's expiry date
    """
    NETWORKS = [
        ('VI', 'Visa'),
        ('MA', 'MasterCard'),
        ('AM', 'American Express')
    ]

    card_network = models.CharField(
        choices=NETWORKS,
        db_column='card_network',
        max_length=2,
        validators=[MinLengthValidator(2)])

    card_number = models.CharField(
        db_column='card_number',
        max_length=16,
        validators=[MinLengthValidator(16)])

    card_security_code = models.CharField(
        db_column='card_security_code',
        max_length=4,
        validators=[MinLengthValidator(3)])

    card_expiry = models.DateField(
        db_column='card_expiry')

    def clean(self):
        if self.card_expiry < date.today():
            raise ValidationError('The expiry date must be in the future')
