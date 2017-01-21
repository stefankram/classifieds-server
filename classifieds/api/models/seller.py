from django.db import models
from .address import Address
from .billing import Billing
from .user import User


class Seller(models.Model):
    """
    Seller Model

    A representation of a seller that can sell products and services from our
    platform

    """
    address_id = models.ForeignKey(
        db_column='address_id',
        on_delete=models.PROTECT,
        to=Address)

    billing_id = models.ForeignKey(
        db_column='billing_id',
        on_delete=models.PROTECT,
        to=Billing)

    company_id = models.ForeignKey(
        db_column='company_id',
        null=True,
        on_delete=models.PROTECT,
        to=Company)

    email = models.CharField(
        db_column='email',
        max_length=192,
        null=True,
        unique=True)

    name = models.CharField(
        db_column='name',
        max_length=192)

    phone = models.CharField(
        db_column='phone',
        max_length=15)

    profile_pic = models.CharField(
        db_column='profile_pic',
        max_length=2048)

    user_id = models.ForeignKey(
        db_column='user_id',
        on_delete=models.CASCADE,
        to=User)
