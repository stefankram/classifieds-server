from django.core.validators import MinLengthValidator
from django.db import models

from .seller import SellerModel
from .buyer import BuyerModel


class RatingModel(models.Model):
    """
    Rating Model

    Description
    -----------
    A rating sent from either a seller to a buyer or vice-versa

    Constants
    ---------
    RECIPIENTS: [(code: string, who: string)]
        The choices of recipients for the rating

    Instance Variables
    ------------------
    buyer_id: models.ForeignKey
        The buyer
    created_at: datetime
        The creation date of the rating
    review: string
        The rating's review
    recipient: string
        Who will receive the rating
    score: decimal
        The score of the rating
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

    review = models.TextField(
        db_column='message')

    recipient = models.CharField(
        choices=RECIPIENTS,
        db_column='recipient',
        max_length=2,
        validators=[MinLengthValidator(2)])

    score = models.DecimalField(
        db_column='score',
        decimal_places=2,
        max_digits=3)

    seller_id = models.ForeignKey(
        db_column='seller_id',
        on_delete=models.CASCADE,
        to=SellerModel)
