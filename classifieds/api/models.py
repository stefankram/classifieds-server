from django.db import models


class Company(models.Model):
    created_at = models.DateTimeField()
    name = models.CharField()
    description = models.CharField()
    email = models.CharField()
    password = models.ForeignKey(Password)
    address = models.ForeignKey(Address)
    billing = models.ForeignKey(Billing)
    header_pic = models.CharField()


class User(models.Model):
    created_at = models.DateTimeField()
    name = models.CharField()
    username = models.CharField()
    password = models.ForeignKey(Password)


class Buyer(models.Model):
    user_id = models.ForeignKey(User)
    email = models.CharField()
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
    created_at = models.DateTimeField()
    name = models.CharField()
    type = models.CharField()
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
