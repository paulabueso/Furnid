from django.contrib import admin

# Register your models here.
from furnid.models import FurnitureList, Item, Buyer, Offer


admin.site.register(FurnitureList)
admin.site.register(Item)
admin.site.register(Buyer)
admin.site.register(Offer)
# admin.sire.refister()

