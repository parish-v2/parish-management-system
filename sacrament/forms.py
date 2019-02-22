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

    def __init__(self, *arg, **kwarg):
        super(SponsorModelForm, self).__init__(*arg, **kwarg)
        self.empty_permitted = False

    class Meta:
        model = Sponsor
        exclude = ['id','baptism','confirmation','marriage']
    
    # def is_valid(self):
    #     if (self.instance.first_name == None or 
    #         self.instance.last_name == None or
    #         self.instance.middle_name == None or 
    #         self.instance.residence == None):
    #         return False
    #     else:
    #         return True
    # def is_valid(self):
    #     if(self.instance.first_name is not None and 
    #         self.instance.middle_name is not None and
    #         self.instance.last_name is not None and
    #         self.instance.residence is not None):
    #             return True
    #     else:
    #         return False
            
SponsorFormset = formset_factory(SponsorModelForm, extra=2)