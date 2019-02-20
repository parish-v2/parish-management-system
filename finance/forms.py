from django.forms import ModelForm
from .models import ItemType

class ItemTypeModelForm(ModelForm):
    class Meta:
        model = ItemType
        exclude = ['id']