from django.db import models


class Item(models.Model):
    """
    Item Model

    A representation of a product or service that can be purchased by a buyer
    or seller

    """
    TYPE = (
        ('PR', 'Product'),
        ('SR', 'Service'),
    )

    available = models.BooleanField(
        db_column='available')

    created_at = models.DateTimeField(
        auto_now_add=True,
        db_column='created_at',
        editable=False)

    name = models.CharField(
        db_column='name',
        max_length=192,
        unique=True)

    type = models.CharField(
        db_column='type',
        max_length=2,
        choices=TYPE)
