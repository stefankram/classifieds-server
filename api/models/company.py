from django.core.validators import MinLengthValidator
from django.db import models

from .password import PasswordModel
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
    created_at: datetime
        The creation date of this account
    description: string
        The description of the company
    email: string
        The company's email address
    logo_pic: string
        The company's logo
    name: string
        The company's name
    password_id: models.ForeignKey
        The password of this account
    phone: string
        The company's phone number
    """
    address_id = models.OneToOneField(
        db_column='address_id',
        on_delete=models.PROTECT,
        to=AddressModel)

    billing_id = models.OneToOneField(
        db_column='billing_id',
        on_delete=models.PROTECT,
        to=BillingModel)

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

    logo_pic = models.URLField(
        db_column='logo_pic',
        max_length=1024)

    name = models.CharField(
        db_column='name',
        max_length=192)

    password_id = models.OneToOneField(
        db_column='password_id',
        on_delete=models.PROTECT,
        to=PasswordModel)

    phone = models.CharField(
        db_column='phone',
        max_length=15,
        validators=[MinLengthValidator(10)])
