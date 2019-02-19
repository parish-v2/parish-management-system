from django.contrib import admin
from .models import ItemType,Invoice,InvoiceItem
# Register your models here.
admin.site.register(ItemType)
admin.site.register(Invoice)
admin.site.register(InvoiceItem)