from django.db import models


class User(models.Model):
    """
    User Model

    A representation of a user that provides a superclass for Buyers and
    Sellers

    """
    created_at = models.DateTimeField(
        auto_now_add=True,
        db_column='created_at',
        editable=False)

    username = models.CharField(
        db_column='username',
        max_length=192,
        unique=True)

    password_id = models.ForeignKey(
        db_column='password_id',
        on_delete=models.PROTECT,
        to=Password)