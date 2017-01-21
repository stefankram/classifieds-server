from django.db import models


class ItemResponse(models.Model):
    """
    Item Response Model

    A response made by a seller to respond to a request made by a buyer

    """
    item_id = models.ForeignKey(
        db_column='item_id',
        on_delete=models.CASCADE,
        to=Item)

    message = models.CharField(
        db_column='message',
        max_length=1024)

    price = models.DecimalField(
        db_column='price',
        max_digits=7,
        decimal_places=2)

    seller_id = models.ForeignKey(
        db_column='seller_id',
        on_delete=models.CASCADE,
        to=Seller)