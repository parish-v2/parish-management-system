from django.forms import ModelForm,NumberInput
from .models import ItemType, Invoice, InvoiceItem

class ItemTypeModelForm(ModelForm):
    class Meta:
        model = ItemType
        exclude = ['id']

class InvoiceModelForm_Application(ModelForm):
    class Meta:
        model = Invoice
        exclude =['id', 'date_issued','profile_A','profile_B']

class InvoiceItemModelForm_Application(ModelForm):
    class Meta:
        model = InvoiceItem
        exclude =['id','quantity','invoice','item_type']