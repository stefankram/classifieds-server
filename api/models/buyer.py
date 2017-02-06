from django.core.validators import MinLengthValidator
from django.db import models

from .password import PasswordModel
from .billing import BillingModel
from .address import AddressModel


class BuyerModel(models.Model):
    """
    Buyer Model

    Description
    -----------
    Represents a user who can buy items

    Instance Variables
    ------------------
    address_id: models.ForeignKey
        The address of the buyer
    billing_id: models.ForeignKey
        The billing info of the buyer
    created_at: datetime
        The creation date of this account
    email: string
        The buyer's email address
    first_name: string
        The buyer's first name
    last_name: string
        The buyer's last name
    password_id: models.ForeignKey
        The password of the buyer
    phone: string
        The buyer's phone number
    profile_pic: string
        The buyer's profile picture
    """
    address_id = models.ForeignKey(
        db_column='address_id',
        on_delete=models.PROTECT,
        to=AddressModel,
        unique=True)

    billing_id = models.ForeignKey(
        db_column='billing_id',
        on_delete=models.PROTECT,
        to=BillingModel,
        unique=True)

    created_at = models.DateTimeField(
        auto_now_add=True,
        db_column='created_at',
        editable=False)

    email = models.EmailField(
        db_column='email',
        max_length=192,
        unique=True)

    first_name = models.CharField(
        db_column='first_name',
        max_length=192)

    last_name = models.CharField(
        db_column='last_name',
        max_length=192)

    password_id = models.ForeignKey(
        db_column='password_id',
        on_delete=models.PROTECT,
        to=PasswordModel,
        unique=True)

    phone = models.CharField(
        db_column='phone',
        max_length=15,
        validators=[MinLengthValidator(10)])

    profile_pic = models.URLField(
        db_column='profile_pic',
        max_length=1024,
        null=True)

    def delete(self, using=None, keep_parents=False):
        if self.address_id:
            self.address_id.delete()

        if self.billing_id:
            self.billing_id.delete()

        if self.password_id:
            self.password_id.delete()
