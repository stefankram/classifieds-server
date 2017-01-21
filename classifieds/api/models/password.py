from django.db import models


class Password(models.Model):
    """
    Password Model

    Holds the hash and salt of a user password

    """
    hash = models.CharField(
        db_column='hash',
        max_length=256)

    salt = models.CharField(
        db_column='salt',
        max_length=256)