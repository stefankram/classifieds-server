from django.db import models


class Order(models.Model):
    """
    Order Model

    An order that has been created by a seller for a product or service that a
    buyer wishes to purchase

    """
    buyer_id = models.ForeignKey(
        db_column='buyer_id',
        on_delete=models.CASCADE,
        to=Buyer)

    completed = models.BooleanField(
        db_column='completed')

    created_at = models.DateTimeField(
        auto_now_add=True,
        db_column='created_at',
        editable=False)

    description = models.TextField(
        db_column='description')

    item_id = models.ForeignKey(
        db_column='item_id',
        on_delete=models.CASCADE,
        to=Item)

    prepaid = models.BooleanField(
        db_column='prepaid')

    price = models.DecimalField(
        db_column='price',
        max_digits=7,
        decimal_places=2)

    purchase_date = models.DateTimeField(
        db_column='purchase_date')

    seller_id = models.ForeignKey(
        db_column='seller_id',
        on_delete=models.CASCADE,
        to=Seller)