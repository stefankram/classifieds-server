from django.db import models
from django.core.validators import MinLengthValidator
from pycountry import countries, subdivisions


class AddressModel(models.Model):
    """
    Address Model

    Description
    -----------
    Contains the address information of a user

    Constants
    ---------
    COUNTRIES: [(alpha_2: string, name: string)]
        All countries in the world
    PROVINCES: [(code: string, name: string)]
        All provinces/states in the world

    Instance Variables
    ------------------
    city: string
        The city of the user
    country: string
        The country of the user
    postal_code: string
        The postal/zip code of the user
    province: string
        The province/state of the user
    street: string
        The street address of the user
    """
    COUNTRIES = [(i.alpha_2, i.name) for i in list(countries)]
    PROVINCES = [(i.code, i.name) for i in list(subdivisions)]

    city = models.CharField(
        db_column='city',
        max_length=192)

    country = models.CharField(
        choices=COUNTRIES,
        db_column='country',
        max_length=2,
        validators=[MinLengthValidator(2)])

    postal_code = models.CharField(
        db_column='postal_code',
        max_length=16)

    province = models.CharField(
        choices=PROVINCES,
        db_column='province',
        max_length=5,
        validators=[MinLengthValidator(5)])

    street = models.CharField(
        db_column='street',
        max_length=192)
