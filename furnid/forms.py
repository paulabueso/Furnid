from django import forms
from django.forms import ModelForm
from furnid.models import FurnitureList, Item, Offer, Buyer


class AddListForm(ModelForm):
    class Meta:
        model = FurnitureList


class AddItemForm(ModelForm):
    class Meta:
        model = Item


class MakeOfferForm(ModelForm):
    class Meta:
        model = Offer


class CustomerForm(ModelForm):
    class Meta:
        model = Buyer



