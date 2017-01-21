from django.db import models


class Address(models.Model):
    """
    Address Model

    Holds the address information of a user

    """
    city = models.CharField(
        db_column='city',
        max_length=192)

    country = models.CharField(
        db_column='country',
        max_length=192)

    postal_code = models.CharField(
        db_column='postal_code',
        max_length=16)

    province = models.CharField(
        db_column='province',
        max_length=192)

    street = models.CharField(
        db_column='street',
        max_length=192)