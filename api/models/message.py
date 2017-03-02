from django.core.validators import MinLengthValidator
from django.db import models

from .seller import SellerModel
from .buyer import BuyerModel
from .search import SearchModel


class MessageModel(models.Model):
    """
    Message Model

    Description
    -----------
    A message sent from either a seller to a buyer or vice-versa

    Constants
    ---------
    RECIPIENTS: [(code: string, who: string)]
        The choices of recipients for the message

    Instance Variables
    ------------------
    buyer_id: models.ForeignKey
        The buyer
    created_at: datetime
        The creation date of the message
    message: string
        The message text
    recipient: string
        Who will receive the message
    search_id: models.ForeignKey
        The search this message belongs to
    seller_id: models.ForeignKey
        The seller
    """
    RECIPIENTS = [
        ('BU', 'Buyer'),
        ('SE', 'Seller')
    ]

    buyer_id = models.ForeignKey(
        db_column='buyer_id',
        on_delete=models.CASCADE,
        to=BuyerModel)

    created_at = models.DateTimeField(
        auto_now_add=True,
        db_column='created_at',
        editable=False)

    message = models.TextField(
        db_column='message')

    recipient = models.CharField(
        choices=RECIPIENTS,
        db_column='recipient',
        max_length=2,
        validators=[MinLengthValidator(2)])

    search_id = models.ForeignKey(
        db_column='search_id',
        on_delete=models.CASCADE,
        to=SearchModel)

    seller_id = models.ForeignKey(
        db_column='seller_id',
        on_delete=models.CASCADE,
        to=SellerModel)
