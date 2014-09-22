from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from furnid.forms import AddListForm, AddItemForm, MakeOfferForm, CustomerForm
from django.db import models
import datetime
from furnid.models import FurnitureList, Item


def home(request):
    return render(request, 'home.html')


def profile(request):
    furn = FurnitureList.objects.all()
    items = Item.objects.all()
    data = {'furn': furn, 'items': items}
    return render(request, "profile.html", data)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("profile")

    else:
        form = UserCreationForm()

    return render(request, "registration/register.html", {
        'form': form,
    })


def add_list(request):
    if request.method == 'POST':
        form = AddListForm(request.POST)
        if form.is_valid():
            if form.save():
                return redirect("/profile")
    else:
        form = AddListForm()
    data = {'form': form}
    return render(request, "add_list.html", data)


def add_item(request):
    if request.method == 'POST':
        form = AddItemForm(request.POST)
        if form.is_valid():
            if form.save():
                return redirect("/profile")
    else:
        form = AddItemForm()
    data = {'form': form}
    return render(request, "add_item.html", data)


def customer(request):
    furn = FurnitureList.objects.all()
    items = Item.objects.all()
    data = {'furn': furn, 'items': items}
    return render(request, "customer.html", data)


def offer(request):
    form = MakeOfferForm
    data = {'form': form}
    return render(request, "offer.html", data)


def customerinfo(request):
    form = CustomerForm
    data = {'form': form}
    return render(request, "customerinfo.html", data)


def what(request):
    return render(request, 'what.html')

def how(request):
    return render(request, 'how.html')

def contact(request):
    return render(request, 'contact.html')







