from django.core.validators import MinLengthValidator
from django.db import models


class ItemModel(models.Model):
    """
    Item Model

    Description
    -----------
    A product or service that is purchased by a buyer from a seller

    Constants
    ---------
    ITEM_TYPES: [(code: string, name: string)]
        The type of item, either product or service

    Instance Variables
    ------------------
    available: boolean
        Specifies whether the item is offered by any sellers
    created_at: datetime
        The creation date of this item
    name: string
        The name of the item
    item_type: string
        Determines whether the item is a product or service
    """
    ITEM_TYPES = [
        ('PR', 'Product'),
        ('SE', 'Service')
    ]

    available = models.BooleanField(
        db_column='available',
        default=True)

    created_at = models.DateTimeField(
        auto_now_add=True,
        db_column='created_at',
        editable=False)

    name = models.CharField(
        db_column='name',
        max_length=192,
        unique=True)

    item_type = models.CharField(
        db_column='item_type',
        max_length=2,
        choices=ITEM_TYPES,
        validators=[MinLengthValidator(2)])
