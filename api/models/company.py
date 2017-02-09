from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db import models

from .billing import BillingModel
from .address import AddressModel


class CompanyModel(models.Model):
    """
    Company Model

    Description
    -----------
    A company who has many sellers

    Instance Variables
    ------------------
    address_id: models.ForeignKey
        The address of the company
    billing_id: models.ForeignKey
        The billing info of the company
    description: string
        The description of the company
    logo_pic: string
        The company's logo
    phone: string
        The company's phone number
    user_id: models.ForeignKey
        A link to the user account of the company
    """
    address_id = models.OneToOneField(
        db_column='address_id',
        on_delete=models.PROTECT,
        to=AddressModel)

    billing_id = models.OneToOneField(
        db_column='billing_id',
        on_delete=models.PROTECT,
        to=BillingModel)

    description = models.TextField(
        db_column='description')

    logo_pic = models.URLField(
        db_column='logo_pic',
        max_length=1024)

    phone = models.CharField(
        db_column='phone',
        max_length=15,
        validators=[MinLengthValidator(10)])

    user_id = models.OneToOneField(
        db_column='user_id',
        on_delete=models.CASCADE,
        to=User)

    def delete(self, using=None, keep_parents=False):
        if self.address_id:
            self.address_id.delete()

        if self.billing_id:
            self.billing_id.delete()
