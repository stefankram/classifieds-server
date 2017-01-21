from django.db import models


class ItemsOffered(models.Model):
    """
    Items Offered Model

    A representation of the list of products and services offered by a seller

    """
    item_id = models.ForeignKey(
        db_column='item_id',
        on_delete=models.CASCADE,
        to=Item)

    seller_id = models.ForeignKey(
        db_column='seller_id',
        on_delete=models.CASCADE,
        to=Seller)