from django.forms import ModelForm
from .models import Baptism,Confirmation,Marriage,Profile

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

class ConfirmationModelForm(ModelForm):
    class Meta:
        model = Confirmation
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

class MarriageModelForm(ModelForm):
    class Meta:
        model = Marriage
        exclude = ['id',
                'registry_number',
                'record_number',
                'page_number',
                'remarks',
                'date',
                'target_price',
                'status',
                'groom_profile',
                'bride_profile',
                ]