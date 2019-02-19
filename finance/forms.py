from django.forms import ModelForm
from .models import ItemType

class ProfileModelForm(ModelForm):
    class Meta:
        model = ItemType
        exclude = ['id']