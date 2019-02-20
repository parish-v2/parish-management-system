from django.forms import ModelForm
from .models import Baptism,Confirmation,Marriage,Profile,Sponsor
from tempus_dominus.widgets import DatePicker
from django.forms import DateField,formset_factory


class ProfileModelForm(ModelForm):
    # birthdate = DateField(widget=DatePicker())
    class Meta:
        model = Profile
        exclude = ['id']
        # widgets = {
		# 	'birthdate': DatePicker(
                
		# 		options={
		# 			'useCurrent': True,
		# 			'collapse': True,
		# 		},
		# 		attrs={
		# 			'append': 'fa fa-calendar',
		# 			'input_toggle': False,
		# 			'icon_toggle': True,
		# 		}
		# 	)
        #     }


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

class SponsorModelForm(ModelForm):
    class Meta:
        model = Sponsor
        exclude = ['id','baptism','confirmation','marriage']

SponsorFormset = formset_factory(SponsorModelForm, extra=1)