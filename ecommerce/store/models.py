from django.db import models
from django.contrib.auth.models import User
from django.db.models import OneToOneField, CharField, CASCADE, Model, \
    FloatField, BooleanField, ForeignKey, SET_NULL, DateField, IntegerField, ImageField


# Create your models here.

class Customer(Model):
    user = OneToOneField(User, null=True, blank=True, on_delete=CASCADE)
    name = CharField(max_length=200, null=True)
    email = CharField(max_length=200)


class Product(Model):
    name = CharField(max_length=200)
    price = FloatField()
    digital = BooleanField(default=False, null=True, blank=True)
    image = ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    #property decorator let us access the function as attribute/variable, not as a method/function.
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Order(Model):
    customer = ForeignKey(Customer, on_delete=SET_NULL, blank=True,
                          null=True)  # po co nam zamówienie gdy nie ma klienta?
    date_order = DateField(auto_now_add=True)
    complete = BooleanField(default=False, null=True, blank=False)
    transaction_id = CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)


class OrderItem(Model):
    product = ForeignKey(Product, on_delete=SET_NULL, blank=True, null=True)
    order = ForeignKey(Order, on_delete=SET_NULL, blank=True, null=True)
    quantity = IntegerField(default=0, null=True, blank=True)
    date_added = DateField(auto_now_add=True)


class ShippingAddress(Model):
    customer = ForeignKey(Customer, on_delete=SET_NULL, null=True)
    order = ForeignKey(Order, on_delete=SET_NULL, null=True)
    address = CharField(max_length=200, null=False)
    city = CharField(max_length=200, null=True)
    state = CharField(max_length=200, null=True)
    zipcode = CharField(max_length=200, null=True)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.address