from django.db import models
from .address import Address
from .billing import Billing
from .password import Password


class Company(models.Model):
    """
    Company Model

    A representation of a company that provides sellers for the platform

    """
    address_id = models.ForeignKey(
        db_column='address_id',
        on_delete=models.PROTECT,
        to=Address)

    billing_id = models.ForeignKey(
        db_column='billing_id',
        on_delete=models.PROTECT,
        to=Billing)

    created_at = models.DateTimeField(
        auto_now_add=True,
        db_column='created_at',
        editable=False)

    description = models.TextField(
        db_column='description')

    email = models.CharField(
        db_column='email',
        unique=True)

    header_pic = models.CharField(
        db_column='header_pic',
        max_length=2048)

    name = models.CharField(
        db_column='name',
        max_length=192)

    password_id = models.ForeignKey(
        db_column='password_id',
        on_delete=models.PROTECT,
        to=Password)

    phone = models.CharField(
        db_column='phone',
        max_length=15)