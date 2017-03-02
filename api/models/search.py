from django.db import models

from .buyer import BuyerModel
from .item import ItemModel


class SearchModel(models.Model):
    """
    Search Model

    Description
    -----------
    A search created by a buyer looking to purchase something

    Instance Variables
    ------------------
    buyer_id: models.ForeignKey
        The buyer
    created_at: datetime
        The creation date of the search
    description: string
        The description of the search
    item_id: models.ForeignKey
        The item they wish to purchase
    latitude: double
        The search latitude location
    longitude: double
        The search longitude location
    radius: integer
        How far the buyer is willing to go
    """
    buyer_id = models.ForeignKey(
        db_column='buyer_id',
        on_delete=models.CASCADE,
        to=BuyerModel)

    created_at = models.DateTimeField(
        auto_now_add=True,
        db_column='created_at',
        editable=False)

    description = models.TextField(
        db_column='description')

    item_id = models.ForeignKey(
        db_column='item_id',
        on_delete=models.CASCADE,
        to=ItemModel)

    latitude = models.FloatField(
        db_column='latitude')

    longitude = models.FloatField(
        db_column='longitude')

    radius = models.IntegerField(
        db_column='radius')
