from django.db import models

from .item import ItemModel
from .seller import SellerModel


class SellerItemModel(models.Model):
    """
    Seller Item Model

    Description
    -----------
    A list of items that are sold by sellers

    Instance Variables
    ------------------
    item_id: models.ForeignKey
        The item
    seller_id: models.ForeignKey
        The seller
    """
    item_id = models.ForeignKey(
        db_column='item_id',
        on_delete=models.CASCADE,
        to=ItemModel)

    seller_id = models.ForeignKey(
        db_column='seller_id',
        on_delete=models.CASCADE,
        to=SellerModel)
