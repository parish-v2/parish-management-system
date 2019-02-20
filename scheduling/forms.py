from django import forms
from tempus_dominus.widgets import DateTimePicker

from .models import Schedule

class ScheduleForm(forms.ModelForm):
	start_date_time = forms.DateTimeField(widget=DateTimePicker(
				options={
					'useCurrent': True,
					'collapse': True,
					'format': 'MMM D, YYYY HH:mm'
				},
				attrs={
					'append': 'fa fa-calendar',
					'input_toggle': False,
					'icon_toggle': True,
				}),
		input_formats=[
						'%Y-%m-%d %H:%M:%S',    # '2006-10-25 14:30:59'
						'%Y-%m-%d %H:%M',       # '2006-10-25 14:30'
						'%m/%d/%Y %H:%M:%S',    # '10/25/2006 14:30:59'
						'%m/%d/%Y %H:%M',       # '10/25/2006 14:30'
						'%m/%d/%y %H:%M:%S',    # '10/25/06 14:30:59'
						'%m/%d/%y %H:%M',       # '10/25/06 14:30'
						'%b %d, %Y %H:%M']		# 'October 25, 2006 14:30' Custom format
	)

	end_date_time = forms.DateTimeField(widget=DateTimePicker(
				options={
					'useCurrent': True,
					'collapse': True,
					'format': 'MMM D, YYYY HH:mm'
				},
				attrs={
					'append': 'fa fa-calendar',
					'input_toggle': False,
					'icon_toggle': True,
				}),
		input_formats=[
						'%Y-%m-%d %H:%M:%S',    # '2006-10-25 14:30:59'
						'%Y-%m-%d %H:%M',       # '2006-10-25 14:30'
						'%m/%d/%Y %H:%M:%S',    # '10/25/2006 14:30:59'
						'%m/%d/%Y %H:%M',       # '10/25/2006 14:30'
						'%m/%d/%y %H:%M:%S',    # '10/25/06 14:30:59'
						'%m/%d/%y %H:%M',       # '10/25/06 14:30'
						'%b %d, %Y %H:%M']		# 'October 25, 2006 14:30' Custom format
	)

	class Meta:
		model = Schedule
		# fields = '__all__'  # use all fields
		fields = ['title', 'details', 'start_date_time', 'end_date_time']