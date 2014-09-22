from django.db import models

from django.contrib.auth.models import User


class FurnitureList(models.Model):

    message = models.CharField(max_length=150)
    # pick_up_date = models.DateTimeField(null=True, blank=True)
    city = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    balance = models.IntegerField(default=0, name='start auction at:')

    def __unicode__(self):
        return self.message


class Item(models.Model):
    name = models.CharField(max_length=30)
    number = models.IntegerField()
    description = models.CharField(max_length=150)
    list = models.ForeignKey(FurnitureList)

    def __unicode__(self):
        return self.name


class Buyer(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    phone = models.IntegerField()

    def __unicode__(self):
        return self.name


class Offer(models.Model):
    quantity = models.IntegerField(default=0)
    customer = models.ForeignKey(Buyer)
    list_bid = models.ForeignKey(FurnitureList)
