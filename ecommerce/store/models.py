from django.db import models
from django.contrib.auth.models import User
from django.db.models import OneToOneField, CharField, CASCADE, Model, \
    FloatField, BooleanField, ForeignKey, SET_NULL, DateField


# Create your models here.

class Customer(Model):
    user = OneToOneField(User, null=True, blank=True, on_delete=CASCADE)
    name = CharField(max_length=200, null=True)
    email = CharField(max_length=200)

class Product(Model):
    name = CharField(max_length=200)
    price = FloatField()
    digital = BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.name


class Order(Model):
    customer = ForeignKey(Customer, on_delete=SET_NULL, blank=True, null=True) # po co nam zamówienie gdy nie ma klienta?
    date_order = DateField(auto_now_add=True)
    complete = BooleanField(default=False, null=True, blank=False)
    transaction_id = CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)