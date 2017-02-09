from django.db import models

from .seller import SellerModel


class LocationModel(models.Model):
    """
    Location Model

    Description
    -----------
    Contains the location of the seller

    Instance Variables
    ------------------
    latitude: double
        The latitude of the seller
    longitude: double
        The longitude of the seller
    seller_id: models.ForeignKey
        The key of the seller
    """
    latitude = models.FloatField(
        db_column='latitude')

    longitude = models.FloatField(
        db_column='longitude')

    seller_id = models.ForeignKey(
        db_column='seller_id',
        on_delete=models.CASCADE,
        to=SellerModel)
