from django.forms import ModelForm
from .models import Baptism,Profile

class ProfileModelForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['id']

class BaptismModelForm(ModelForm):
    class Meta:
        model = Baptism
        exclude = ['id',
                'registry_number',
                'record_number',
                'page_number',
                'remarks',
                'date',
                'target_price',
                'status',
                'profile',
                ]