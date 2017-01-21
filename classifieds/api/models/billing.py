from django.db import models


class Billing(models.Model):
    """
    Billing Model

    Holds the billing information of a user

    """
    cvv = models.CharField(
        db_column='cvv',
        max_length=4)

    expiry = models.DateField(
        db_column='expiry')

    name = models.CharField(
        db_column='name',
        max_length=192)

    number = models.CharField(
        db_column='number',
        max_length=19)