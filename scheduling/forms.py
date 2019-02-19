from django import forms
from tempus_dominus.widgets import DateTimePicker
import datetime

from .models import Schedule

class ScheduleForm(forms.ModelForm):
	class Meta:
		model = Schedule
		# fields = '__all__'  # use all fields
		fields = ['title', 'details', 'start_date_time', 'end_date_time']
		widgets = {
			'start_date_time': DateTimePicker(
				options={
					'useCurrent': True,
					'collapse': True,
				},
				attrs={
					'append': 'fa fa-calendar',
					'input_toggle': False,
					'icon_toggle': True,
				}
			),


			'end_date_time': DateTimePicker(
				options={
					'useCurrent': True,
					'collapse': True,
				},
				attrs={
					'append': 'fa fa-calendar',
					'input_toggle': False,
					'icon_toggle': True,
				}
			),
		}