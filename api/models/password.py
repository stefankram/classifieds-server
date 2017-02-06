from django.core.validators import MinLengthValidator
from django.db import models


class PasswordModel(models.Model):
    """
    Password Model

    Description
    -----------
    Contains the password information of a user

    Instance Variables
    ------------------
    hash: string
        The hash of the user's password
    salt: string
        The salt of the user's password
    """
    hash = models.CharField(
        db_column='hash',
        max_length=256,
        validators=[MinLengthValidator(256)])

    salt = models.CharField(
        db_column='salt',
        max_length=256,
        validators=[MinLengthValidator(256)])
