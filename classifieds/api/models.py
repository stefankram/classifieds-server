from django.db import models


#
# Model: Company
#
# Description: A company that provides sellers
#
class Company(models.Model):
    created_at = models.DateTimeField(
        db_column='created_at',
        auto_now_add=True,
        editable=False
    )

    name = models.CharField(
        db_column='name',
        max_length=192
    )

    description = models.TextField(
        db_column='description'
    )

    email = models.CharField(
        db_column='email',
        unique=True
    )

    header_pic = models.CharField(
        db_column='header_pic',
        max_length=2048
    )

    password_id = models.ForeignKey(
        Password,
        db_column='password_id',
        on_delete=models.CASCADE
    )

    address_id = models.ForeignKey(
        Address,
        db_column='address_id',
        on_delete=models.CASCADE
    )

    billing_id = models.ForeignKey(Billing, on_delete=models.CASCADE)


class User(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    name = models.CharField(max_length=192)
    username = models.CharField(unique=True)
    password = models.ForeignKey(Password, on_delete=models.CASCADE)


class Buyer(models.Model):
    user_id = models.ForeignKey(User)
    email = models.CharField(unique=True)
    phone = models.CharField()
    address = models.ForeignKey(Address)
    billing = models.ForeignKey(Billing)
    rating = models.ForeignKey(Rating)
    profile_pic = models.CharField()


class Seller(models.Model):
    user_id = models.ForeignKey(User)
    phone = models.CharField()
    address = models.ForeignKey(Address)
    company_id = models.ForeignKey(Company)
    rating = models.ForeignKey(Rating)
    profile_pic = models.CharField()


class Password(models.Model):
    hash = models.CharField()
    salt = models.CharField()


class Address(models.Model):
    street = models.CharField()
    city = models.CharField()
    province = models.CharField()
    country = models.CharField()
    postal_code = models.CharField()


class Billing(models.Model):
    name = models.CharField()
    number = models.CharField()
    expiry = models.DateField()
    cvv = models.CharField()


class Rating(models.Model):
    score = models.FloatField()
    review = models.CharField()


class Item(models.Model):
    TYPE = (
        ('PR', 'Product'),
        ('SR', 'Service'),
    )

    created_at = models.DateTimeField()
    name = models.CharField(unique=True)
    type = models.CharField(
        max_length=2,
        choices=TYPE)
    available = models.BooleanField()


class ItemRequest(models.Model):
    created_at = models.DateTimeField()
    buyer_id = models.ForeignKey(Buyer)
    item_id = models.ForeignKey(Item)
    description = models.CharField()
    purchase_date = models.DateTimeField()


class ItemResponse(models.Model):
    seller_id = models.ForeignKey(Seller)
    item_id = models.ForeignKey(Item)
    message = models.CharField()
    price = models.FloatField()


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
