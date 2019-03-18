from django.forms import ModelForm, Form ,ValidationError
from .models import Baptism, Confirmation, Marriage, Profile, Sponsor
from tempus_dominus.widgets import DatePicker
from django.forms import DateField, formset_factory, ValidationError, BaseFormSet
from datetime import datetime
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class ProfileModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProfileModelForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        #helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        # helper.layout = Layout(
        # 'first_name',
        # 'last_name')

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
    def clean_birthdate(self):
        birthdate = self.cleaned_data['birthdate']
        if birthdate > datetime.now().date():
            raise ValidationError("Invalid Birthdate")
        return  birthdate

    def clean(self):
        titleCase = lambda x: x.title() if x else ""
        cleaned_data = super().clean()
        cleaned_data['first_name']= titleCase(cleaned_data['first_name'])
        cleaned_data['middle_name']= titleCase(cleaned_data['middle_name'])
        cleaned_data['last_name']= titleCase(cleaned_data['last_name'])
        cleaned_data['suffix']= titleCase(cleaned_data['suffix'])
        cleaned_data['residence']= titleCase(cleaned_data['residence'])
        cleaned_data['birthplace']= titleCase(cleaned_data['birthplace'])
        return cleaned_data
    
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

class RequiredFormSet(BaseFormSet):
    def clean(self):
        if any(self.errors):
            #return 
            raise ValidationError('Please add at least one vehicle.') 
        #if not self.forms[0].has_changed():
        #    raise forms.ValidationError('Please add at least one vehicle.') 

class SponsorModelForm(ModelForm):

    class Meta:
        model = Sponsor
        exclude = ['id', 'baptism', 'confirmation', 'marriage']

    def clean(self):
        cleaned_data = super().clean()
        try:
            cleaned_data['first_name']
            cleaned_data['middle_name'] 
            cleaned_data['last_name']
            cleaned_data['residence']
            return cleaned_data
        except:
            raise ValidationError("Please fill in all fields")

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

class Submit_Form(Form):
    helper = FormHelper()
    helper.add_input(Submit('submit', 'Submit'))
    def __init__(self, *args, **kwargs):
        super(Submit_Form, self).__init__(*args, **kwargs)

    