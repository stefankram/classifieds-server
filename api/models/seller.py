from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db import models

from .company import CompanyModel
from .billing import BillingModel
from .address import AddressModel


class SellerModel(models.Model):
    """
    Seller Model

    Description
    -----------
    Represents a user who can sell items

    Instance Variables
    ------------------
    address_id: models.ForeignKey
        The address of the seller
    billing_id: models.ForeignKey
        The billing info of the seller
    company_id: models.ForeignKey
        The company a seller may belong to
    created_at: datetime
        The creation date of this account
    description: string
        A description of what the seller sells
    email: string
        The seller's email address
    first_name: string
        The seller's first name
    last_name: string
        The seller's last name
    phone: string
        The seller's phone number
    profile_pic: string
        The seller's profile picture
    updated_at: datetime
        The last time the buyer's data was updated
    user_id: models.ForeignKey
        A link to the user account of the buyer
    """
    address_id = models.OneToOneField(
        db_column='address_id',
        on_delete=models.PROTECT,
        to=AddressModel)

    billing_id = models.OneToOneField(
        db_column='billing_id',
        on_delete=models.PROTECT,
        to=BillingModel)

    company_id = models.ForeignKey(
        db_column='company_id',
        null=True,
        on_delete=models.CASCADE,
        to=CompanyModel)

    created_at = models.DateTimeField(
        auto_now_add=True,
        db_column='created_at',
        editable=False)

    description = models.TextField(
        db_column='description')

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

    phone = models.CharField(
        db_column='phone',
        max_length=15,
        validators=[MinLengthValidator(10)])

    profile_pic = models.URLField(
        db_column='profile_pic',
        max_length=1024)

    updated_at = models.DateTimeField(
        auto_now=True,
        db_column='updated_at',
        editable=False)

    user_id = models.OneToOneField(
        db_column='user_id',
        on_delete=models.CASCADE,
        to=User)

    def delete(self, using=None, keep_parents=False):
        if self.address_id:
            self.address_id.delete()

        if self.billing_id:
            self.billing_id.delete()
