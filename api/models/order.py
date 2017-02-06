from django.db import models

from .seller import SellerModel
from .item import ItemModel
from .buyer import BuyerModel


class OrderModel(models.Model):
    """
    Order Model

    Description
    -----------
    An order created by a seller for an item a buyer wants to purchase

    Instance Variables
    ------------------
    buyer_id: models.ForeignKey
        The buyer
    completed: boolean
        Whether the order has been completed successfully
    created_at: datetime
        The creation date of the order
    description: string
        The description of the order and items being bought
    prepaid: boolean
        Whether the order was paid using the app instead of in person
    price: decimal
        The price of the order
    purchase_date: datetime
        The day which the product will be bought on or the service will be
        performed on
    seller_id: models.ForeignKey
        The seller
    """
    buyer_id = models.ForeignKey(
        db_column='buyer_id',
        on_delete=models.CASCADE,
        to=BuyerModel)

    completed = models.BooleanField(
        db_column='completed',
        default=False)

    created_at = models.DateTimeField(
        auto_now_add=True,
        db_column='created_at',
        editable=False)

    description = models.TextField(
        db_column='description')

    item_id = models.ForeignKey(
        db_column='item_id',
        on_delete=models.PROTECT,
        to=ItemModel)

    prepaid = models.BooleanField(
        db_column='prepaid',
        default=False)

    price = models.DecimalField(
        db_column='price',
        max_digits=7,
        decimal_places=2)

    purchase_date = models.DateTimeField(
        db_column='purchase_date')

    seller_id = models.ForeignKey(
        db_column='seller_id',
        on_delete=models.CASCADE,
        to=SellerModel)
