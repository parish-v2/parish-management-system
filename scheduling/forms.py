from django import forms
from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker
import datetime

from .models import Schedule

class ScheduleForm(forms.ModelForm):
	class Meta:
		model = Schedule
		# fields = '__all__'  # use all fields
		fields = ['title', 'details', 'start_date_time', 'end_date_time']
		widgets = {
			# 'name': Textarea(attrs={'cols': 80, 'rows': 20}),
			'start_date_time' : DateTimePicker(
				options={
					'minDate': (datetime.date.today() + datetime.timedelta(days=1)).strftime('%Y-%m-%d'),  # Tomorrow
					'useCurrent': True,
					'collapse': False,
				},
				attrs={
					'append': 'fa fa-calendar',
					'input_toggle': False,
					'icon_toggle': True,
				}
			),
			
		}