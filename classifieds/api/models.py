from django.db import models


class Company(models.Model):
    """
    Company Model

    A representation of a company that provides sellers
    for the platform

    """
    address_id = models.ForeignKey(
        db_column='address_id',
        on_delete=models.PROTECT,
        to=Address)

    billing_id = models.ForeignKey(
        db_column='billing_id',
        on_delete=models.PROTECT,
        to=Billing)

    created_at = models.DateTimeField(
        auto_now_add=True,
        db_column='created_at',
        editable=False)

    description = models.TextField(
        db_column='description')

    email = models.CharField(
        db_column='email',
        unique=True)

    header_pic = models.CharField(
        db_column='header_pic',
        max_length=2048)

    name = models.CharField(
        db_column='name',
        max_length=192)

    password_id = models.ForeignKey(
        db_column='password_id',
        on_delete=models.PROTECT,
        to=Password)

    phone = models.CharField(
        db_column='phone',
        max_length=15)


class User(models.Model):
    """
    User Model

    A representation of a user that provides a superclass
    for Buyers and Sellers

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


class Buyer(models.Model):
    """
    Buyer Model

    A representation of a buyer that can buy products
    and services from our platform

    """
    address_id = models.ForeignKey(
        db_column='address_id',
        on_delete=models.PROTECT,
        to=Address)

    billing_id = models.ForeignKey(
        db_column='billing_id',
        on_delete=models.PROTECT,
        to=Billing)

    email = models.CharField(
        db_column='email',
        max_length=192,
        unique=True)

    name = models.CharField(
        db_column='name',
        max_length=192)

    phone = models.CharField(
        db_column='phone',
        max_length=15)

    profile_pic = models.CharField(
        db_column='profile_pic',
        max_length=2048)

    user_id = models.ForeignKey(
        db_column='user_id',
        on_delete=models.CASCADE,
        to=User)


class Seller(models.Model):
    """
    Seller Model

    A representation of a seller that can sell products
    and services from our platform

    """
    address_id = models.ForeignKey(
        db_column='address_id',
        on_delete=models.PROTECT,
        to=Address)

    billing_id = models.ForeignKey(
        db_column='billing_id',
        on_delete=models.PROTECT,
        to=Billing)

    company_id = models.ForeignKey(
        db_column='company_id',
        null=True,
        on_delete=models.PROTECT,
        to=Company)

    email = models.CharField(
        db_column='email',
        max_length=192,
        null=True,
        unique=True)

    name = models.CharField(
        db_column='name',
        max_length=192)

    phone = models.CharField(
        db_column='phone',
        max_length=15)

    profile_pic = models.CharField(
        db_column='profile_pic',
        max_length=2048)

    user_id = models.ForeignKey(
        db_column='user_id',
        on_delete=models.CASCADE,
        to=User)


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


class Address(models.Model):
    """
    Address Model

    Holds the address information of a user

    """
    city = models.CharField(
        db_column='city',
        max_length=192)

    country = models.CharField(
        db_column='country',
        max_length=192)

    postal_code = models.CharField(
        db_column='postal_code',
        max_length=16)

    province = models.CharField(
        db_column='province',
        max_length=192)

    street = models.CharField(
        db_column='street',
        max_length=192)


class Billing(models.Model):
    """
    Billing Model

    Holds the billing information of a user

    """
    cvv = models.CharField(
        db_column='cvv',
        max_length=4)

    expiry = models.DateField(
        db_column='expiry')

    name = models.CharField(
        db_column='name',
        max_length=192)

    number = models.CharField(
        db_column='number',
        max_length=19)


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


class Item(models.Model):
    """
    Item Model

    A representation of a product or service that
    can be purchased by a buyer or seller

    """
    TYPE = (
        ('PR', 'Product'),
        ('SR', 'Service'),
    )

    available = models.BooleanField(
        db_column='available')

    created_at = models.DateTimeField(
        auto_now_add=True,
        db_column='created_at',
        editable=False)

    name = models.CharField(
        db_column='name',
        max_length=192,
        unique=True)

    type = models.CharField(
        db_column='type',
        max_length=2,
        choices=TYPE)


class ItemRequest(models.Model):
    """
    Item Request Model

    A request made by a buyer to search for sellers
    that can sell the item they want

    """
    buyer_id = models.ForeignKey(
        db_column='buyer_id',
        on_delete=models.CASCADE,
        to=Buyer)

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

    purchase_date = models.DateTimeField(
        db_column='purchase_date')


class ItemResponse(models.Model):
    """
    Item Response Model

    A response made by a seller to respond to a
    request made by a buyer

    """
    item_id = models.ForeignKey(
        db_column='item_id',
        on_delete=models.CASCADE,
        to=Item)

    message = models.CharField(
        db_column='message',
        max_length=1024)

    price = models.DecimalField(
        db_column='price',
        max_digits=7,
        decimal_places=2)

    seller_id = models.ForeignKey(
        db_column='seller_id',
        on_delete=models.CASCADE,
        to=Seller)


class Message(models.Model):
    created_at = models.DateTimeField()
    _from = models.ForeignKey(User, name='from')
    to = models.ForeignKey(User)
    message = models.CharField()


class Order(models.Model):
    created_at = models.DateTimeField()
    item = models.ForeignKey(Item)
    buyer = models.ForeignKey(Buyer)
    seller = models.ForeignKey(Seller)
    purchase_date = models.DateTimeField()
    price = models.FloatField()
    description = models.CharField()
    completed = models.BooleanField()


class ItemsOffered(models.Model):
    item_id = models.ForeignKey(
        db_column='item_id',
        on_delete=models.CASCADE,
        to=Item)

    seller_id = models.ForeignKey(
        db_column='seller_id',
        on_delete=models.CASCADE,
        to=Seller)
