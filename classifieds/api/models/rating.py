from django.db import models


class Rating(models.Model):
    """
    Rating Model

    Holds the rating information of a user

    """
    review = models.TextField(
        db_column='review')

    score = models.DecimalField(
        db_column='score',
        decimal_places=2,
        max_digits=3)
