from django.db import models


class Company(models.Model):
    created_at = models.DateTimeField()
    name = models.CharField()
    description = models.CharField()
    email = models.CharField()
    password = models.ForeignKey(Password)
    address = models.ForeignKey(Address)
    billing = models.ForeignKey(Billing)


class User(models.Model):
    created_at = models.DateTimeField()
    name = models.CharField()
    username = models.CharField()
    password = models.ForeignKey(Password)


class Buyer(models.Model):
    user_id = models.ForeignKey(User)
    email = models.CharField()
    address = models.ForeignKey(Address)
    billing = models.ForeignKey(Billing)


class Seller(models.Model):
    user_id = models.ForeignKey(User)
    company_id = models.ForeignKey(Company)


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


class Product(models.Model):
    created_at = models.DateTimeField()
    name = models.CharField()


class ProductRequest(models.Model):
    buyer_id = models.ForeignKey(Buyer)
    product_id = models.ForeignKey(Product)
    description = models.CharField()


class ProductResponse(models.Model):
    seller_id = models.ForeignKey(Seller)
    product_id = models.ForeignKey(Product)
    message = models.CharField()
    price = models.FloatField()
    


class Service(models.Model):
    created_at = models.DateTimeField()
    name = models.CharField()


class ServiceRequest(models.Model):
    buyer_id = models.ForeignKey(Buyer)
    service_id = models.ForeignKey(Service)
    description = models.CharField()
